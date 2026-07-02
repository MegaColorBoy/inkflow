//Random Color Pattern Generator
var colorRange = 4;
var pixelSize = 12;
var colors = [];
var article_canvas = document.getElementById("bg-pattern");
var article_ctx = article_canvas.getContext("2d");

//Generate Random Colors
function generateColors(colorRange){
	colors = [];

	for(var i=0; i<colorRange; i++)
	{
		// var rgb = randomRGB();
		if(i == colorRange - 1)
		{
			colors[i] = "#FFFFFF";
		}
		else
		{
			colors[i] = getRandomColor();
		}
	}

	function getRandomColor()
	{
		var letters = "0123456789ABCDEF".split('');
		var color = "#";
		for(var i=0; i<6; i++)
		{
			color += letters[Math.floor(Math.random() * letters.length)];
		}
		return color;
	}

	// function randomRGB()
	// {
	// 	var rgb = [0,0,0];
	// 	for(var i=0; i<rgb.length; i++)
	// 	{
	// 		rgb[i] = Math.floor((Math.random() * 255) + 1).toString(16);
	// 	}
	// 	return rgb;
	// }
}

function generateCanvasPattern()
{
	var x, y;

	//Clear canvas
	article_ctx.clearRect(0, 0, article_canvas.width, article_canvas.height);
	
	generateColors(colorRange);

	for(y=0; y<=article_canvas.height; y+=pixelSize)
	{
		for(x=0; x<=article_canvas.width; x+=pixelSize)
		{
			//Random color per pixel
			article_ctx.fillStyle = colors[Math.floor(Math.random() * colors.length)];
			article_ctx.fillRect(x, y, pixelSize, pixelSize);
		}
	}
}

//This will convert the canvas to an image.
function convertCanvasToImg()
{
	// var placeholder = document.getElementById("article-bg-image");
	var dataURL = article_canvas.toDataURL();
	$("#article-bg-image").css({
		"background-image" : `url(`+ dataURL +`)`,
		"background-size" : "cover",
		"background-repeat" : "no-repeat",
		"background-position" : "center",
		"height" : "450px"
	});
	// placeholder.style.backgroundImage = dataURL;
	// var imgElement = document.createElement("img");
	// imgElement.className = "article-bg-image";
	// imgElement.src = dataURL;
	// imgElement.style.width = "100%";
	// imgElement.style.height = "100%";
	// imgElement.style.height = "auto";
	document.getElementById("bg-pattern").remove();
	// placeholder.appendChild(imgElement);
}

generateCanvasPattern();
convertCanvasToImg();