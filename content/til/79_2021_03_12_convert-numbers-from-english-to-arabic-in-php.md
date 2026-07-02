title: Convert numbers from English to Arabic in PHP
date: March 12th, 2021
slug: convert-numbers-from-english-to-arabic-in-php
category: PHP
status: active

If you're a developer working in the Middle East, it's quite common that you'll work on a project that bilingual, in our case, it's english and arabic.

In my opinion, it's not aesthetically pleasing and logical to have english numbers in arabic text, so, write a simple helper function to convert the numerals from english to arabic:

```php
<?php
function convertEnglishToArabicNumerals($str) {
    if (\App::getLocale() == 'ar') {
        $westernArabic = array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
        $easternArabic = array('٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩');
        $str = str_replace($westernArabic, $easternArabic, $str);
    }
    return $str;
}
?>
```

And since most browsers can handle RTL, you don't have to worry about how the arabic numerals are being displayed in your application.