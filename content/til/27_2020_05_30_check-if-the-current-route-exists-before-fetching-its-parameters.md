title: Check if the current route exists before fetching it's parameters
date: May 30th, 2020
slug: check-if-the-current-route-exists-before-fetching-its-parameters
category: Laravel
status: active

If you've ever come across this type of error when you're trying to fetch parameters of the current route:
```text
Symfony\Component\Debug\Exception\FatalThrowableError: Call to member function parameters() on null
```

It's probably because the route doesn't exist, which is why it failed to call the `parameters()` function. It can be easily resolved by checking if the route exists before calling the function:
```php
<?php
namespace App\Http\Controllers;
use Route;

class FooController extends Controller {
    public function __construct(Request $request){
        // insert code here...
    }
    
    public function foo(Request $request){
        $params = $request->route() ? Route::current()->parameters() : '';
        return $params;
    }
}
?>
```
Although, the sample code above is to fetch parameters of the current route, you can apply this before calling any method from the `Route` class.

This works for version 5.2 and above.