title: Find the number of uppercase and lowercase letters in a string
date: July 18th, 2020
slug: find-the-number-of-uppercase-and-lowercase-letters-in-a-string
category: Regular Expressions
status: active

The usual approach of counting the number of uppercase and lower letters in a string is done by using a counter and a loop:
```js
var upperCount = 0;
var lowerCount = 0;
var str = "AbCdEfGhiJkL";
for(var i=0; i&lt;str.length; i++){
    if(str[i] == str[i].toUpperCase()){
        upperCount++;
    }
    else{
        lowerCount++;
    }
}
```

That's nice but here's shorter and faster implementation:
```js
var str = "AbCdEfGhiJkL";
var lowerCount = str.length - str.replace(/[A-Z]/g, '').length;
var upperCount = str.length - str.replace(/[a-z]/g, '').length;
```

The `lowerCount` variable is taking the difference of the lengths between the original string and the string with lowercase letters only because the `.replace()` method replaced the pattern of uppercase letters `[A-Z]` with empty spaces. The `upperCount` variable does the opposite of what the `lowerCount` variable does.

Hope you found this trick useful!