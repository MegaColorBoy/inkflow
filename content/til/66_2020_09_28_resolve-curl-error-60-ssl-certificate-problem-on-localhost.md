title: Resolve cURL error 60: SSL certificate problem on localhost
date: September 28th, 2020
slug: resolve-curl-error-60-ssl-certificate-problem-on-localhost
category: Laravel
status: active

You'll get this error when you're hosting a Laravel project with using HTTPS/SSL protocol on `localhost` or `127.0.0.1`:
```text
cURL error 60: SSL certificate problem: unable to get local issuer certificate (see https://curl.haxx.se/libcurl/c/libcurl-errors.html)
```

I read some article on trying to install `cacert.pem` authorization certificate on your WAMP/XAMPP setup but it didn't really work out for me as I was running out of time.

So, I did a little digging and learnt that I can just modify the `verify` flag to `false` in the `vendor/guzzlehttp/guzzle/src/Client.php` file:
```php
<?php
$defaults = [
    'allow_redirects' => RedirectMiddleware::$defaultSettings,
    'http_errors'     => true,
    'decode_content'  => true,
    'verify'          => false, // changed it to false
    'cookies'         => false
];
?>
```

By changing to it `false`, you'll not face that error again but please keep in mind, you should do this only if you're developing on localhost.

Happy coding!