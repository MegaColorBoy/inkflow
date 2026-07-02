title: Arcade Challenge 3: Pong
date: August 11th, 2017
slug: arcade-challenge-3-pong
category: Arcade Challenge
summary: This is the third article of the Arcade Challenge series. In this article, I'll be talking about Pong, it's history and game mechanics, in short.

<script defer type="text/javascript" src="/static/projects/pong/js/pong.js"></script>

<figure>
    <canvas style="border-radius: 0px;" id="pong_canvas" width="500" height="500"></canvas>
</figure>

Before you read more about this article, play with the above game. The rules are simple, control the paddle using <kbd>W</kbd> and <kbd>S</kbd> keys.

This is part of the [Arcade Challenge](/posts/i-challenged-myself-to-build-4-arcade-games/) series. If you haven't read the previous articles, here you go:

+ [Snake Game](/posts/arcade-challenge-1-snake-game/)
+ [Breakout](/posts/arcade-challenge-2-breakout/)

## Background
It's a 2D [table tennis](https://en.wikipedia.org/wiki/Table_tennis) simulation game. The player controls a paddle that moves vertically up and down on the side of the screen and can compete against AI or a second player, who controls the second paddle on the opposite side. The aim of the game is to hit the ball back and forth and reach 11 points before the opponent (although, I didn't build a scoring system for my implementation as I felt it wasn't necessary).

## History
Pong is one of the most popular and commercially successful arcade game built by ***Atari, Inc*** in 1972. It was the company's first game and was created by [Allan Alcorn](https://en.wikipedia.org/wiki/Allan_Alcorn), who got it as a warm-up exercise from the founder of the company, [Nolan Bushnell](https://en.wikipedia.org/wiki/Nolan_Bushnell).

## Game mechanics
There are two important mechanics that made it challenging to build this game:

+ [Game AI](#gameai)
+ [Ball Collision](#ballcollision)

## <a id="gameai"></a> Game AI
While I was building Pong, I thought of making it a 2 player game but later I decided to build a simple AI to make things interesting. Building the AI logic for this was simple, ***"When the player paddle hits the ball, the AI should try it's best to position itself by tracking the ball's destination to hit the it's center"***.

**Code snippet of the AI object:**
```js
var ai = {
    x: null,
    y: null,
    width: 10,
    height:100,

    //Update the AI paddle position based on the ball's direction
    update: function(){
        var dest_y = ball.y - (this.height - ball.side) * 0.5;
        this.y += (dest_y - this.y) * 0.1;
        this.y = Math.max(Math.min(this.y, height-this.height), 0);
    },
    draw: function(){
        ctx.fillRect(this.x, this.y, this.width, this.height);
    }
};  
```

## Ball Collision
In this game, the collision works a little different than [Breakout](#)'s version. I came across an algorithm called [Axis Aligned Bounding Box](https://en.wikipedia.org/wiki/Minimum_bounding_box#Axis-aligned_minimum_bounding_box), which is one of the simpler forms of detecting a collision between a set of objects that are axis aligned that means no rotation. This algorithm also inspired me to use it in my next game, Tetris. 

**Code snippet of the Axis Aligned Bounding Boxes collision:**

```js
//AABB Collision function
var AABBCollision = function(px, py, pw, ph, bx, by, bw, bh)
{
    return px < bx+bw && py < by+bh && bx < px+pw && by < py+ph;
}

//if the ball has -ve velocity, it's hit by AI paddle and it's the player's turn
//if the ball has +ve velocity, it's hit by player paddle and it's the AI's turn
var paddle = this.velocity.x < 0 ? player : ai;

if(AABBCollision(paddle.x, paddle.y, paddle.width, paddle.height, this.x, this.y, this.side, this.side))
{
    this.x = (paddle == player ? player.x+player.width : ai.x - this.side);
    var n = (this.y+this.side - paddle.y)/(paddle.height+this.side);
    var phi = 0.25 * pi * (2 * n - 1);
    var dir = (paddle == player ? 1 : -1);

    var impact = Math.abs(phi) > 0.2 * pi ? 1.5 : 1;

    this.velocity.x = impact * dir * this.speed * Math.cos(phi);
    this.velocity.y = impact * this.speed * Math.sin(phi);
}
```

The game was built using HTML5 Canvas and Javascript, so please feel free to read the source code to understand the logic of the game.

## What's next?
Building this game was fun as I built a simple AI and implemented a better collision detection algorithm. In my first post of this series, I had mentioned that I was working on Tetris and honestly, I finished building that game today as I didn't find the time to work on it. Now that it's ready, hence, my next post will be about ***Tetris***. 

Stay Tuned! 

## References
+ [Pong (1972)](https://en.wikipedia.org/wiki/Pong)
+ [Axis Aligned Bounding Collision](https://en.wikipedia.org/wiki/Minimum_bounding_box#Axis-aligned_minimum_bounding_box)
+ [Allan Alcorn](https://en.wikipedia.org/wiki/Allan_Alcorn)