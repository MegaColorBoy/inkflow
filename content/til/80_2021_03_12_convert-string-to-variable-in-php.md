title: Convert string to variable in PHP
date: March 12th, 2021
slug: convert-string-to-variable-in-php
category: PHP
status: active

I read about [variable variables](https://www.php.net/language.variables.variable) in PHP's official documentation.

Here's a sample:

```php
<?php
    $a = "hello";
    // Remove special characters and tags to prevent it from crashing.
    $foo = preg_replace('/[^a-zA-Z0-9\s]/', '', $$a);
    echo $foo;
?>
```

Not sure if this is a good practice but it sure gets the job done!