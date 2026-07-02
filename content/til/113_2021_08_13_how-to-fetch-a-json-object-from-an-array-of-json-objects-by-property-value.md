title: How to fetch a JSON object from an array of JSON objects by property value?
date: August 13th, 2021
slug: how-to-fetch-a-json-object-from-an-array-of-json-objects-by-property-value
category: JavaScript
status: active

Say, for example, you have an array of JSON objects that contains the following data:
```js
var arrOfObjects = [
	{
		name: "John Doe",
		age: 20,
		email: "john.doe@email.com"
	},
	{
		name: "Bob Smith",
		age: 56,
		email: "bob.smith@email.com"
	},
];
```

Hmm, that's pretty basic but how will get the information of "Bob Smith" using his email? Well, that's where the `Array.find()` method comes into the picture.

Try reading the [Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) on `Array.prototype.find()` and implement the following:
```js
var key = "email";
var valueToFind = "bob.smith@email.com";
var result = arrOfObjects.find(obj =&gt; {
    return obj[key] == value;
});

//This should give you the record of Bob Smith.
console.log(result) 
```

This works fine on all browsers except **Internet Explorer** (I mean, it sucks anyways!), which is okay!

Hope you found this useful!