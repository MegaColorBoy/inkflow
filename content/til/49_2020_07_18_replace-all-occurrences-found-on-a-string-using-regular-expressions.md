title: Replace all occurrences found on a string using Regular Expressions
date: July 18th, 2020
slug: replace-all-occurrences-found-on-a-string-using-regular-expressions
category: Regular Expressions
status: active

Let's say you have the following string and you must replace all occurrences of **"Hello"** with **"Bye"**:
```js
var str = "Hello Hello Hello World";
```

You may think of using the `.replace()` method to solve this problem:
```js
var newStr = str.replace("Hello", "Bye")
```

But unfortunately, it only replaces the first occurrence in the string:
```js
console.log(newStr); // returns "Bye Hello Hello World" as the output.
```

Using the power of Regular Expressions, you can replace all occurrences in one go:
```js
function replaceAll(str, search, replace){
    var re = new RegExp(search, "g");
    return str.replace(re, replace);
}    
```

Now, when you execute the following, you'll get a string that replaced all occurrences:
```js
var newStr = replaceAll(str, "Hello", "Bye");
console.log(newStr); // returns "Bye Bye Bye World" as the output.
```

Until next time, then!