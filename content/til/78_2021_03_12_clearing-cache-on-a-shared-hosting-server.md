title: Clearing cache on a Shared Hosting Server
date: March 12th, 2021
slug: clearing-cache-on-a-shared-hosting-server
category: Laravel
status: active

Hosted your website on a Shared Hosting Server and got limited access to clear the cache on your project?

Open up `routes/web.php` and create this route:

```php
&lt;?php
Route::get('/clearcache', function(){
    \Artisan::run('config:clear');
    \Artisan::run('cache:clear');
    \Artisan::run('view:clear');
    \Artisan::run('route:clear');
    \Artisan::run('config:cache');
});
?&gt;
```

Just type the URL and it will clear all existing cache from the project.

Hope this helps you out!