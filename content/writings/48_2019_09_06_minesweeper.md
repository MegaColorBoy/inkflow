title: Minesweeper Clone
date: September 6th, 2019
slug: minesweeper-clone
category: Personal Challenge
summary: Wrote an old classic puzzle game using Javascript.

<iframe src="/static/projects/minesweeper" width='500' height='590'></iframe>

Before you read this article, play with the above game. The rule is simple, reveal one cell at a time by clicking on them, If the cell you've clicked on is clear, you'll see the number of mines that's adjacent to it. Else, if it's a mine, then all mines will explode and you lose the game. Reload the game by clicking the ***Reset*** button.

The source code of the game can be found [over here](https://github.com/megacolorboy/BlogProjects/tree/master/minesweeper).

## Background
It's a classical puzzle game that gained immense popularity when it came along with Windows 3.1 OS. To be honest, I never really had any experience playing this game until a few days ago, I had a sudden curiosity as to how it works. I studied it's game mechanics on Wikipedia and it turned to be simple enough to write a clone in Javascript.

## Game mechanics
What makes it interesting to play is it's simplicity in which all that matters is that you shouldn't click the cell that goes "KABOOM!".

Here are some of the game mechanics:

- [Generate cells](#generate-cells)
- [Placing the mines](#place-mines)
- [Reveal the mines](#reveal-mines)
- [Scan for mines](#scan-mines)
- [Level completion](#level-complete)

### <a id="generate-cells"></a> Generate cells
Generating the grid is pretty much straightforward. Each cell will have an attribute named <mark>data-mine</mark> with a boolean value of <mark>true</mark> or <mark>false</mark>.
```js
//Generate minesweeper grid
const generateGrid = () => {
    allowClick = true;
    grid.innerHTML = "";
    for(let i=0; i&lt;size; i++) {
        let row = grid.insertRow(i);
        for(let j=0; j&lt;size; j++) {
            let cell = row.insertCell(j);
            cell.onclick = function(){clickCell(this);}
            let mine = document.createAttribute("data-mine");
            mine.value = "false";
            cell.setAttributeNode(mine);
        }
    }
    setMines();
}
```

### <a id="place-mines"></a> Placing the mines
After the grid is generated, a mine will be added to each random cell.
```js
//Set mines
const setMines = () => {
    for(let i=0; i&lt;size*2; i++) {
        let r = Math.floor(Math.random() * size);
        let c = Math.floor(Math.random() * size);
        let cell = grid.rows[r].cells[c];
        cell.setAttribute("data-mine", "true");
        if(testMode){cell.innerHTML = "&#x1f4a3;";}
    }
}
```

### <a id="reveal-mines"></a> Reveal the mines
If you've clicked on a mine, every cell that has a mine will be exposed and then it's game over.
```js
//Reveal mines
const revealMines = () => {
    for(let i=0; i&lt;size; i++) {
        for(let j=0; j&lt;size; j++) {
            let cell = grid.rows[i].cells[j];
            if(cell.getAttribute("data-mine") === "true") {
                cell.className = "mine";
                cell.innerHTML = "&#x1f4a3;";
            }
        }
    }
}
```

### <a id="scan-mines"></a> Scan for mines
When you click on a tile, there are 2 possibilities i.e. either the cell is a mine or not.

If it's a mine, we know what happens, it's self explanatory. If it's not a mine, what happens then? Well, it'll start scanning for mines that are adjacent to it in all eight directions:

<table class="table">
    <tr>
        <th>Direction</th>
        <th>Coordinates</th>
    </tr>
    <tr>
        <td>Top</td><td>(row - 1, col)</td>
    </tr>
    <tr>
        <td>Bottom</td><td>(row + 1, col)</td>
    </tr>
    <tr>
        <td>Left</td><td>(row, col - 1)</td>
    </tr>
    <tr>
        <td>Right</td><td>(row, col + 1)</td>
    </tr>
    <tr>
        <td>Top Left</td><td>(row - 1, col - 1)</td>
    </tr>
    <tr>
        <td>Top Right</td><td>(row - 1, col + 1)</td>
    </tr>
    <tr>
        <td>Bottom Left</td><td>(row + 1, col - 1)</td>
    </tr>
    <tr>
        <td>Bottom Right</td><td>(row + 1, col + 1)</td>
    </tr>
</table>

If there aren't any mines adjacent to it, it'll reveal all adjacent cells via recursion.
```js
    //Click a cell
    const clickCell = (cell) => {
        if(allowClick != false) {
            //If it's a mine, game over
            if(cell.getAttribute("data-mine") === "true") {
                alert("game over");
                revealMines();
                allowClick = false;
            }
            //If it's not a mine, reveal the mines
            else {
                //Mark it as "clicked"
                cell.className = "clicked";
                scanForMines(cell);
                checkGameStatus();
            }       
        }
    }

    //Scan for mines that are adjacent to the cell
    const scanForMines = (cell) => {
        let rowPos = cell.parentNode.rowIndex;
        let colPos = cell.cellIndex;
        let mineCount = 0;

        for(let i=Math.max(rowPos-1, 0); i&lt;Math.min(rowPos+1, size-1); i++) {
            for(let j=Math.max(colPos-1, 0); j&lt;Math.min(colPos+1, size-1); j++) {
                let adjacentCell = grid.rows[i].cells[j];
                if(adjacentCell.getAttribute("data-mine") == "true") {
                    mineCount++;
                }
            }
        }

        cell.innerHTML = mineCount > 0 ? mineCount : " ";

        //If zero mines, then reveal all adjacent cells
        if(mineCount == 0) {
            for(let i=Math.max(rowPos-1, 0); i&lt;Math.min(rowPos+1, size-1); i++) {
                for(let j=Math.max(colPos-1, 0); j&lt;Math.min(colPos+1, size-1); j++) {
                    let adjacentCell = grid.rows[i].cells[j];
                    if(adjacentCell.innerHTML == "") {
                        clickCell(adjacentCell);
                    }
                }
            }
        }
    }
```

### <a id="level-complete"></a> Level completion
If the player completed the game without clicking on any mine, the level is complete.
```js
    //Check game status
    const checkGameStatus = () => {
        let levelComplete = true;
        for(let i=0; i&lt;size; i++) {
            for (let j=0; j&lt;size; j++) {
                var cell = grid.rows[i].cells[j];
                if((cell.getAttribute("data-mine") == "false") && (cell.innerHTML == "")) {
                    levelComplete = false;
                }
            }
        }

        if(levelComplete) {
            alert("Congratulations, you won!");
            revealMines();
        }
    }
```

## Conclusion
Well, that's about it. I had fun writing this game. Do you want me to build more games like this? Send me an email about it and I'll see what I can do from my end.

Have fun playing the game and oh, don't blow yourself up! &#x1F61C;

Hope you liked reading this article!

Stay tuned for more!


