title: Make your own generative pixel art in less than 100 lines of code
date: March 5th, 2021
slug: make-your-own-generative-pixel-art-in-less-than-100-lines-of-code
category: Generative Art + JavaScript
summary: By modifying my old random pixel generator, I was able to generate a Space Invaders-esque pixel art.
status: active

<canvas id="myCanvas" width="500" height="302" style="border:0px solid #40514e;background-color: #e4f9f5;"></canvas>
<script defer type="text/javascript" src="/static/projects/invaders-sprites/script.js"></script>

<div class="post-notification success">
    <h3>Try it out!</h3>
    <p>Refresh the page to generate unique Space Invader-esque patterns as the results are unpredictable!</p>
</div>

Generative art is a topic that still fascinates me because of the fact that you can produce something unique by just writing few (sometimes, more) lines of code. Especially, if it's self-generating art that makes use of fixed rules and a slight dash of randomness to produce unique results.

When it comes to writing code, it's quite straightforward. You come up with the rules and constraints and voila, you have something that works. Having said that, setting up rules for generative art can get quite tricky.

You might have read about my previous post about [The Game of Life](/writings/posts/the-game-of-life/), it contains only four rules and each of them took a part in evolving the system through each generation. With generative systems like that, you can never predict the results as complex patterns will emerge due to it's randomness.

In my view, a combination of predictability and randomness is needed in order to create a good looking generative art.

## Why you should explore it?
There could be many reasons, maybe you're bored, curious or passionate to learn something new. Who knows? Open up your editor and try it for yourself.

Exploring the craft of making generative art has allowed me to:

- Gain different experiences &mdash; It allows you to sharpen your algorithms & data structures and maybe even, learn a new technique.
- Create something visually appealing &mdash; A picture is equal to a thousand words.
- Instant results that makes you feel good &mdash; I mean, it's hard to explain but y'know what I mean, right?

## Where to start?
Just like any other project, you just need:

- An inspiration or an idea that you can work on.
- The right kind of technology to use.

With today's article, I'll be showing you how I built a Space Invader-esque pixel art generator in JavaScript that makes use of the Canvas API.

## Building a generator
I'd like to give a shout out to the [person](https://www.erdavids.com/) who built a twitterbot that generates random sprites using Python's Pillow image library.

I was inspired and I thought of writing it in JavaScript and as you can see above, it did turn out pretty well.

Here's the code for your reference and please read the comments to know how it functions:
```javascript
// To store any used colors
var colorStack = [];

// Selected color palette
var colors = [
    '#30e3ca',
    '#ff5a5f',
    '#40514e',
    '#e4f9f5',
    '#40514e',
    '#e4f9f5',
    '#e4f9f5',
];

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext('2d');

var width = canvas.width;
var height = canvas.height;

function createSquare(squareDimensions, color, element, spriteDim) {
    const {squareX, squareY, squareWidth, squareHeight} = squareDimensions;

    // If it's a middle element, apply a color
    if (element == parseInt(spriteDim/2)) {
        ctx.fillStyle = color;
        ctx.fillRect(parseInt(squareX), parseInt(squareY), parseInt(squareWidth/squareX)+3, parseInt(squareHeight/squareY)+3);
    }
    // If it's the last element, then use the color that you saved previously
    else if (colorStack.length == element + 1) {
        ctx.fillStyle = colorStack.pop();
        ctx.fillRect(parseInt(squareX), parseInt(squareY), parseInt(squareWidth/squareX)+3, parseInt(squareHeight/squareY)+3);  
    }
    // Else, apply a color and save this for the last element.
    else {
        colorStack.push(color);
        ctx.fillStyle = color;
        ctx.fillRect(parseInt(squareX), parseInt(squareY), parseInt(squareWidth/squareX)+3, parseInt(squareHeight/squareY)+3);      
    }
}

function createInvader(invaderDimensions, spriteDim) { 

    var {posX, posY, invaderWidth, invaderHeight} = invaderDimensions;
    var squareSize = (invaderWidth - posX) / spriteDim;

    var cellPosition = 1;
    var element = 0;

    for(var y=0; y<spriteDim; y++){
        // Starts from the left side of the grid.
        // Think of it as something like this:
        // [-3,-2,-1,0,1,2,3]
        cellPosition *= -1;

        // First element
        element = 0;

        for(var x=0; x<spriteDim; x++) {
            squareX = x * squareSize + posX;
            squareY = y * squareSize + posY;
            squareWidth = squareX + squareSize;
            squareHeight = squareY + squareSize;

            // Pick a random color from the color palette
            var color = colors[Math.floor(Math.random() * colors.length)];

            var squareDimensions = {
                'squareX': squareX+2,
                'squareY':squareY+2,
                'squareWidth':squareWidth,
                'squareHeight':squareHeight,
            };

            // Create a square with a color and desired dimensions.
            createSquare(squareDimensions, color, element, spriteDim);

             // If it's the middle element or the starting element, 
             // then shift it's position to the leftmost.
            if(element == parseInt(spriteDim/2) || element == 0) {
                cellPosition *= -1;
            }

            element += cellPosition;
        }
    }
}

function main() {
    var spriteDim = 7;
    var numberOfInvaders = 15;
    var invadersSize = parseInt(width / numberOfInvaders);
    var padding = parseInt(invadersSize / spriteDim);

    for(var x=0; x<numberOfInvaders; x++) {
        for(var y=0; y<numberOfInvaders; y++) {
            var posX = (x * invadersSize) + padding + 2;
            var posY = (y * invadersSize) + padding + 2;
            var invaderWidth = posX + invadersSize - (padding * 3);
            var invaderHeight = posY + invadersSize - (padding * 3);

            var invaderDimensions = {
                'posX': posX,
                'posY': posY,
                'invaderWidth': invaderWidth,
                'invaderHeight': invaderHeight
            };

            createInvader(invaderDimensions, spriteDim);
        }
    }   
}

main();
```

Well, I won't say that is a perfect solution but hey, it works and yes, it doesn't take a lot of code to achieve something like this.

## Explanation
I'll try my best to explain how this whole thing works.

First, you need to initialize a `<canvas>` DOM element of the desired width and height. Then in the `main()` function, you determine the size of each invader by specifying the number of invaders and dividing it with the width of the canvas. These values will then be used to determine the coordinates for each invader.

Second, the function `createInvader()` follows nearly the same process as the `main` function except that the coordinates for each pixel is determined by calculating the width of the invader and subtracting it's `x` position divided by the dimensions of each invader.

Third, as you can see in the function `createSquare()`, it contains 3 simple rules in which all of them draws a square with a color but with an emphasis that each invader has a symmetrical pattern.

The code looks deceptively simple but achieving this complexity did take a lot of trial and error and a little bit of simple calculus &#x1F602;.

## Conclusion
Generative art might be something that you may not need to explore but it's quite fun and you may never know what you might be able to produce by combining both code and visuals.

Hope you liked reading this article.

Stay tuned for more! &#x1F918;