title: Create migrations and seeds from an existing database
date: March 12th, 2021
slug: create-migrations-and-seeds-from-an-existing-database
category: Laravel
status: active

Up until now, I've written migrations and generated seeders for some Laravel projects that I have worked on but recently, I thought of seeing if there's a way to generate migrations and seeds from an existing database especially if it's a project that never had any migrations or seeds created before.

Luckily, I found these two packages, which turned out to be quite productive:

1. [kitloong/laravel-migrations-generator](https://github.com/kitloong/laravel-migrations-generator)
2. [orangehill/iseed](https://github.com/orangehill/iseed)

Execute the following commands to install the packages mentioned above:
```bash
composer require --dev "kitloong/laravel-migrations-generator"
composer require orangehill/iseed
```

## Generate migrations using existing database
You can generate your migrations for all tables like this:
```bash
php artisan migrate:generate
```

Or, you can specify the tables you wish to generate:
```bash
php artisan migrate:generate table1,table2,table3
```

## Generate new seeds using existing database
You can generate seeds for a single table like this:
```bash
php artisan iseed table_name
```

And for multiple tables, you can do this:

```bash
php artisan iseed table1,table2,table3
```

Hope you find this tip useful!.