title: Integrate Excel into your Laravel project
date: May 25th, 2020
slug: integrate-excel-into-your-laravel-project
category: Laravel
status: active

Before you integrate Excel into your application, make sure your project meets the following requirements:

- PHP v7.0 or greater
- Laravel v5.5 or greater
- PhpSpreadsheet v1.6 or greater

## Download the package
Download the `maatwebsite/excel` package using Composer:
```bash
composer require maatwebsite/excel
```

## Add it to service provider
By default, this will be done automatically when you're installing the package but if you want to do it yourself, add this in your `config/app.php` file:
```php
<?php
// ...
'providers' => [
    // ...
    Maatwebsite\Excel\ExcelServiceProvider::class,
],

// ...
'aliases' => [
    // ...
    'Excel' => 'Maatwebsite\Excel\Facades\Excel::class',
],
?>;
```

## Publish your configuration
Last but not the least, run the `vendor:publish` command using `artisan` to publish your configuration:
```bash
php artisan vendor:publish -provider="Maatwebsite\Excel\ExcelServiceProvider"
```

Upon publishing, the `config/excel.php` configuration file will be created where you can make your changes.

Hope this helps you out!