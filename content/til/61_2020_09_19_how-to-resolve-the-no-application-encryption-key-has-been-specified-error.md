title: How to resolve the "No application encryption key has been specified" error
date: September 19th, 2020
slug: how-to-resolve-the-no-application-encryption-key-has-been-specified-error
category: Laravel
status: active

Are you facing the same error as this article's title? Then this article might help you out.

If you're developing applications using HTTP/SSL Protocols (regardless, you should!) on Laravel, by default, you'll be using Laravel's encrypter but in it's [official documentation](https://laravel.com/docs/7.x/encryption#configuration), it says:

> Before using Laravel's encrypter, you must set a `key` option in your `config/app.php` configuration file. You should use the `php artisan key:generate` command to generate this key since this Artisan command will use PHP's secure random bytes generator to build your key. If this value is not properly set, all values encrypted by Laravel will be insecure.

Just execute the following command in your root directory:
```bash
php artisan key:generate
```
If the error still persists, try clearing the cache by doing the following:
```bash
php artisan config:cache
php artisan cache:clear
php artisan config:clear
```

Hope you found this article useful!
