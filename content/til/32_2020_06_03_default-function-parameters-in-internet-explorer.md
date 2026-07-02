title: Using default function parameters in Internet Explorer
date: June 3rd, 2020
slug: using-default-function-parameters-in-internet-explorer
category: JavaScript
status: active

Today, I wrote a simple method that fetches images from the database via AJAX and also, I defined an empty object as a default parameter:
```js
function fetchImages(obj={}){
    // some code here...
}

fetchImages();
```
The default `obj` parameter would contain extra parameters like `id`, `slug` and `page`, which would be then used to fetch a particular group of images, else, it'll fetch a random set of images.

This method worked fine in Google Chrome and Mozilla Firefox but not in Internet Explorer. I thought of inspecting the code and I was facing weird errors like `undefined` or `Expected: ')'` on the IE console.

Luckily, I had compared it to the other methods that didn't have any default parameters, so I did a little research and turns out that according to [Mozilla's documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/default_parameters), default function parameters are proposed by the ES6 syntax and at this point, I realized that Internet Explorer **doesn't support ES6 syntax**. What a bummer! &#x1F612;

However, there's a way to prevent this from happening by rewriting the method like this:
```js
function fetchImages(obj){
    // Check if obj is defined, else make it assign it as an empty object.
    var data = obj || {};

    // some code here...
}
```
And BAM! The method worked flawlessly just as it's intended to do so. &#x1F60E;

Addtionally, you may refer to the [ECMAScript 6 Compatibility table](http://kangax.github.io/compat-table/es6/) that you might find it quite helpful to check browser compatiblity for Internet Explorer versions 11 and under.
