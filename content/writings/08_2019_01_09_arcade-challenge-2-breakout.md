title: Arcade Challenge 2: Breakout
date: July 22nd, 2017
slug: arcade-challenge-2-breakout
category: Arcade Challenge
summary: This is the second post of this month's personal challenge. I'll be talking about Breakout, it's history and game mechanics, in short.

<script defer type="text/javascript" src="/static/projects/breakout/js/breakout.js"></script>
<script defer type="text/javascript" src="/static/projects/breakout/js/ball_collision.js"></script>

<figure>
    <canvas style="border-radius: 0px;" id="breakout_canvas" width="500" height="500"></canvas>
</figure>

Before you read more about this article, play with the above game. You can control the paddle using the mouse or left-right arrow keys. Press <kbd>P</kbd> to pause the game. Press <kbd>S</kbd> to resume and <kbd>R</kbd> to restart the game.

This is part of the [Arcade Challenge](/posts/i-challenged-myself-to-build-4-arcade-games/) series. In the previous post, I built a snake game, [click here](/posts/arcade-challenge-1-snake-game/) if you've not read the article.

## Background
Breakout is a single player game where you have to break a layer of bricks with a ball that travels across the screen (in this case, it's a canvas) that bounces off the walls of the screen. When the ball hits a brick, the ball bounces back and of course, the brick gets destroyed or disappears. If the ball touches the bottom of the screen, the game is over. In order to prevent this from happening, the player is given a movable paddle to bounce the ball upwards, which ensures the game continues.

## History
Breakout was one of the most popular arcade games developed by ***Atari, Inc.*** Inspired by the 1972's Pong, the game was developed and designed by [Nolan Bushnell](https://en.wikipedia.org/wiki/Nolan_Bushnell), [Steve Wozniak](https://en.wikipedia.org/wiki/Steve_Wozniak), Steve Bristow using the hardware built for Pong against it's competitors who built clones of Pong.

<figure>
    <img src="http://68.media.tumblr.com/15f5cfe691599a10ad9ca9cf33f89ff9/tumblr_ntykhyjQXI1qjotzlo1_1280.jpg"/>
    <figcaption>Atari's Video Pinball console system</figcaption>
</figure>

Most notably, the late ***Steve Jobs*** was also involved with the development of Breakout as he was approached by Nolan Bushnell to design a prototype that required 150 to 170 computer chips. Jobs brought in Wozniak to work with along with him on building the prototype, who built a version of Pong using 30 computer chips and they both had spent days and nights working on it and finally built the prototype that had 44 computer chips.

However, Wozniak's design wasn't approved by Atari, Inc as they found the design to be complicated and infeasible to manufacture, so they ended up making their own version of the hardware which contained around 100 computer chips.

## Game mechanics
Unlike the previous post, the game mechanics of this game are quite simple to understand and it makes use of [2D Mathematics](https://en.wikipedia.org/wiki/Two-dimensional_space).

Using 2D Mathematics, I was able to program the ball-brick collision, movement and bounciness of the ball and the movement of the paddle (which can only move on the x-axis).

### Collision Detection
To check for ball collision, the program must check if the ball has touched / collided with the wall, if so, then the ball's direction will be changed accordingly. The ball can only bounce off from the top, left and right side of the walls and the paddle, if it touches the bottom of the canvas, it's game over.

**Ball Movement and Collision Detection:**

If the distance between the ball radius and the wall's edge is the same, it will change the ball direction. This would allow a proper ball collision to bounce off the walls.

<figure>
    <canvas style="border-radius: 0px;" id="ball_collision_canvas" width="500" height="300"></canvas>
</figure>

**Code for Ball Movement and Collision Detection:**
```js
$(document).ready(function(){
    //Canvas stuff
    var canvas = document.getElementById("ball_collision_canvas");
    var height = canvas.height;
    var width = canvas.width;
    var ctx = canvas.getContext("2d");

    //coordinates of the ball
    var x = canvas.width / 2;
    var y = canvas.height - 30;
    var dir_x = 2;
    var dir_y = 4;
    var ball_r = 10;

    //Draw a circle
    function circle(x,y,r)
    {
        ctx.fillStyle = "#FF6D6D";
        ctx.beginPath();
        ctx.arc(x,y,r,0,Math.PI*2, true);
        ctx.closePath();
        ctx.fill();
    }

    //Draw canvas
    function draw()
    {
        ctx.clearRect(0, 0, width, height);
        circle(x,y,ball_r);

        /*
            If the distance between the ball radius and the wall's edge is the same,
            it will change the ball direction. This would allow a proper ball collision
            to bounce off the walls.
        */
        if(x + dir_x > width - ball_r || x + dir_x < ball_r)
        {
            dir_x = -dir_x;
        }
        
        if(y + dir_y > height - ball_r || y + dir_y < ball_r)
        {
            dir_y = -dir_y;
        }

        x += dir_x;
        y += dir_y;
    }

    setInterval(draw, 10);
});
```

The game was built using HTML5 Canvas and Javascript, so please feel free to read the source code to understand the logic of the game.

## What's next?
In my next post, I'll be talking about the third game that I built in this challenge, Pong. Well, that's it for today, hope you guys have found this post interesting and yes, have fun playing the game!

Peace Out!

## References
+ [Pong](https://en.wikipedia.org/wiki/Pong)
+ [2D Dimensional Space](https://en.wikipedia.org/wiki/Two-dimensional_space)
+ [Atari, Inc](https://en.wikipedia.org/wiki/Atari)