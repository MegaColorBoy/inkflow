title: Clear a file directory using Filesystem in Laravel
date: September 28th, 2020
slug: clear-a-file-directory-using-filesystem-in-laravel
category: Laravel
status: active

I was working on a project that dealt with generating large .zip exports and as a result, the `storage/exports` directory, which was used to store all the .zip exports, ended up going all the way up to a whopping size of 10 gigabytes! &#x1F62E;

I resolved it by calling the `Filesystem` package in my controller:
```php
<?php
use Illuminate\Filesystem\Filesystem;
?>
```

Then simply, create a new instance and define the directory you wanted to clear:
```php
<?php
$folder = new Filesystem;
$folder->cleanDirectory('storage/exports');
?>
```

Hope this helps you out!