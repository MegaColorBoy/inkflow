title: Forcing HTTP to HTTPS redirect after enabling SSL
date: June 22nd, 2020
slug: forcing-http-to-https-redirect-after-enabling-ssl
category: Apache
status: active

You can manually force HTTP to HTTPS after enabling your SSL certificate by adding the following condition at the beginning of your `.htaccess` file in your `public` directory:

```bash
RewriteCond %{HTTP:X-Forward-Proto} !=https
RewriteRule .* https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
```

Save your file and restart your Apache server and now, your web application will redirect all your users to `https://` instead of `http://` URLs in the future.
