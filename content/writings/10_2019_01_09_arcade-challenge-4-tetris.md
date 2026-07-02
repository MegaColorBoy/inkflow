title: Arcade Challenge 4: Tetris
date: August 12th, 2017
slug: arcade-challenge-4-tetris
category: Arcade Challenge
summary: This is the fourth article of the Arcade Challenge series. In this article, I'll be talking about Tetris, it's history and game mechanics, in short.

<script defer type="text/javascript" src="/static/projects/tetris/js/tetris.js"></script>
<script defer type="text/javascript" src="/static/projects/tetris/js/render.js"></script>
<script defer type="text/javascript" src="/static/projects/tetris/js/controller.js"></script>

<figure>
	<canvas style="border-radius: 0px;background-color:#333;" id="tetris_canvas" width="300" height="600"></canvas>
</figure>

Before you read more about this article, play with the above game. It's simple, control each block using ***WASD*** keys to rotate and move the block to the left, right and down of the canvas.

This is part of the [Arcade Challenge](/posts/i-challenged-myself-to-build-4-arcade-games) series. If you haven't read the previous articles, here you go:

+ [Snake Game](/posts/arcade-challenge-1-snake-game/)
+ [Breakout](/posts/arcade-challenge-2-breakout/)
+ [Pong](/posts/arcade-challenge-3-pong/)

## Background
Tetris is a tile-matching puzzle game in which you have shapes called "Tetrominoes" (I'll be talking about it more in detail below.) falling down vertically from above into a matrix or "the well". The game's objective is to set a high score by manipulating the seven shapes (but I didn't set a scoring system for this implementation) by moving left, right, down or rotating the shape by 90 degree units. As the game progresses, the tetrominoes would fall faster in every level, thus, making it challenging to play.

## History
In 1984, the game was invented, designed and programmed by an AI researcher named [Alexey Pajitnov](https://en.wikipedia.org/wiki/Alexey_Pajitnov), who at the time worked for the ***Soviet Academy of Sciences*** in Moscow.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/en/8/8d/NES_Tetris_Box_Front.jpg"/>
    <figcaption>Tetris cover art</figcaption>
</figure>

Alexey Pajitnov was inspired by the classic Roman puzzle game called [Pentomino](https://en.wikipedia.org/wiki/Pentomino). In 1985, the game was published for various game consoles.

## Game mechanics
This game has quite some interesting mechanics, for those who don't know, here it is:

+ [Generating Shapes](#generating-shapes)
+ [Collision](#collision)
+ [Freeze the Line](#freeze-the-line)
+ [Rotating Shapes](#rotating-shapes)
+ [Clearing the Line](#clearing-the-line)

### <a id="generating-shapes"></a> Generating Shapes
These shapes are called ***"tetrominoes"*** i.e. a unique arrangement of 4 cells in a 4x4 grid. Mathematically, it is proven that there can only be seven tetrominoes on a ***two-dimensional space***, which also means seven different ways to arrange 4 cells.

<figure>
    <img src="http://oopsilon.com/06/texts/tetris-shapes.gif"/>
    <figcaption>The Seven Tetrominoes</figcaption>
</figure>

I'm sure a lot of you know that Javascript doesn't have a special way of creating multi-dimensional arrays. So in order to draw a random shape, I had to convert a two-dimensional array index to a one-dimensional array index to fill each cell i.e. if it was a '1', it would be filled with color and if it's a '0', it would be empty.

```js
//Generate new random shape
function newShape()
{
    current = [];

    var rand = Math.floor(Math.random() * shapes.length);
    var shape = shapes[rand];

    for(var y=0; y<4; y++)
    {
        current[y] = [];
        for(var x=0; x<4; x++)
        {
            //convert 2D index to 1D index
            var i = 4 * y + x;
            if(shape[i])
            {
                current[y][x] = rand + 1;
            }
            else
            {
                current[y][x] = 0;
            }
        }
    }

    currentX = 5;
    currentY = 0;
}
```

### <a id="collision"></a> Collision
As I had mentioned in my [previous post](/posts/arcade-challenge-3-pong/), I was inspired to use the [AABB collision](https://en.wikipedia.org/wiki/Minimum_bounding_box#Axis-aligned_minimum_bounding_box) algorithm to prevent the tetrominoes from going away from the canvas. Well, we all know that simple physics says that if an object is dropped from above, it should break the ones below but in this case, that doesn't happen. Instead, the tetrominoes are stacked on top of each other, which unlike real gravity, that contributes to the actual gameplay.

```js
//Check if this shape's position is valid in the board
function isValid(offsetX, offsetY, newCurrent)
{
    //if offsetX is not set, set it to 0
    offsetX = offsetX || 0;
    //if offsetY is not set, set it to 0
    offsetY = offsetY || 0;

    offsetX = currentX + offsetX;
    offsetY = currentY + offsetY;

    newCurrent = newCurrent || current;

    for(var y=0; y<4; y++)
    {
        for(var x=0; x<4; x++)
        {
            if(newCurrent[y][x])
            {
                if(typeof board[y + offsetY] == 'undefined' ||
                typeof board[y + offsetY][x + offsetX] == 'undefined' ||
                board[y + offsetY][x + offsetX] ||
                x + offsetX < 0 ||
                y + offsetY >= rows ||
                x + offsetX >= cols)
                {
                    if(offsetY == 1){lose = true;}
                    return false;
                }
            }
        }
    }
    return true;
} 
```

### <a id="freeze-the-line"></a> Freeze the Line
Honestly, I could have come up with a better name but the method freeze() stops the shape at it's current position (i.e. after a collision has occurred) and saves it to the 2D canvas.

```js
function freeze()
{
    for(var y=0; y<4; y++)
    {
        for(var x=0; x<4; x++)
        {
            if(current[y][x])
            {
                board[y+currentY][x+currentX] = current[y][x];
            }
        }
    }
}
```

### <a id="rotating-shapes"></a> Rotating Shapes
In order to rotate a shape perpendicularly anticlockwise, you have to perform an operation that flips the indices from bottom to top of the matrix, this operation is called [Matrix Transpose](https://en.wikipedia.org/wiki/Transpose). Although I learnt this in my math classes, I implemented this operation in a Computer Graphics course that I took, as an elective, in my university on Spring 2016 for the first time.

```js
//Rotate the current moving shape
function rotate(current)
{
    var newCurrent = [];
    for(var y=0; y<4; y++)
    {
        newCurrent[y] = [];
        for(var x=0; x<4; x++)
        {
            newCurrent[y][x] = current[3-x][y];
        }
    }
    return newCurrent;
}
```

### <a id="clearing-the-line"></a> Clearing the Line
At every update, the method named ***clearLines()*** has to scan for any complete row(s), if it's complete, the cells in those rows must be replaced with the ones above it. This gives a sort of ***"falling gravity"*** effect, when the remaining cells are replaced with the row that has been cleared.

```js
function clearLines()
{
    //Bottom up approach
    for(var y = rows - 1; y>=0; y--)
    {
        var isComplete = true;
        for(var x=0; x < cols; x++)
        {
            //if there's any empty cell in the row
            if(board[y][x] == 0)
            {
                //Then the row isn't complete
                isComplete = false;
                break;
            }
        }

        //This code is to remove the current completed line,
        //and replace it with the line above it.
        if(isComplete)
        {
            for(var i=y; i>0; i--)
            {
                for(var j=0; j < cols; j++)
                {
                    board[i][j] = board[i-1][j];
                }
            }
            y++;
        }
    }
}
```

The game was built using HTML5 Canvas and Javascript, so please feel free to read the source code to understand the logic of the game. 

## What's next?
I know that in my [first post](/posts/i-challenged-myself-to-build-4-arcade-games/), I had mentioned that I'll do this whole challenge for a month but then I wasn't able to do everything in a month. So, I decided that I will be trying my best to remake more arcade games in the future and keep posting them on this blog. Hope you guys liked reading these articles!

Sayonara!

## References
+ [Tetris (1984)](https://en.wikipedia.org/wiki/Tetris)
+ [Alexey Pajitnov](https://en.wikipedia.org/wiki/Alexey_Pajitnov)
+ [Matrix Transpose](https://en.wikipedia.org/wiki/Transpose)
+ [Axis Aligned Bounding Collision](https://en.wikipedia.org/wiki/Minimum_bounding_box#Axis-aligned_minimum_bounding_box)