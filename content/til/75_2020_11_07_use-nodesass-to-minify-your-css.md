title: Use node-sass to minify your CSS
date: November 7th, 2020
slug: use-nodesass-to-minify-your-css
category: CSS+SCSS
status: active

If you want to turn your `.scss` files to minified `.css` files but without using Webpack or Gulp, just install the `node-sass` package using `npm` package manager and then run this on your terminal:
```bash
sass scss/style.scss css/style.css --style compressed
```
And now, you can use your `style.css` file on production! &#x1F606;

Hope you found this tip useful!
