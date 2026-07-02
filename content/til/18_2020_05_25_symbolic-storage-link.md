title: Create a symbolic storage link
date: May 25th, 2020
slug: symbolic-storage-link
category: Laravel

When using Laravel, the `public` directory is used for files that are publicly accessible. By default, it's stored in `local` and often stored in this `storage/app/public` directory. You can make it easily accessible by using the following command:

```bash
php artisan storage:link
```

Once, it has been created, you can use access those files using the `public_path` or `asset` methods.

```php
<?php
echo public_path('images/sample_1.jpg');
echo asset('images/sample_2.jpg');
?>
```