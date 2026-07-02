title: Create a unique multidimensional array using a key index
date: July 18th, 2020
slug: create-a-unique-multidimensional-array-using-a-key-index
category: PHP
status: active

Let's say, you have a multidimensional array like this:
```php
<?php
$cars = [
    [
        "id" => 1,
        "name" => "Mercedes Benz",
        "color" => "Black"
    ],
    [
        "id" => 2,
        "name" => "Toyota",
        "color" => "Red"
    ],
    [
        "id" => 3,
        "name" => "Toyota",
        "color" => "White"
    ],
    [
        "id" => 4,
        "name" => "Nissan",
        "color" => "Grey"
    ],
];
?>
```

And say, you want to be able to return unique cars by `name` or `color`, use this method:
```php
<?php
function multi_array_unique($array, $key) {
    $i = 0;
    $temp_array = [];
    $key_array = [];
   
    foreach($array as $val) {
        // insert only unique keys
        if (!in_array($val[$key], $key_array)) {
            $key_array[$i] = $val[$key];
            $temp_array[$i] = $val;
        }
        $i++;
    }
    return $temp_array;
}
?>
```

Call this method from anywhere in your code like this:
```php
<?php
$unique_cars = multi_array_unique($cars, "name");
dd($unique_cars);
?>
```

And now, you'll get something like this:
```php
<?php
[
    [
        "id" => 1,
        "name" => "Mercedes Benz",
        "color" => "Black"
    ],
    [
        "id" => 2,
        "name" => "Toyota",
        "color" => "Red"
    ],
    [
        "id" => 4,
        "name" => "Nissan",
        "color" => "Grey"
    ],
];
?>
```

You might wonder why I tried this instead of PHP's `array_unique()` method and the reason I didn't use it is because it doesn't support multidimensional arrays.

Hope you found this useful!