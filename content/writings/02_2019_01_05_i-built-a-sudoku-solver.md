title: I built a Sudoku Solver!
date: April 29th, 2017
slug: i-built-a-sudoku-solver
category: Algorithms + Data Structures
summary: I built a sudoku solver using Javascript by implementing the Exhaustive Recursion and Backtracking algorithms.

<link rel="stylesheet" href="/static/projects/sudoku/css/style.css" type="text/css"/>
<script defer type="text/javascript" src="/static/projects/sudoku/js/script.js"></script>

<figure>
    <div id="sudokusolver"></div>
</figure>

Before you read about this article, try playing the Sudoku Solver above. You can only insert numbers ranging from 1 to 9 in any empty cell. Press <kbd>Random Level</kbd> to generate a random sudoku puzzle. Made a mistake? Press <kbd>Reset</kbd> to clear the board. To test the algorithm, Press <kbd>Solve</kbd> to complete the entire puzzle.

As for the source code, you can view it in my [GitHub repository](https://www.github.com/megacolorboy) or can be found near the end of this article.

## What is Sudoku?
Sudoku stems from the two Japanese words: "Su" and "doku", when translated to English, it means "single numbers only". Although, many people feel that Sudoku was invented by the Japanese, it was actually invented by an American named [Howard Garns](https://en.wikipedia.org/wiki/Howard_Garns) in 1979 under the name "Number Place" but died in 1989 before a Japanese publisher named [Nikoli](https://en.wikipedia.org/wiki/Nikoli_(publisher)) made it popular, renamed it as "Sudoku" and which of course, became mainstream in 1986.

## What is it about?
Sudoku is a logic-based, combinatorial, 9x9 number grid puzzle. The puzzles are usually a partially completed grid, thus allows the puzzle solver to come up with a single solution to the puzzle. The objective of this game is to fill the empty spaces in the partially completed 9x9 grid in such a way that each row, column and 3x3 subgrids (that compose the grid) contains all digits from 1 to 9.

## Why did I build it?
Well, one day, I downloaded a Sudoku game on my iPhone and I got hooked to it instantly. I would play the game, usually, during metro rides to my university or any long trips to not make myself feel bored. So one day, I thought ***"What if I built a sudoku solver and see if it could solve all the puzzles from the game?"***, which made me even more curious to see how a computer would do it.

## Implementation
Okay, I know this is the part that you must be waiting for: ***"How to implement this?"***. As I was doing my research on how to implement it, I came across two algorithmic techniques:

+ [Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
+ [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

### Recursion
Recursion is an algorithmic technique used for breaking down larger problems into smaller instances of the same problem. This is also known as [Divide-and-Conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) method. This is usually used in binary search, reversing a file, generating large Fibonacci numbers and the list could go on.

### Backtracking
Backtracking is an algorithmic technique used for searching every possible combination in order to solve a problem in an optimized way. You could be familiar with this technique in popular problems like Chess, the 8 Queen Puzzle or Crossword solvers.

### Explanation
Imagine, you're playing chess with a friend and you've made a silly move, which prompts you to ask your friend: *"Hey, I made a mistake! Can I go back to my old move?"*, your friend (hopefully, a merciful one) would allow you to return back to your old move. So in this case, you'll return back to your old position and begin to restrategize your plans on how to take down the next pawn or maybe finally hatch your plot to trap your opponent's King (you evil person). If it fails, you can ask again but I don't think your friend would be dumb enough to give you another chance!

**Here's a pseudocode on how this strategy would work:**
```text
Find [row,col] of an unassigned cell
If there is none, then return true

For digits from 1 to 9
    If there is no conflict for digit at [row,col]
        Assign digit to [row,col] and recursively try to fill in the rest of the grid
        If this recursion is successful, return true
        Otherwise, remove this digit and try another one
    If all digits have been tried for this cell and nothing worked out
        return false, trigger backtracking and try again
```

**Javascript implementation:**
```js
//Sudoku solver 
function solveSudoku(grid, row, col) {
    var cell = findUnassignedLocation(grid, row, col);
    row = cell[0];
    col = cell[1];

    // base case: if there's no empty cell  
    if (row == -1) {
        return true;
    }

    for (var num = 1; num <= 9; num++) {

        if (noConflicts(grid, row, col, num)) {   
            grid[row][col] = num;

            if (solveSudoku(grid, row, col)) {                
                return true;
            }

            // mark cell as empty (with 0)    
            grid[row][col] = 0;
        }
    }

    // trigger back tracking
    return false;
}

//Find an empty cell
function findUnassignedLocation(grid, row, col) {
    var done = false;
    var res = [-1, -1];

    while (!done) {
        if (row == 9) {
            done = true;
        }
        else {
            if (grid[row][col] == 0) {
                res[0] = row;
                res[1] = col;
                done = true;
            }
            else {
                if (col < 8) {
                    col++;
                }
                else {
                    row++;
                    col = 0;
                }
            }
        }
    }

    return res;
}

//Check if there are any conflicts in row, column or 3x3 subgrid
function noConflicts(grid, row, col, num) {
    return isRowOk(grid, row, num) && isColOk(grid, col, num) && isBoxOk(grid, row, col, num);
}

//Check if this number is valid in this row
function isRowOk(grid, row, num) {
    for (var col = 0; col < 9; col++)
        if (grid[row][col] == num)
            return false;

    return true;
}

//Check if this number is valid in this column
function isColOk(grid, col, num) {
    for (var row = 0; row < 9; row++)
    if (grid[row][col] == num)
        return false;

    return true;    
}

//check if this number is valid in 3x3 subgrid
function isBoxOk(grid, row, col, num) {
    row = Math.floor(row / 3) * 3;
    col = Math.floor(col / 3) * 3;

    for (var r = 0; r < 3; r++)
        for (var c = 0; c < 3; c++)
            if (grid[row + r][col + c] == num)
                return false;

    return true;
}
```

## What's next?
So now that you have understood the rough concept of how it works, combining and applying these two techniques in a Sudoku puzzle i.e. trying out every possible number to fill an empty square in the 9x9 grid would allow the computer to solve Sudoku puzzles more efficiently and quickly than using a plain [Brute Force](https://en.wikipedia.org/wiki/Brute-force_search) technique on puzzle that has around 4 x 1038 possibilities (which means, you'll probably require next-gen hardware to compute one puzzle that could take billions of years!)

Oh, you can play around with the Sudoku Solver above by trying out a Sudoku puzzle or generate a random one and solve it. Or best, if you'd like to challenge yourself, you could try to implement this solution on Project Euler's [Problem 96](https://projecteuler.net/problem=96) by solving all 50 sudoku puzzles in a row!

## References
+ [Stanford's Exhaustive Recursion and Backtracking](https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf)
+ [Solving Every Sudoku Puzzle](http://norvig.com/sudoku.html)