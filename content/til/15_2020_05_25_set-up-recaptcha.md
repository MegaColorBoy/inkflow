title: Set up reCaptcha in Laravel
date: May 25th, 2020
slug: set-up-recaptcha
category: Laravel

I mean, come on, you need to have a reCaptcha in your forms, no matter what.

Here are the steps:

## 1. Install using Composer
```bash
composer require anhskohbo/no-captcha
```

## 2. Add provider and alias to configuration
Open your `config/app.php` file and add this to your providers array:
```php
<?php
Anhskohbo\NoCaptcha\NoCaptchaServiceProvider::class,
?>
```

And this to your aliases array:
```php
<?php
'NoCaptcha' => Anhskohbo\NoCaptcha\Facades\NoCaptcha::class,
?>
```

## 3. Publish configuration
```bash
php artisan vendor:publish --provider="Anhskohbo\NoCaptcha\NoCaptchaServiceProvider"
```

## 4. Add sitekey and secret key to .env file
Open your `.env` file and add this:
```text
NOCAPTCHA_SITEKEY=yoursitekey
NOCAPTCHA_SECRET=yoursecret
```

## How to use it?
Now, you can use it in your validator using like this:
```php
<?php
$validate = Validator::make(Input::all(),[
    'g-recaptcha-response' => 'required|captcha'
]);
?>
```