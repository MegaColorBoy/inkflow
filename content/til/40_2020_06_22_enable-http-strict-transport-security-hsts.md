title: Enable HTTP Strict Transport Security (HSTS)
date: June 22nd, 2020
slug: enable-http-strict-transport-security-hsts
category: Apache
status: active

As part of a project that I was working on, I learnt about [HTTP Strict Transport Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) protocol which tells the browser about making future web requests over HTTPS only. So, even if you attempt to use `http://`, the browser will force you to use `https://` URLs in the future.

You can enable it by writing this header in your `.htaccess` file in your `public` directory:

```bash
Header always set Strict-Transport-Security "max-age=31536000" env=HTTPS
```

Please note that once you enable this protocol, your web application is committed to using SSL i.e. you won't be able to use insecure HTTP for your web application.