title: Increase memory limit in PHP
date: August 23rd, 2020
slug: increase-memory-limit-in-php
category: PHP
status: active

Last month, I was building a web application that collected a lot of data via form submissions. I wrote a method to export attachments and form data by zipping them all together. 

It worked for a smaller archives but as the records grew larger, I got a fatal error which said that I've exhausted the PHP's memory limit.

So, I found an easy way to increase the memory limit to 1024MB (1GB) like this:

```php
&lt;?php
ini_set('memory_limit', '1024M');
?&gt;
```

Before you write this stub in your script, make sure you have enough resources in your system or else, it'll go splat!