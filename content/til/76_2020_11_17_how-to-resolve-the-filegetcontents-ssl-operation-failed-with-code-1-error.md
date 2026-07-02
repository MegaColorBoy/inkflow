title: How to resolve the "file_get_contents(): SSL operation failed with code 1" error
date: November 17th, 2020
slug: how-to-resolve-the-filegetcontents-ssl-operation-failed-with-code-1-error
category: PHP
status: inactive

Last week, I was deployed some changes on a client's server and one of those updates had a function that simply fetches the contents of a `.pdf` file, which then opens up in a new tab via a custom route.

Here's a sample code:
```php
&lt;?php
public function foo() {
    $filename = 'file.pdf';
    $path = storage_path($filename);
    
    return Response::make(file_get_contents($path), 200, [])
}
?&gt;
```

It worked on development environment but it didn't work on the production server. I digged up the `laravel.log` file and found this error:

> file_get_contents(): SSL operation failed with code 1

It was weird and instantly understood that it had something to do with SSL verification. So, I simply resolved the si
