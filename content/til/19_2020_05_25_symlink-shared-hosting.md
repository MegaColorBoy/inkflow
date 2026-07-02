title: Symbolic storage link in shared hosting
date: May 25th, 2020
slug: symlink-shared-hosting
category: Laravel

If you're hosting a laravel project via cPanel, chances are that it could be a shared hosting server and that means you can't really use `php artisan storage:link` for this.
But don't worry, there's another way to this. Just follow the steps below:

## 1. Create a symlink
In your `public_html/public` directory, remove the `storage` folder. Next, create a `symlink.php` file in your `public_html` directory and add the following code:
```php
<?php
$targetFolder = $_SERVER['DOCUMENT_ROOT'].'/storage/app/public';
$linkedFolder = $_SERVER['DOCUMENT_ROOT'].'/public/storage';
symlink($targetFolder, $linkedFolder);
echo "done";
?>
```

## 2. Create a custom route to access storage
Alright, this is kind of a hack but it works extremely fine. Just add the following route in your `routes/web.php` file:
```php
<?php
Route::get('/storage/anyfolder/{filename}', function($filename){
    // Your folder path
    $folder_path = storage_path('app/public/anyfolder/'.$filename);

    // check if the file exists
    if(!File::exists($folder_path)) {
        abort(404);
    }

    $file = File::get($folder_path);
    $type = File::mimeType($folder_path);

    $response = Response::make($file, 200);
    $response->header("Content-Type", $type);

    return $response;
})
?>
```

Now, you can access your images or any other assets easily using: 
```php
<?php
asset('storage/anyfolder/'.$filename)
?>
```

Hope this helps you out!