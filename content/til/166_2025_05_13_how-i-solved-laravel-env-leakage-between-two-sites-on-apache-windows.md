title: Eliminate Laravel .env leakage between multiple sites on Apache (Windows)
date: May 13th, 2025
slug: eliminate-laravel-env-leakage-between-multiple-sites-on-apache-windows
category: PHP + DevOps + Windows + Apache
status: active

Today, I learned something pretty important (and frustrating until I figured it out): if you're running **multiple Laravel applications** on **Apache (Windows)** using `mod_php`, you can run into a strange bug where **one site's `.env` settings override the other**.

This became painfully obvious when I noticed that **one of my Laravel sites was randomly connecting to the wrong database**, even though the configurations in each `.env` were different. Weird, right?

Turns out, the culprit was `mod_php`.

## The problem

I had two Laravel sites hosted on the same Windows machine with Apache. Both were running fine — until they weren’t.

The issue? Sometimes one site would pick up the database config of the other. One minute I’d be on Site A, and then somehow its `.env` settings were coming from Site B. 

This is just total chaos and worse, this issue existed from more two years until I decided to dive into the problem.

## The cause

Laravel loads `.env` values during the bootstrap process and **caches them in memory**. When using `mod_php`, Apache loads PHP as a module **once** and shares it across all sites. That means **only one copy of Laravel’s environment gets loaded — and reused** across both apps.

So even if each app had its own `.env`, it didn’t matter. Apache was essentially saying:

> “Hey, here’s PHP. I already booted Laravel with this config — just reuse it.”

## The solution

After some digging, the solution is **ditch `mod_php`** and switch to **FastCGI (`mod_fcgid`)**.

With FastCGI, each site runs its own instance of PHP via `php-cgi.exe`, which **boots Laravel in isolation** — meaning **each `.env` file is respected per site**.

### How to configure it?

First, you need to disable **`mod_php`** in `httpd.conf`:

```apache
# LoadModule php_module "C:/path/to/php/php8apache2_4.dll"
# <FilesMatch \.php$>
#     SetHandler application/x-httpd-php
# </FilesMatch>
# PHPIniDir "C:/path/to/php/"
```

Then install **`mod_fcgid`** from Apache Lounge and copy `mod_fcgid.so` to `modules/` directory and enable it in `httpd.conf`:

```apache
LoadModule fcgid_module modules/mod_fcgid.so
Include conf/extra/httpd-fcgid.conf
```

Next, you have to create/update **`httpd-fcgid.conf`**:

```apache
<IfModule fcgid_module>
   AddHandler fcgid-script .php
   FcgidInitialEnv PHPRC "C:/path/to/php"
   FcgidWrapper "C:/path/to/php/php-cgi.exe" .php
   Options +ExecCGI
   FcgidMaxProcessesPerClass 150
   FcgidMaxRequestsPerProcess 1000
   FcgidProcessLifeTime 300
   FcgidIOTimeout 120
   FcgidPassHeader Authorization
   FcgidFixPathinfo 0
</IfModule>
```

And then atlast, update your virtual host:

```apache
<VirtualHost *:443>
   ServerName example.com
   DocumentRoot "C:/path/to/website/public"

   <Directory "C:/path/to/website/public">
      Options +ExecCGI -Indexes +FollowSymLinks
      AllowOverride All
      Require all granted
      AddHandler fcgid-script .php
      FCGIWrapper "C:/path/to/php/php-cgi.exe" .php
   </Directory>

   SSLEngine on
   SSLCertificateFile "..."
   SSLCertificateKeyFile "..."
</VirtualHost>
```

Restart the nginx service and clear the laravel application cache:

```bash
httpd -k restart
php artisan config:clear
php artisan cache:clear
```

### Bonus: Fixing 403 Forbidden Errors

After switching to FastCGI, I ran into a `403 Forbidden` error on one site. That turned out to be a **missing `Options +ExecCGI`** and `Require all granted` in the `<Directory>` block. Once added, everything worked perfectly.

## Result

Now, each Laravel site runs completely isolated, even though they use the same `php-cgi.exe`. No more `.env` bleed. No more wrong DBs. Just clean, independent Laravel environments — as it should be.

## Takeaways

* Don’t run multiple Laravel apps on Apache with `mod_php` unless you're okay with shared config risks.
* Use `mod_fcgid` and `php-cgi.exe` for **true isolation**.
* Even if using the **same PHP version**, FastCGI will **spawn separate processes**, so `.env` loading stays scoped.
* Always check Apache error logs (`error.log`) and `php_sapi_name()` for confirmation.

If you’re running Laravel on Windows with Apache — **this fix is a must**. 

Happy hosting and hope you found this article useful!