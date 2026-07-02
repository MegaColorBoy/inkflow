title: The 15 Puzzle Game
date: June 22nd, 2019
slug: the-15-puzzle-game
category: Personal Challenge
summary: A classical numbered puzzle that requires the player to place all the tiles in an ordered sequence.

<iframe src="/static/projects/15-puzzle" width="500" height="500"></iframe>

Before you read this article, play with the above puzzle. You can move the block around by ***left-clicking*** on a numbered tile that's adjacent to the empty tile.

The source code for this puzzle can be found [over here](https://github.com/megacolorboy/BlogProjects/tree/master/15-puzzle).

## Background

This is a game that has been on my list of projects for a long time and I've finally decided to work on it last night. Although, this post has nothing to do with Artificial Intelligence, I was inspired to write this game when I studied about [Heuristics](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) in the book named [Artificial Intelligence: A Modern Approach](/posts/artificial-intelligence-a-modern-approach--chapter-1) and on how it was applied to this game.

## What are the game mechanics?

This game is played on a ***four-by-four*** grid with numbered tiles that are shuffled randomly. As you can see, there are ***15 numbered cells*** and ***1 empty cell*** in the grid, this is to allow movement of the tiles within the grid.

However, the movement is limited to the numbered tiles that are adjacent to the empty tile.

The player wins the game after ordering all the numbered tiles in the grid in an order of ascending sequence.

## Source code

Here's the source code of the entire game:

```js
var board = [], rows = 4, cols = 4;
var possibleMoves, zx, zy, oldzx = -1, oldzy = -1;

//Generate 2D Board
function generateBoard()
{
    for(var i=0; i&lt;rows; i++)
    {
        board[i] = [];
    }

    for(var j=0; j&lt;cols; j++)
    {
        for(var i=0; i&lt;rows; i++)
        {
            board[j][i] = (i + j * 4) + 1;
        }
    }

    //position of the empty cell in the grid i.e. 3,3
    zx = zy = 3;
    board[zx][zy] = 16;
}

//Generate the cells
function generateCells()
{
    var grid = document.createElement("div");
    grid.className += "board";

    document.body.appendChild(grid);

    for(var j=0; j&lt;4; j++)
    {
        for(var i=0; i&lt;4; i++)
        {
            var cell = document.createElement("div");
            cell.className += "cell";
            cell.id = "cell_" + (i + j * 4);
            cell.row = i;
            cell.col = j;
            cell.addEventListener("click", cellEventHandle, false);
            cell.appendChild(document.createTextNode(""));
            grid.appendChild(cell);
        }
    }
}

/*
    Determine the possible number of moves
    based on the empty cell's coordinates.
*/
function genPossibleMoves()
{
    possibleMoves = [];
    var ii, jj;
    
    /*
        Just for reference:
        The empty cell can be moved in the following x,y coords:
        -1,0, 0,-1, 1,0, 0,1
    */
    var xCoords = [-1, 0, 1, 0];
    var yCoords = [0, -1, 0, 1];

    for(var i=0; i&lt;4; i++)
    {
        ii = zx + xCoords[i];
        jj = zy + yCoords[i];

        //If it's out of bounds, skip it
        if(ii &lt; 0 || jj &lt; 0 || ii &gt; 3 || jj &gt; 3)
        {
            continue;
        }

        possibleMoves.push({x: ii, y: jj});
    }
}

function updateCells()
{
    for(var j=0; j&lt;cols; j++)
    {
        for(var i=0; i&lt;rows; i++)
        {
            var cell_id = "cell_" + (i + j * 4);
            var cell = document.getElementById(cell_id);
            var val = board[i][j];

            if(val &lt; 16)
            {
                cell.innerHTML = ("" + val);
                if(val % 2 == 0)
                {
                    cell.className = "cell dark";               
                }
                else
                {
                    cell.className = "cell light";
                }
            }
            else
            {
                cell.innerHTML = "";
                cell.className = "empty";
            }
        }
    }
}

//Event handler for each cell
function cellEventHandle(e)
{
    genPossibleMoves();

    //Current coords of the cell
    var r = e.target.row;
    var c = e.target.col;
    var pos = -1;
    var isPossible = false;
    // console.log(r + "," + c);

    /*
        Check if the current cell is 
        one of the possible moves
    */
    for(var i=0; i&lt;possibleMoves.length; i++)
    {
        if(possibleMoves[i].x == r && possibleMoves[i].y == c)
        {
            isPossible = true;
            pos = i;
            break;
        }
    }

    if(isPossible)
    {
        var temp = possibleMoves[pos];

        //Swap position of the empty cell
        board[zx][zy] = board[temp.x][temp.y];
        //Update the coordinates of the empty cell
        zx = temp.x;
        zy = temp.y;
        board[zx][zy] = 16;
        updateCells();

        //Check if the game is over
        if(is_game_over())
        {
            setTimeout(function(){
                alert("Congrats!");
            }, 2);
        }
    }

}

//Check if the game is over
function is_game_over()
{
    var currentVal = 0;
    for(var j=0; j&lt;cols; j++)
    {
        for(var i=0; i&lt;rows; i++)
        {
            if(board[i][j] &lt; currentVal)
            {
                return false;
            }

            currentVal = board[i][j];
        }
    }
    return true;
}

//Shuffle the board
function shuffleBoard()
{
    var shuffleLimit = 0;
    var temp;

    do
    {
        genPossibleMoves();

        while(true)
        {
            // Pick a random cell of possible moves
            temp = possibleMoves[Math.floor(Math.random() * possibleMoves.length)];
            if (temp.x != oldzx || temp.y != oldzy)
            {
                break;
            }
        }

        oldzx = zx;
        oldzy = zy;

        board[zx][zy] = board[temp.x][temp.y];
        zx = temp.x;
        zy = temp.y;
        board[zx][zy] = 16;

    }while(++shuffleLimit &lt; 200);
}

//REstart the game
function restart()
{
    shuffleBoard();
    updateCells();
}

//Start the game
function start()
{
    generateBoard();
    generateCells();
    restart();
}
````

As I had mentioned above, today's article has nothing to do with Artificial Intelligence but in the future, I plan to write a solver for this game that makes use of Heuristics.

Hope you liked reading this article and have fun playing the game!

Stay tuned for more!