title: Containerize your Laravel application for Development
date: October 23rd, 2022
slug: containerize-your-laravel-application-for-development
category: Tutorial + Docker + DevOps + Laravel
summary: A short tutorial on how to containerize your Laravel application and use it for testing and development purposes.
status: active

Since I started exploring Docker containers during my spare time, I learnt how to containerize a Laravel application using Docker Compose.

In this guide, I'll show you how to containerize your application and by the end of this tutorial, you'll have your application running on four separate service containers:

- App service running `php7.4-fpm`.
- A database service running `mysql-80`.
- An NGINX service.
- A phpMyAdmin service for you to view and manage your database.

## Prerequisites

- You need to have Docker and Docker Compose installed on your system
- A non-root user with sudo privileges (If you are using any UNIX-based environment).
- An existing working Laravel project.

I tried this on my personal laptop that runs on Fedora Workstation 36 and hopefully, it should work on Windows and macOS as well. If you are a Windows user, I would recommend you to try WSL2 with Ubuntu installed in it.

## Configure your app service
First, you need to create a Dockerfile for your app service in your project's root directory:

```bash
touch Dockerfile
vim Dockerfile
```

In this tutorial, I'll be using PHP7.4 but you can use any version that you need. Here you go:

```Dockerfile
FROM php:7.4-fpm

# Arguments defined in docker-compose.yml
ARG user
ARG uid 

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Create system user to run Composer and Artisan Commands
RUN useradd -G www-data,root -u $uid -d /home/$user $user
RUN mkdir -p /home/$user/.composer && \
    chown -R $user:$user /home/$user

# Set working directory
WORKDIR /var/www

USER $user
```

So, what's happening in the configuration above is that, it pulls a PHP7.4-FPM image from Docker Hub. Next, it'll define the user of the service and install all the necessary dependencies that are given above and set the working directory to `/var/www/`. The last step will change to the newly created user, which would make sure that you are using the service as a normal user.

Again, if you are a bit playful, try configuring it to however you want it and see if it works.

## Set up NGINX and MySQL

I have been following some tutorials and I liked the idea of creating dedicated directories to organize your files related to configuring each service container.

Create a directory named `.docker` in your project's root directory:

```bash
mkdir -p .docker
```

### NGINX
Go to `.docker` directory and create `nginx` directory:
```bash
mkdir -p nginx
```

Now let's set up the NGINX service by creating a `.conf` file:

```bash
touch myservice.conf
```

Now, copy the following configuration to your `.conf` file:
```bash
server {
    listen 80;
    index index.php index.html;
    error_log  /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/public;
    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass app:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
    location / {
        try_files $uri $uri/ /index.php?$query_string;
        gzip_static on;
    }
}
```

### MySQL

Since this is a Laravel application, you can skip this step by running migrations and seeding your database or you can try creating a directory inside the `.docker` folder to store your MySQL related configuration:

```bash
mkdir -p mysql
```

Once created, create a file named `init_db.sql` that would contain your entire database dump to be seeded once you run your docker service.

## Set up multiple containers using Docker Compose

This the configuration I have used to create four separate services, please take a look and feel free to modify it based on your requirements.

In this configuration, all services will share a bridge network named `yourapp` which is defined at the bottom of this configuration.

Here is the configuration:

```yaml
version: '3.8'
services:
  # PHP Service
  app:
    build:
      args:
        user: username
        uid: 1000
      context: ./
      dockerfile: Dockerfile
    image: yourapp 
    container_name: yourapp-app
    restart: unless-stopped
    working_dir: /var/www/
    volumes:
      - ./:/var/www
    networks:
      - yourapp
  
  # MySQL Service
  db: 
    image: mysql:8.0
    container_name: yourapp-db
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: ${DB_DATABASE}
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_USER: ${DB_USERNAME}
      SERVICE_TAGS: dev 
      SERVICE_NAME: mysql
    volumes:
      - ./.docker/mysql:/docker-entrypoint-initdb.d
    healthcheck:
      test: mysqladmin ping -h 127.0.0.1 -u ${DB_USERNAME} --password=${DB_PASSWORD}
      interval: 5s
      retries: 10
    networks:
      - yourapp
  
  # NGINX Service
  nginx:
    image: nginx:alpine
    container_name: yourapp-nginx
    restart: unless-stopped
    ports:
      - 8000:80
    volumes:
      - ./:/var/www
      - ./.docker/nginx:/etc/nginx/conf.d/
    networks:
      - yourapp
  
  # phpMyAdmin service
  phpmyadmin:
    image: phpmyadmin/phpmyadmin:5
    ports:
      - 8080:80
    environment:
      PMA_HOST: db
    depends_on:
      db: 
        condition: service_healthy
    networks:
      - yourapp

networks:
  yourapp:
    driver: bridge

```

## Configure your application
Open your current `.env` file of your laravel project and just add the necessary database configuration:

```yaml
DB_HOST=yourapp-db
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=your_database_user_name
DB_PASSWORD=your_database_password
```

## Build the application image

After you are done with configuring, run the following command to build your application image:

```bash
docker-compose build yourapp
```

Depending on your network speed, it might take a few minutes to build your image.

## Run the application
Once the build is complete, execute the following command:

```bash
docker-compose up -d
```

The following command will run your containers in the background. To display your information about the state of your docker services:

```bash
docker-compose ps
```

Install your application's dependencies:

```bash
docker-compose exec yourapp rm -rf vendor composer.lock
docker-compose exec yourapp composer install
```

And then run the following commands to run your Laravel application:

```bash
docker-compose exec yourapp php artisan key:generate
docker-compose exec yourapp php artisan config:clear
docker-compose exec yourapp php artisan cache:clear
docker-compose exec yourapp php artisan view:clear
docker-compose exec yourapp php artisan route:clear
docker-compose exec yourapp php artisan storage:link 

```

Now, you can go to your browser, type your `http://localhost:8000` to access your application.

## Conclusion
If you've come to this part, give yourself a pat in the back!

From now onwards, you don't really need to install and set up a local web server and database to run and test your application.

Furthermore, you'll be having a disposable environment in your hand, which means you can easily replicate and distribute it to other developers in your team, so that no one says "It works on my machine and not on yours!"

Hope you liked this tutorial!