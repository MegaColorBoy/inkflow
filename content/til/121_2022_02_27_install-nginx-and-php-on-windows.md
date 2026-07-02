title: Install NGINX and PHP on Windows
date: February 27th, 2022
slug: install-nginx-and-php-on-windows
category: Tutorial
status: active

Thought of writing a small tutorial on how to install NGINX and PHP on Windows. You can also use this as a reference if you wanted to install them on Windows Server too.

<div class="post-notification warning">
	<h3><i class="ph-warning-light"></i> Note</h3>
	<p>This tutorial won't teach you how to configure both PHP and NGINX configurations as there are a lot of tutorials focusing on that topic.</p>
</div>

## Setting up NGINX

1. Download [NGINX for Windows](http://nginx.org/en/docs/windows.html)
2. Go to `C:/` directory and create a folder named `C:/nginx`.
3. Unzip the downloaded `.zip` file in `C:/nginx` directory.
4. Go to `C:/nginx` and create two new folders named `sites-available` and `sites-enabled`.
5. To test, if it's working, double-click on `C:/nginx/nginx.exe` and type `localhost` in the browser. You should be able to see a Welcome page.
6. Kill the NGINX process from Task Manager.

## Setting up PHP

1. Download [PHP 8.1 for Windows](https://windows.php.net/downloads/releases/php-8.1.1-nts-Win32-vs16-x64.zip).
2. Go to `C:/` directory and create a folder named `C:/php` or if you wanted to have multiple versions, `C:/php8.1`.
3. Unzip the downloaded `.zip` file in `C:/php` directory.
4. Add PHP to your system environment variables by adding the path `C:/php`
5. Open Command Prompt and type `php -v`. You see should be able to see the version if it's installed correctly.

## Run NGINX and PHP as separate services

Generally, it's good practice to run both PHP and NGINX as background services or else, you might have to start the processes manually every time the server goes down.

As I was looking for a way to do that, I stumbled upon this post on [StackOverflow](https://stackoverflow.com/questions/40846356/run-nginx-as-windows-service) and it was quite helpful.

### Install NSSM Service Manager

NSSM Service Manager is a free open-source alternative that helps you create a service with the help of GUI. Below are the steps that I followed:

1. Download [NSSM Service Manager](https://nssm.cc/download)
2. Go to `C:/` directory and create a folder named `C:/nssm`.
3. Unzip the downloaded `.zip` file in `C:/nssm` directory.

### Install NGINX as a service

1. Open Command Prompt as an Administrator.
2. Go to `C:/nssm/win64/` directory.
3. Type `nssm install nginx`
4. Define the path of the `nginx.exe` file.
5. Click on `Install Service`.
6. Press `Win+R` and type `services.msc`.
7. Look for `nginx` and start the service.
8. Open your browser and type `localhost` to see if it's working correctly.

### Install PHP as a service

1. Open Command Prompt as an Administrator.
2. Go to `C:/nssm/win64/` directory.
3. Type `nssm install php`
4. Define the path of the `php-cgi.exe` file.
5. Add the arguments: `-b 127.0.0.1:9000`
6. Click on `Install Service`.
7. Press `Win+R` and type `services.msc`.
8. Look for `php` and start the service.

### Test to see if it works!
Before you proceed with the following steps, ensure that you include the `*.conf` files from the `sites-enabled` folder in your `nginx.conf` file.

Add the line `include "C:/nginx/sites-enabled/*.conf";` in your `nginx.conf` file and follow the steps below:

1. Go to `C:/nginx/sites-available` directory and create `example.com.conf`.
2. Go to `C:/nginx/html` and create directory.
2. Refer to the [sample configuration](#nginx-config) provided and make the necessary changes.
3. To enable the site, you have to create a symlink: `mklink "C:\nginx\sites-enabled\example.com.conf" "C:\nginx\sites-available\example.com.conf"`.
4. Ensure the configuration doesn't have any errors by typing `nginx -t` in `C:/nginx` directory.
5. Restart the NSSM service.
6. Add an entry in your hosts file: `127.0.0.1 example.com`.
7. And you're done!

<div class="post-notification warning">
	<h3><i class="ph-warning-light"></i> Tip</h3>
	<p>If you get a "Connection Refused" or error that is similar to that, it's most probably due to firewall or maybe the PHP service isn't running.</p>
</div>

### Useful commands while using NSSM

```bash
# Start a service
nssm start "servicename" 

# Restart a service
nssm restart "servicename" 

# Stop a service
nssm stop "servicename" 

# Install a service
nssm install "servicename" 

# Remove/Uninstall a service
nssm remove "servicename" 
```


### Sample NGINX Virtual Host Configuration

```bash
server {

	# Your Domain Name
	listen 80;
	server_name example.com;

	autoindex off;
	add_header X-Frame-Options "SAMEORIGIN";
	add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
	add_header X-Content-Type-Options "nosniff";
	add_header X-XSS-Protection "1; mode=block";
	add_header Access-Control-Allow-Origin *;

	if (!-e $request_filename) {
		rewrite  ^/[_0-9a-zA-Z-]+(/wp-(content|admin|includes).*) $1 break;
		rewrite  ^/[_0-9a-zA-Z-]+(/.*\.php)$ $1 break;
	}

	# Uncomment these lines if SSL is provided
	#==========================
	#listen 443 ssl;
	#ssl_certificate your-ssl.pem;
	#ssl_certificate_key your-ssl.key;
	#ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
	#ssl_prefer_server_ciphers on;
	#ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
	#==========================

	# Log files for Debugging
	access_log logs/example-access.log;
	error_log logs/example-error.log;

	# Directory
	root "C:/nginx/html/example.com";
	index index.php index.html index.htm;

	location / {
		try_files $uri $uri/ /index.php?$query_string;
	}

	location ~ /\.(?!well-known).* {
		deny all;
		access_log off;
		log_not_found off;
	}

	# Deny yaml, twig, markdown, ini file access
	location ~* /.+\.(markdown|md|twig|yaml|yml|ini)$ {
		deny all;
		access_log off;
		log_not_found off;
	}

	# PHP-FPM Configuration Nginx
	location ~ \.php$ {
		fastcgi_pass   127.0.0.1:9000;
		fastcgi_index  index.php;
		fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
		include        fastcgi_params;
	}
}
```

## Conclusion
If you've gotten this far, give yourself a pat in the back.

Hope you've found this tutorial useful and please share it with your friends and colleagues if they really need it!