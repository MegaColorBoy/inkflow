title: Convert to date from timestamp using Carbon
date: March 12th, 2021
slug: convert-to-date-from-timestamp-using-carbon
category: Laravel
status: active

Using Carbon's `createFromFormat()` method is basically a wrapper for `DateTime::createFromFormat()`, the main difference between the two methods is that you can add a timezone to Carbon's method.

Here's a sample on how you can convert to date using timestamp using Carbon:

```php
<?php
    function formatDate(Request $request) {
        return \Carbon\Carbon::createFromFormat('Y-m-d H:i:s', $request->date)->format('Y-m-d');
    }
?>
```

Hope you found this useful!