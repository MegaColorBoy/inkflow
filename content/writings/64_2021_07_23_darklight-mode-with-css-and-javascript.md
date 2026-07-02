title: Dark/Light mode with CSS and JavaScript
date: September 9th, 2021
slug: darklight-mode-with-css-and-javascript
category: Tutorial
summary: A simple guide on how to implement a dark/light theme switcher with CSS and JavaScript
status: active

It's quite common these days that many websites let their users to decide their preferred color scheme(s). Giving this sort of customizability offers good user experience.

In this article, I'll provide a simple step-by-step guide on how to implement a dark/light theme switcher with HTML, CSS and JavaScript.

<div class="post-notification warning">
	<h3>Prerequisites</h3>
	<p>This article assumes that the reader has a basic know-how on HTML, CSS, JavaScript and basic knowledge on using the command-line.</p>
</div>

## Using CSS variables
I always wanted to implement one for this website too and I thought of making use of CSS variables as I found it to be quite straight forward and I don't have to worry too much about browser support.

Try adding the below CSS to your stylesheet:

```css
	:root {
		--background-color: white;
		--font-color: black;
		--accent-color: red;
		--alt-background-color: black;
		--alt-font-color: white;
		--alt-accent-color: yellow;
	}
	
	html {
		background-color: var(--background-color);
		color: var(--font-color);
	}

	a {
		color: var(--accent-color);
	}

	html[data-theme="dark"] {
		background-color: var(--alt-background-color);
		color: var(--alt-font-color);
	}

	html[data-theme="dark"] a {
		color: var(--alt-accent-color);
	}
	```

The `:root` selector contains a set of default values and in this case, these are just different colors, kind of like how we initialize variables in other programming languages.

For example, whenever the `data-theme` attribute is set to `dark`, the default values will be overidden by the `html[data-theme="dark"]` CSS rule for the theme to take effect.

Really, it's that simple!

## Add some markup
That depends on what you really want to have in your website but for this tutorial, you can just place a simple button somewhere in your navigation bar or anywhere you like:

```html
<button class="themeSwitcher">Dark/Light</button>
```

## Toggle between light and dark themes 
Yes, we are getting there and you just have to write a simple logic that checks if whether the current theme is dark or light based on the class used on the `<body>` element.

```js
$('.themeSwitcher').on('click', function(){
	switch($('body').attr('data-theme')){
		case "dark":
			$('body').attr('data-theme', 'dark');
			break;

		case "light":
		default:
			$('body').attr('data-theme', '');
			break;
	}
});
```

### Save user's preference in their browser
If your button works as expected, good! Now, once you refresh the page, the background would return to it's default mode but that's not what we wanted, right?

But why does it return instead of staying dark? Because your "preference" is not stored in your browser.

Modify your code to store your preferences in your browser:

```html
<script>
$('.themeSwitcher').on('click', function(){
	switch($('body').attr('data-theme')){
		case "dark":
			$('body').attr('data-theme', 'dark');
			localStorage.setItem("theme", "dark");
			break;

		case "light":
		default:
			$('body').attr('data-theme', '');
			localStorage.setItem("theme", "");
			break;
	}
});
</script>
```

This should work fine but you'll want to avoid the "flickering" issue while changing themes or refreshing the page, in order to do that, make sure that you check the user preference before the page is completely loaded:

```html
<script>
	if(localStorage.theme){
		document.documentElement.setAttribute('data-theme', localStorage.getItem("theme"));
	}
</script>
```

## Conclusion
Well, if you've noticed, I wrote a simple theme switcher for my blog too. Try it out and you can inspect the code to see how it works.

Hope you enjoyed this article!

Stay tuned for more!