title: Input sanitization with PHP
date: August 23rd, 2020
slug: input-sanitization-with-php
category: PHP
status: active

This can come in handy when you're dealing with user inputs during a form submission and in most cases, your web application will be using a database query to store the data. 

## Using filter_var()
This method uses a number of flags to validate and sanitize a string. Here are some examples I have tried:

### Removing special characters
Want to strip out all tags and certain characters? Try this:
```php
&lt;?php
$str = "&lt;h1&gt;Hello World&lt;/h1&gt;";
$filtered = filter_var($str, FILTER_SANITIZE_STRING);
echo $filtered;
?&gt;
```

### Integer validation
You can check if the input is an integer and if it's a value between 1 and 20:
```php
&lt;?php
$x = 10;
$min = 1;
$max = 20;
$options = [
    "min_range" => $min,
    "max_range" => $max
];

if(!filter_var($x, FILTER_VALIDATE_INT, $options)){
    echo "This input is invalid.";
}
else {
    echo "This input is valid.";
}
?&gt;
```

### URL validation
Want to check if the input is a valid URL? Try this out:
```php
&lt;?php
// Make sure the URL is sanitized
$url = filter_var("https://www.google.com", FILTER_SANITIZE_URL);
if(filter_var($url, FILTER_VALIDATE_URL)){
    echo "This URL is valid.";
}
else {
    echo "This URL is invalid.";
}
?&gt;
```

Using these in-built features makes it easier for PHP developers to process data from external sources in a safer manner and also adds an extra layer of protection to your web application.

Read more about this method in [PHP's official documentation](https://www.php.net/manual/en/function.filter-var.php).
