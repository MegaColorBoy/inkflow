title: Using IIFE in JavaScript
date: August 10th, 2022
slug: using-iife-in-javascript
category: JavaScript
status: active

IIFE a.k.a Immediately-Invoked Function Expression &mdash; is a way to execute functions as soon as the function is created.

Using IIFE, you can easily isolate declared variables away from the global scope.

This is how the syntax would look like:

```javascript
// ES5 Standard
let foo = (function(){
    let message = "Hello world"
    console.log(message);
})();
```

They can be defined with arrow functions as well:

```javascript
// ES6 Standard
let foo = (() => {
    let message = "Hello world"
    console.log(message);
})();
```

According to **MDN Docs**, it's a design pattern a.k.a Self-Executing Anonymous Function. There are two parts to this:

1. The function that's enclosed within the Grouping Operator `()`, which would prevent it from polluting the global space and access to the variables within it's scope.

2. The `();` will create the Immediately Invoked Function Expression on-the-fly.

## When to use it?

There are many interesting cases such as if you are following the [Module Pattern](https://www.patterns.dev/posts/classic-design-patterns/) especially if you want to avoid polluting the global namespace or just that you don't want your code to interfere with other code thus ensures code safety.

## Readings
- [IIFE - MDN Web Docs Glossary](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)