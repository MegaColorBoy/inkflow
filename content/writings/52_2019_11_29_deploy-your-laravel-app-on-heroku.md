title: Deploy your Laravel app on Heroku
date: November 29th, 2019
slug: deploy-your-laravel-app-on-heroku
category: Tutorial
summary: Learn how to deploy your Laravel application along with a database on Heroku.

In my [previous article](/posts/getting-started-with-laravel-homestead), I talked about how to setup your environment for developing your Laravel applications. Today, I'll be talking about deploying your application along with a database on Heroku.

I wrote a simple CRUD application using Laravel but didn't understand on how to host it. I tried to host it on free shared hosting service but apparently, most of them don't support PHP system calls like <mark>proc_open()</mark>. However, if it was a VPS hosting service, it's supported but ain't nobody got time for shelling out cash for a test drive.

As an alternative, I went on google and discovered that Heroku does support my requirements and it worked flawlessly, which is why I thought of sharing this information to others as well.

If you're a developer who's at the early stages of learning Laravel (like me &#x1f606;), then this article is for you.

## Prerequisites
You'll be doing some minor configurations, so you should be fine as long as you have a stable internet connection, familiar with using the CLI (Command Line Interface) and have some PHP knowledge.

If you're a Windows user, please [Git for Windows](https://gitforwindows.org). Else, if you're a Linux or macOS user, you should be fine.

## How to deploy?
You can ignore the first two steps if you already know about Heroku and how to work with it but please follow the rest of the steps:

1. [Install Heroku](#step-1)
2. [Create a Heroku repository](#step-2)
3. [Define Procfile](#step-3)
4. [Push Laravel app to repository](#step-4)
5. [Add configuration variables](#step-5)
6. [Setup your database](#step-6)

### <a id="step-1"></a> Install Heroku CLI
You can install this directly from the command line by typing the following:

```bash
sudo snap install heroku --classic
```

### <a id="step-2"></a> Create a Heroku repository

If you don't have a Heroku account yet, [create an account](https://heroku.com) now and once you're done with that, type the following:

```bash
heroku login
```

Follow the login instructions from the command line prompt, fill in your login credentials and you'll be in!

Once, you're done with that, create a repository by doing the following:

```bash
heroku create
```

In a few seconds, you'll get a randomly generated domain address, which is the link to your Heroku repository. If you can't remember the link, it's fine, you can make changes to it in your Heroku account.

### <a id="step-3"></a> Define Procfile
In case, you don't know what's a Procfile, it's a file that specifies the commands that needs to be executed by the application on startup. You can declare a variety of process types, [click here](https://devcenter.heroku.com/articles/procfile) to learn more.

Since our application is PHP based, we need to add some specific command that selects the server on boot, I chose Apache server for this project:

```bash
cd your_laravel_project
touch Procfile
echo "web: vendor/bin/heroku-php-apache2 web/" &gt; Procfile
```

### <a id="step-4"></a> Push Laravel app to repository
It's similar to pushing your code into your GitHub, except this time, it's your Heroku repository. Type the following in your command line:

```bash
git add .
git commit -m "pushing application to repo"
git push heroku master
```

To check if your application is launched, type the following:

```bash
heroku open
```

At this stage, you might face <mark>Error 500</mark>, that's normal because we'll take care of that in the next step.

### <a id="step-5"></a> Configure your Heroku environment
We need to add some config variables that changes the way your app behaves. So, let's start adding it:

```bash
heroku config:set APP_DEBUG=true
heroku config:set APP_KEY=yourlaravelapplicationkey
heroku config:set APP_URL=https://yourwebsite.herokuapp.com
heroku config:set REDIRECT_HTTPS=true
```

In this configuration, you have done the following:
- Enabled debug mode
- Set your Laravel application's base64 encrypted key
- The website's URL
- Force HTTPS redirect (Useful, when you're calling external assets that uses HTTPS protocol)

**Note:** You can find your <mark>APP_KEY</mark> in your <mark>.env</mark> file that's found in your project directory.

### <a id="step-6"></a> Setup your database
Initially, I built the database on MySQL but I later learnt that Heroku gives a free PostgreSQL starter database. I've never tried PostgreSQL before but it's quite similar to MySQL, so you shouldn't worry about your schema as Laravel supports PostgreSQL and MySQL databases by default.

Type the following in the command line:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

This will create a PostgreSQL database and sets a <mark>DATABASE_URL</mark>, which contains the username and password to the database. To check it, type the following:

```bash
heroku config
```

Now, go to your project directory and open the <mark>config/database.php</mark>  file and add the following:
```php
<?php
// Place these variables above
$url = parse_url(getenv("DATABASE_URL"));
$host = $url["host"]??null;
$username = $url["user"]??null;
$password = $url["pass"]??null;
$database = substr($url["path"], 1)??null;

// Replace the default connection
'default' => env('DB_CONNECTION', 'pgsql_prod'),

// Under the connections attribute, create a new connection called 'pgsql_prod'
'pgsql_production' => [
    'driver' => 'pgsql',
    'host' => $host,
    'database' => $database,
    'username' => $username,
    'password' => $password,
    'charset' => 'utf-8',
    'prefix' => '',
    'schema' => 'public',
],
?>
```

Push the new changes to your repository:
```bash
git add .
git commit -m "configured database"
git push heroku master
```

One last step, we need to create the tables from your schema, so type the following:
```bash
heroku run php /app/artisan migrate --seed
```

Follow the command line prompt and voila, you have successfully deployed your Laravel application with a database on Heroku.

## Conclusion
Well, I hope you found this article really useful especially if you're a beginner. If you do find this useful, please share it with others too!

Stay tuned for more!