var colorStack = [];

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

	if (element == parseInt(spriteDim/2)) {
		ctx.fillStyle = color;
		ctx.fillRect(parseInt(squareX), parseInt(squareY), parseInt(squareWidth/squareX)+3, parseInt(squareHeight/squareY)+3);
	}
	else if (colorStack.length == element + 1) {
		ctx.fillStyle = colorStack.pop();
		ctx.fillRect(parseInt(squareX), parseInt(squareY), parseInt(squareWidth/squareX)+3, parseInt(squareHeight/squareY)+3);	
	}
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
		cellPosition *= -1;
		element = 0;
		for(var x=0; x<spriteDim; x++) {
			squareX = x * squareSize + posX;
			squareY = y * squareSize + posY;
			squareWidth = squareX + squareSize;
			squareHeight = squareY + squareSize;

			var color = colors[Math.floor(Math.random() * colors.length)];

			var squareDimensions = {
				'squareX': squareX+2,
				'squareY':squareY+2,
				'squareWidth':squareWidth,
				'squareHeight':squareHeight,
			};

			createSquare(squareDimensions, color, element, spriteDim);

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