title: Select all elements except the current element
date: May 28th, 2020
slug: select-all-elements-except-the-current-element
category: jQuery

If you don't want the current element to be selected in an array of elements that belongs to same class or type, just use the `.not()` method like the example below:

```js
$(".btn").click(function(){
    $(".btn").not(this).text('selected');
});
```
The above code will change the text for all buttons except the current element.
