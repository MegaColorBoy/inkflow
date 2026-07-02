title: Looping infinitely around an array
date: July 4th, 2020
slug: looping-infinitely-around-an-array
category: Algorithms
status: active

Sometimes, I find myself in a situation where I might have a fixed array of colors, text, numbers or something like that but I want to loop around infinitely like a carousel.

Let's say we have an array like this:
```js
var colors = ["#111", "#222", "#333"];
```
The code is an array of three colors that we want to apply to, hmmm, say a list of HTML DOM elements like `<div>` containers or any element that you prefer. In this example, we'll add some colors to a bunch of `<div>` elements that has the classname `.card` or we'll just call them "cards".

## Behold, the Modulus operator!
You may think of writing different conditions or loops to achieve a solution but a more elegant one is by using the Modulus operator a.k.a the Remainder operator (`%`). Using this operator gives you the remainder after the division of a number.

Hmm, confused? Okay, here's a simple example of how a Modulus operator would be like:

> In plain english, if you have 10 apples and you divide them by 4 and by doing so, you'll end up with 2 sets of 4 apples and the remaining set would be 2 apples. Thus, the remainder is 2.

Did that make sense? If not, then try the following code in your browser:

```js
var x = 10 % 4;
console.log(x); // output will be 2
```

Let's say we have 10 "cards" and we want every 3 three cards to have 3 different colors, we must just define a way to determine the index of each color while iterating through a loop of cards. So, we can easily get the index by doing so:
```js
var currentColor = colors[i % colors.length-1];
```

Here's the full code:
```js
var elements = document.querySelectorAll('.card');
for(var i=0; i&lt;elements.length; i++){
    var currentColor = colors[i % colors.length-1];
    elements[i].style.backgroundColor = currentColor;
}
```

The following code will apply the colors to each "card" with respect to it's order and will reset back to the first color once it's reached it's last color based on the remainder of the next iteration in the loop.

Read about [Modulus Operation](https://en.wikipedia.org/wiki/Modulo_operation) to know more about it.
