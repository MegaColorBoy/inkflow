let generativeArt = (() => {
	let _self = this;
	let _articles = document.querySelectorAll(".article");
	// Utiities
	_self.utils = {
		generateRandomNumber: (min, max) => {
			return Math.floor(Math.random() * (max - min + 1)) + min;
		},
		getRandomColor: () => {
			let letters = "0123456789ABCDEF".split('');
			let color = "#";
			for(let i=0; i<6; i++) {
				color += letters[Math.floor(Math.random() * letters.length)];
			}
			return color;
		},
		generateColors: (colorRange) => {
			colors = [];
			for(let i=0; i<colorRange; i++) {
				colors[i] = (i == colorRange - 1) ? "#EEEEEE" : _self.utils.getRandomColor();
			}
			return colors;
		},
		injectArtPlaceholderIntoArticles: (className, elementTag) => {
			_articles.forEach((el, idx) => {
				isElementExist = el.querySelector('iframe') || el.querySelector('canvas') || el.querySelector('p:first-of-type img') || el.querySelector('.article-body figure:first-of-type');
				// Inject .tiles-wall class after the article's description
				if(!isElementExist) {
					container = null;
					if(elementTag == 'svg') {
						container = document.createElementNS("http://www.w3.org/2000/svg", "svg");
					} else {
						container = document.createElement(elementTag);
					}
					container.classList.add(className);
					articleDescriptionElement = el.querySelector('.article-header > .description')
					if(articleDescriptionElement) {
						articleDescriptionElement.parentNode.appendChild(container);	
					}
				}
			})
		}
	};
	// Bauhaus Tiles Art 
	_self.bauhaus = () => {
		injectStyle = () => {
			style = `<style>
				.tiles-wall {
				    border-radius: 4px;
				    display: grid;
				    width: 100%;
				    grid-template-columns: repeat(10, 50px);
				    grid-template-rows: repeat(4, 50px);
				    margin: 20px 0px 0px;
				    overflow: hidden;
				}

				.tiles-wall div {
					width: 50px;
					height: 50px;
				}

				/* STYLES  */
				.circle {
				}
				div[class*="circle-"] {
					background-size: 200% 200% !important;
				}
				.circle-up {
					background-position: bottom !important;
				}
				.circle-right {
					background-position: left !important;
				}
				.circle-down {
					background-position: top !important;
				}
				.circle-left {
					background-position: right !important;
				}
				.triangle-up, .triangle-down {
				}
			</style>`;
			document.head.insertAdjacentHTML("beforeend", style);
		};
		generateTiles = () => {
			let tilesWall = document.querySelectorAll(".tiles-wall");
			
			const colorPalettes = [
				["#E8C547", "#30323D", "#4D5061", "#5C80BC", "#CDD1C4"],
				["#3B429F", "#AA7DCE", "#F5D7E3", "#F4A5AE", "#A8577E"],
				["#DE9151", "#F34213", "#2E2E3A", "#BC5D2E", "#BBB8B2"],
				["#F1E4E8", "#E2DCDE", "#CEB1BE", "#B97375", "#2D2D34"],
				["#002A32", "#C4A29E", "#EBA6A9", "#FFC6AC", "#F40076"],
				["#1446A0", "#DB3069", "#F5D547", "#EBEBD3", "#3C3C3B"],
				["#D6FFF6", "#231651", "#4DCCBD", "#2374AB", "#FF8484"],
				["#1C1D21", "#A288A6", "#BB9BB0", "#CCBCBC", "#F1E3E4"],
				["#FCFCFC", "#F7567C", "#FFFAE3", "#99E1D9", "#5D576B"]
			];
			
			const styles = [
				"circle-up",
				"circle-right",
				"circle-down",
				"circle-left",
				"circle",
				"triangle-up",
				"triangle-down"
			];
			
			tilesWall.forEach((item, idx) => {
				let colors = colorPalettes[_self.utils.generateRandomNumber(0, colorPalettes.length - 1)];
				
				for (r = 1; r <= 40; r++) {
					let gradientSettings = {};
					
					const gridItem = document.createElement("div");
					const selectedStyle = `${styles[_self.utils.generateRandomNumber(0, styles.length - 1)]}`;
					gridItem.setAttribute("class", selectedStyle);

					switch(selectedStyle) {
						case "triangle-up":
							gradientSettings = {
								'type': "linear-gradient",
								'angle': "225deg",
								'p1': "50%",
								'p2': "51%"	
							};
							break;
						case "triangle-down":
							gradientSettings = {
								'type': "linear-gradient",
								'angle': "315deg",
								'p1': "50%",
								'p2': "51%"
							};
							break;
						default:
							gradientSettings = {
								'type': "radial-gradient",
								'angle': "circle",
								'p1': "35%",
								'p2': "36%"	
							};
							break;
					}

					gridItem.style.background = `${gradientSettings.type}(${gradientSettings.angle},  ${
						colors[_self.utils.generateRandomNumber(0, colors.length - 1)]
					} ${gradientSettings.p1}, ${colors[_self.utils.generateRandomNumber(0, colors.length - 1)]} ${gradientSettings.p2})`;

					item.appendChild(gridItem);
				}
			});	
		};
		init = () => {
			injectStyle();
			_self.utils.injectArtPlaceholderIntoArticles('tiles-wall', 'div');
			generateTiles();
		};
		init();
	};
	// Pixel Tiles Art
	_self.pixels = () => {
		const colorRange = 4;
		const pixelSize = 10;
		injectStyle = () => {
			style = `<style>
				.pixels-canvas {
					width: 500px;
					height: 200px;
					border-radius: 4px;
					margin: 5px 0px 0px;
					overflow: hidden;
				}
			</style>`;
			document.head.insertAdjacentHTML("beforeend", style);
		};
		drawPixelPatternOnCanvas = (canvas) => {
			let ctx = canvas.getContext("2d");
			let row, col;
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			colors = _self.utils.generateColors(colorRange);
			for(col=0; col<=canvas.height; col+=pixelSize) {
				for(row=0; row<=canvas.width; row+=pixelSize) {
					//Random color per pixel
					ctx.fillStyle = colors[Math.floor(Math.random() * colors.length)];
					ctx.fillRect(row, col, pixelSize, pixelSize);
				}
			}
		};
		generateCanvasPattern = () => {
			let pixelCanvases = document.querySelectorAll(".pixels-canvas");
			pixelCanvases.forEach((el, idx) => {
				drawPixelPatternOnCanvas(el);
			});
		};
		init = () => {
			injectStyle();
			_self.utils.injectArtPlaceholderIntoArticles('pixels-canvas', 'canvas');
			generateCanvasPattern();
		}
		init();
	};
	// Truchet Tiles Art -- Quarter Circles
	_self.truchetQuarterCircles = () => {
		injectStyle = () => {
			style = `<style>
				.truchet-canvas {
					background-color: #EEEEEE;
					border-radius: 4px;
					margin: 5px 0px 0px;
					overflow: hidden;
				}
			</style>`;
			document.head.insertAdjacentHTML("beforeend", style);
		};
		generateArcsLeft = (ctx, coordinates) => {
			canvasContext = ctx.getContext('2d');
			canvasContext.lineWidth = 5;
			canvasContext.beginPath();
			canvasContext.arc(coordinates.x, coordinates.y, coordinates.w/2, 0, Math.PI*1/2, 0);
			canvasContext.strokeStyle = "#222222";
			canvasContext.stroke();
			canvasContext.beginPath();
			canvasContext.arc(coordinates.x + coordinates.w, coordinates.y + coordinates.h, coordinates.w/2, Math.PI*3/2, Math.PI, 1);
			canvasContext.strokeStyle = "#222222";
			canvasContext.stroke();
		};
		generateArcsRight = (ctx, coordinates) => {
			canvasContext = ctx.getContext('2d');
			canvasContext.lineWidth = 5;
			canvasContext.beginPath();
			canvasContext.arc(coordinates.x + coordinates.w, coordinates.y, coordinates.w/2, Math.PI*1/2, Math.PI, 0);
			canvasContext.strokeStyle = "#222222";
			canvasContext.stroke();
			canvasContext.beginPath();
			canvasContext.arc(coordinates.x, coordinates.y + coordinates.h, coordinates.w/2, 0, 2*Math.PI*3/4, 1);
			canvasContext.strokeStyle = "#222222";
			canvasContext.stroke();
		};
		generateRectangle = (ctx, coordinates) => {
			canvasContext = ctx.getContext('2d');
			canvasContext.rect(coordinates.x, coordinates.y, coordinates.w, coordinates.h);
			canvasContext.stroke();
		};
		generateCanvasPattern = () => {
			let truchetCanvases = document.querySelectorAll(".truchet-canvas");
			truchetCanvases.forEach((el, idx) => {
				ctx = el.getContext('2d');
				ctx.canvas.width = 500;
				ctx.canvas.height = 200;
				var s = 50;
				for(let x = 0; x < el.width; x += s) {
					for(let y = 0; y < el.height; y += s) {
						// generateRectangle(el, {x:x, y:y, w:s, h:s});
						if (0.5 >= Math.random()) {
							generateArcsLeft(el, {x:x, y:y, w:s, h:s});
						} else {
							generateArcsRight(el, {x:x, y:y, w:s, h:s});
						}
					}
				}
			});
		};
		init = () => {
			injectStyle();
			_self.utils.injectArtPlaceholderIntoArticles('truchet-canvas', 'canvas');
			generateCanvasPattern();
		}
		init();
	};
	// Truchet Tiles Art -- Triangles
	_self.truchetTriangles = () => {
		injectStyle = () => {
			style = `<style>
				.truchet-triangles-pattern {
					width: 100%;
					height: 200px;
					border-radius: 4px;
					margin: 5px 0px 0px;
					overflow: hidden;
				}
			</style>`;
			document.head.insertAdjacentHTML("beforeend", style);
		};
		triangle0 = (svg, c, x, y, w, h) => {
			tri(svg, c, x, y, x + w, y, x, y + h)
		};
		triangle1 = (svg, c, x, y, w, h) => {
			tri(svg, c, x + w, y, x + w, y + h, x, y)
		};
		triangle2 = (svg, c, x, y, w, h) => {
			tri(svg, c, x + w, y + h, x, y + h, x + w, y)
		};
		triangle3 = (svg, c, x, y, w, h) => {
			tri(svg, c, x, y + h, x, y, x + w, y + h)
		};	
		tri = (svg, c, x1, y1, x2, y2, x3, y3) => {
			let p = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
			p.setAttribute("points", `${x1},${y1} ${x2},${y2} ${x3},${y3}`)
			p.setAttribute("style", `fill:${c}`)
			svg.appendChild(p)
		};
		rand = (m) => {
			return Math.floor(Math.random() * Math.floor(m))
		};
		drawTrianglePatternOnPlaceholder = (svg) => {
			let tiles = 25;
			let w = 500 / tiles;
			let h = 500 / tiles;
			const colorPalettes = [
				["#E8C547", "#30323D", "#4D5061", "#5C80BC", "#CDD1C4"],
				["#3B429F", "#AA7DCE", "#F5D7E3", "#F4A5AE", "#A8577E"],
				["#DE9151", "#F34213", "#2E2E3A", "#BC5D2E", "#BBB8B2"],
				["#F1E4E8", "#E2DCDE", "#CEB1BE", "#B97375", "#2D2D34"],
				["#002A32", "#C4A29E", "#EBA6A9", "#FFC6AC", "#F40076"],
				["#1446A0", "#DB3069", "#F5D547", "#EBEBD3", "#3C3C3B"],
				["#D6FFF6", "#231651", "#4DCCBD", "#2374AB", "#FF8484"],
				["#1C1D21", "#A288A6", "#BB9BB0", "#CCBCBC", "#F1E3E4"],
				["#FCFCFC", "#F7567C", "#FFFAE3", "#99E1D9", "#5D576B"]
			];
			let colors = colorPalettes[rand(colorPalettes.length)];
			for (let row = 0; row < tiles; row++) {
				for (let col = 0; col < tiles; col++) {
					let x = col * w
					let y = row * h
					let r = rand(4)
					let c = colors[rand(colors.length)]
					switch (r) {
						case 0:
							triangle0(svg, c, x, y, w, h);
						break;
						case 1:
							triangle1(svg, c, x, y, w, h);
						break;
						case 2:
							triangle2(svg, c, x, y, w, h);
						break;
						case 3:
							triangle3(svg, c, x, y, w, h);
						break;
					}
				}
			}
		};
		generatePattern = () => {
			let truchetPlaceholders = document.querySelectorAll('.truchet-triangles-pattern');
			truchetPlaceholders.forEach((el, idx) => {
				drawTrianglePatternOnPlaceholder(el);
			});
		};
		init = () => {
			injectStyle();
			_self.utils.injectArtPlaceholderIntoArticles('truchet-triangles-pattern', 'svg');
			generatePattern();
		};
		init();
	};
	// TODO: Mondrian Tiles Art
	_self.mondrian = () => {
		console.log("coming soon.");
	};
	// TODO: Hypnotic Squares
	_self.hypnoticSquares = () => {
		console.log("coming soon.");
	};
	// TODO: Lines
	_self.lines = () => {
		injectStyle = () => {
			style = `<style>
				.lines-art {
					background-color: #111111;
					width: 100%;
					height: 100%;
					border-radius: 4px;
					margin: 5px 0px 0px;
					overflow: hidden;
				}
			</style>`;
			document.head.insertAdjacentHTML("beforeend", style);
		},
		draw = (ctx, x, y, width, height) => {
			let leftToRight = Math.random() >= 0.5;
			if(leftToRight) {
				ctx.moveTo(x, y);
				ctx.lineTo(x + width, y + height);    
			} else {
				ctx.moveTo(x + width, y);
				ctx.lineTo(x, y + height);
			}
			ctx.strokeStyle = "#555555";
			ctx.stroke();
		},
		generateCanvasPattern = () => {
			let step = 20;
			let linesArtCanvases = document.querySelectorAll(".lines-art");
			linesArtCanvases.forEach((el, idx) => {
				ctx = el.getContext('2d');
				ctx.canvas.width = 500;
				ctx.canvas.height = 200;
				ctx.lineCap = 'round';
				ctx.lineWidth = 2;

				for(let x = 0; x < ctx.canvas.width; x += step) {
					for(let y = 0; y < ctx.canvas.height; y+= step) {
						draw(ctx, x, y, step, step);    
					}
				}
			})
		},
		init = () => {
			injectStyle();
			_self.utils.injectArtPlaceholderIntoArticles('lines-art', 'canvas');
			generateCanvasPattern();
		};
		init();
	};
	// TODO: Joy Division
	_self.joyDivision = () => {
		console.log("coming soon.");
	};
	// Main function
	_self.init = () => {
		// let methods = ['truchetTriangles', 'truchetQuarterCircles', 'bauhaus', 'pixels'];
		// let methods = ['truchetTriangles', 'truchetQuarterCircles', 'bauhaus', 'lines'];
		let methods = ['truchetTriangles', 'bauhaus'];
		_self[methods[_self.utils.generateRandomNumber(0,methods.length-1)]]();
	};
	return _self;
})();
generativeArt.init();