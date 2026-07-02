title: Built a 2048 clone in 15 minutes
date: August 21st, 2018
slug: built-a-2048-clone-in-15-minutes
category: Personal Challenge
summary: An implementation of the famous 2048 game using JavaScript and HTML5 Canvas.

<script defer src="/static/projects/2048/script.js"></script>

<figure>
    <canvas id="game-grid" width="500" height="500"></canvas>
</figure>

Before you read more about this article, play with the above game. You
can move the tiles around using your <kbd>&uarr;</kbd><kbd>&larr;</kbd><kbd>&darr;</kbd><kbd>&rarr;</kbd>
or <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> keys. The rule is simple, when two tiles with the same
number touch, they merge into one tile. Press the <kbd>R</kbd> key to restart
the game.

Please make sure that you have JavaScript enabled and running in your
browser, otherwise you won't be able to play this game. Oh, just a
little heads up, it might get a little buggy and freeze your browser
window, so keep calm and play patiently.

As for the source code, you can view it in my [GitHub
repository](https://www.github.com/megacolorboy) or can be found near
the end of this article.

## Background

I was always fond of puzzle games and **2048** is one of them. The first
time I got to play this game was back in 2014 and I would play it on my
iPhone during my train commute to university.

Yesterday, I thought of building a clone and turns out it wasn't as hard
as I had expected it to be, in fact, I was able to build a functional
version in just 15 minutes.

## What are the game mechanics?

The sliding-puzzle game is played on a **four-by-four** grid with
numbered tiles that is moved by the player in all four directions.

In every move, a new tile would randomly appear in an empty spot in the
grid with a value that consists of **2** or **4**. These tiles are moved
towards any direction as far as it could and if there are two tiles that
collide with the same value, they merge into one tile and as a result,
the score is updated.

The player wins the game once the tile of **2048** appears on the grid,
thus is the name of the game.

## Source code

<script src="https://gist.github.com/MegaColorBoy/fcce2a2029a1b0352884cbbc1f059cb1.js"></script>

Well then, that's all for the game. Just like the previous ones, I had
fun building this sliding-puzzle game. I'm looking forward to building
more puzzle games and talking about them in my blog.

Hope you guys liked reading this article and have fun playing the game
as many times as you like!

Stay tuned for more!