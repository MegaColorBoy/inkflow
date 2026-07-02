title: How to cache your queries on your Laravel application?
date: July 5th, 2020
slug: how-to-cache-your-queries-on-your-laravel-application
category: Laravel
status: active

Although, Laravel is a good framework, it's quite heavy when it comes to executing queries especially if you're using the [Eloquent ORM](https://laravel.com/docs/7.x/eloquent) instead of the normal [query builder](https://laravel.com/docs/7.x/queries).

But Laravel does offer the option of caching your queries in the server and will only make calls to your database if there's a change in content.

Quite handy when you're having a content-heavy website and huge amount of user traffic.

Using the `Cache` class, you can cache your queries like this:
```php
<?php
$apples = \Cache::rememberForever('apples_cache', function(){
    return FruitsModel::where('item_name', 'LIKE', '%apples')
        ->get();
});
?>
```
In the above example, `apples_cache` is the key that stores your queries of apples forever and which will be used to obtain your cached results from the server. 

Oh, be sure to create distinctive names for different types of queries or else, you'll end up being confused! &#128540;

You can also give it a time limit in milliseconds:
```php
<?php
$apples = \Cache::remember('apples_cache', 300000, function(){
    return FruitsModel::where('item_name', 'LIKE', '%apples')
        ->get();
});
?>
```

Hope this tip helps you out! &#x1F600;