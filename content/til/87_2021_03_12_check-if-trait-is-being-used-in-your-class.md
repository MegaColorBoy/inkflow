title: Check if trait is being used in your class
date: March 12th, 2021
slug: check-if-trait-is-being-used-in-your-class
category: PHP
status: active

Want to know if a trait is being used in your current class? Try this:
```php
<?php
in_array(Foo::class, class_uses($this))
?>
```

By any chance, if the current class is inherited, please note that the `class_uses()` method will only return the list of traits used by the current class and won't include any traits of it's parent class.