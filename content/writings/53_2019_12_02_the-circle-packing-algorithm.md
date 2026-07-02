title: The Circle Packing Algorithm
date: December 8th, 2019
slug: the-circle-packing-algorithm
category: Algorithms + Art
summary: Implemented a mathematically beautiful generative pattern that looks deceivingly complex to the human.

<iframe width="100%" height="485" src="/static/projects/circle-packing"></iframe>

Beautiful, isn't it? It might look complex but it's mathematically quite impressive. Making this pattern wasn't hard but it definitely took a lot of trial and error to get it right and honestly, I don't really know if it's this is the most efficient way to generate this pattern.

This article isn't a tutorial but rather, I'll be talking about the algorithm itself. However, you can check out the source code in my [GitHub repository](https://github.com/megacolorboy/BlogProjects).

## How it works?
In order to achieve that "stacked" effect, there are two things to keep in mind:

1. Generate circles with a random radius
2. Look for collisions with other circles

The logic is quite similar to the [Overlapping Rectangles](https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other) problem except this is done with circles.

## Generate circles with dynamic radius
This method will help generate valid circles with a random radius. Circles that don't overlap or collide with other circles are considered to be valid.
```js
// Generate a valid circle
const generateCircle = () => {
    let newCircle;
    let isValidCircle = false;

    for(let i=0; i<attempts; i++) {
        newCircle = {
            x: Math.floor(Math.random() * width),
            y: Math.floor(Math.random() * width),
            radius: minRadius
        };

        if(checkForCollision(newCircle)) {
            continue;
        }
        else {
            isValidCircle = true;
            break;
        }
    }

    if(!isValidCircle) { return; }

    for(let i=minRadius; i<=maxRadius; i++) {
        newCircle.radius = i;
        if(checkForCollision(newCircle)) {
            newCircle.radius--;
            break;
        }
    }

    circles.push(newCircle);
    drawCircleOnCanvas(context, newCircle, colors[Math.floor(Math.random() * colors.length)]);
}
```

## Look for collision with other circles
Thanks to some online research, I was able implement the [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) equation that helped with calculating the distances between each circle and detect for collisions. Along with that, I also found another article on [Touching Circles](http://www.mathsmutt.co.uk/files/tcirc.htm) that was quite useful.

These are the formulas used to detect the collision:

1. Find the distance between two centres
\\[ AB = \sqrt{ (x2 - x1)^2 - (y2 - y1)^2} \\]

2. Calculate the radii of both circles.
\\[R = r1 + r2\\]

If the radii is greater than or equal to the euclidean distance of both circles, then it's a valid circle with no collisions.

```js
// Check for collision in a canvas
const checkForCollision = (newCircle) => {
    
    let x2 = newCircle.x;
    let y2 = newCircle.y;
    let r2 = newCircle.radius;

    
    // Determine the euclidean distance between two circle
    // using Pythagorean Theorem.

    // Refer to: 
    // https://en.wikipedia.org/wiki/Euclidean_distance

    for(let i=0; i<circles.length; i++) {

        let otherCircle = circles[i];
        let r1 = otherCircle.radius;
        let x1 = otherCircle.x;
        let y1 = otherCircle.y;
        let xx = ((x2 - x1) * (x2 - x1));
        let yy = ((y2 - y1) * (y2 - y1));
        let radii = r2 + r1;
        let euclidDistance = Math.sqrt(xx + yy);

        if(radii >= euclidDistance) {
            return true;
        }
    }

    // Check collision on top
    if(x2 + r2 >= width || 
        x2 - r2 <= 0) {
        return true;
    }

    // Check collision on bottom
    if(y2 + r2 >= width || 
        y2 - r2 <= 0) {
        return true;
    }

    //else return false
    return false;
}
```

## Conclusion
I'm thinking of implementing more generative patterns like [Triangular Mesh](https://en.wikipedia.org/wiki/Triangle_mesh) and Piet Mondrian's [Red, Blue and Yellow composition](https://en.wikipedia.org/wiki/Composition_with_Red_Blue_and_Yellow).

Hope you liked reading this article.

Stay tuned for more!