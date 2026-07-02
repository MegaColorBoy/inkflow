title: Create aliased class constants in Laravel
date: November 7th, 2020
slug: create-aliased-class-constants-in-laravel
category: Laravel
status: active

There are many ways to define constants in Laravel but I learnt a neat technique where you can define constants using an alias.

First off, create the following directory:

```bash
mkdir app/Constants
```

Next, create a file named `MyConstants.php` in the `app/Constants` directory and copy-paste the following code:

```php
<?php
namespace App\Constants;

class MyConstants {
    const HELLO = 'hello';
}
?>
```

Then, go to the `config/app.php` file and define your new alias:

```php
<?php
'aliases' => [
    // previously defined aliases...
    'MyConstants' => App\Constants\MyConstants::class,
]
?>
```

Lastly, execute the following commands to update your app's configuration:

```bash
php artisan config:clear
composer dump-autoload
php artisan config:cache
```

After that, you can use your new constants anywhere (Controllers, Models or Blades) like this:

```php
<?php
echo MyConstants::HELLO;
?>
```

Learning this new technique helps me keep the code clean and makes it easier to trace the constants.

Hope you find this tip useful!