title: Arcade Challenge 1: Snake Game
date: July 14th, 2017
slug: arcade-challenge-1-snake-game
category: Arcade Challenge
summary: This is the first post of this month's personal challenge. I'll be talking about Snake Game, it's history and game mechanics, in short.

<script defer type="text/javascript" src="/static/projects/snake/js/snake.js"></script>

<figure>
    <canvas style="border-radius: 5px;" id="snake_canvas" width="500" height="500"></canvas>
</figure>

Before you read more about this article, play with the above game. You can control the snake using <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> or the <kbd>&larr;</kbd> <kbd>&uarr;</kbd> <kbd>&darr;</kbd> <kbd>&rarr;</kbd> keys. Orange block is for food, it'll increase your score. Yellow block is for poison, if eaten, it'll reduce your score. Press <kbd>Space</kbd> to pause the game. Press <kbd>P</kbd> to resume and <kbd>R</kbd> to restart the game. Oh and avoid hitting the white walls!

## Background
Snake is a game of simple concept where the player manuevers the snake in all 4 straight directions (reverse movement is not possible i.e. UP, DOWN, LEFT, RIGHT only) to eat the fruit and as a result, the length of the snake increases, making the game difficult for the player. The player will have to prevent the snake to hit the walls or from eating the poison, which will decrease the snake's length, and also prevent it from hitting itself.

## History
I remember playing this game, for the first time, on my father's monochrome ***Nokia 3310*** mobile phone (which can still break walls, I guess!) and every 90's kid I knew played this game a lot.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Nokia_3310_blue.jpg/320px-Nokia_3310_blue.jpg"/>
    <figcaption>Nokia 3310 (in case, if you've never heard about it!)</figcaption>
</figure>

The game was published by ***Nokia*** and it was programmed by a Nokia Design Engineer named Taneli Armanto in 1997 for ***Nokia 6110***. The original concept of this game was derived from an arcade game called [Blockade](https://en.wikipedia.org/wiki/Blockade_(video_game)), which was published in 1976 by ***Gremlin Industries***. Ever since, there have been so many variations and clones of this game, in fact, there are over 300+ variations of this game for iOS devices alone.

## Game mechanics
The game makes use of [Linked Lists](https://en.wikipedia.org/wiki/Linked_list), which is a simple and dynamic data structure used to store and control the movement of the snake. Below is the pseudocode for each of the game's behaviour:

**Movement of the Snake:**

```text
for node in the list (always starts from the end of the list):
    if node is not equal to head node:
        shift the snake's position to node+1 (by making it closer to the snake)
    set head node to new position
endfor
```

**Length of the Snake:**

```text
nx: current x coordinate of the snake head
ny: current y coordinate of the snake head

fx: x coordinate of the food
fy: y coordinate of the food

px: x coordinate of the poison
py: y coordinate of the poison

if [nx] matches with [fx] and if [ny] matches with [fy]:
    push the new cell to the snake's tail node
    shift the new cell from tail node to the head node
    increment score + 1

if [nx] matches with [px] and if [ny] matches with [py]:
    pop the cell from the tail node
    shift cell from tail node to head node
    decrement life - 1
```

**Collision of the Snake:**

```text
nx: current x coordinate of the snake head
ny: current y coordinate of the snake head

sx: x coordinate of the snake cell
sy: y coordinate of the snake cell

wx: x coordinate of the wall cell
wy: y coordinate of the wall cell

for cell in the wall array:
    if [nx] matches with [wx] and if [ny] matches with [wy]:
        display "game over" message

for cell in the snake list:
    if [nx] matches with [sx] and if [ny] matches with [sy]:
        display "game over" message
```

Oh yeah, please feel free to study the source code of this game in order to understand how this game was implemented on Javascript.

## What's next?
In my next post, I'll be talking about, the second game that I built in this challenge, ***Breakout***. I hope you've found this article interactive and interesting and yes, have fun playing this game! 

Adios Amigo!

## References
+ [Snake](https://en.wikipedia.org/wiki/Snake_(video_game))
+ [Nokia 3310](https://en.wikipedia.org/wiki/Nokia_3310)
+ [Blockade (1976)](https://en.wikipedia.org/wiki/Blockade_(video_game))
+ [Linked List](https://en.wikipedia.org/wiki/Linked_list)
