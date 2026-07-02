title: Optimize your website performance
date: July 25th, 2019
slug: optimize-your-website-performance
category: Tips
summary: Sharing my experiences on website optimization.

This article is directed towards audiences who are keen on making their websites and web applications load faster and perform better.

I won't be focusing on the SEO (Search Engine Optimization) part of it but rather, I'll be covering on how to overcome performance bottleneck issues. If you want to know more about SEO, you can go [here](http://lmgtfy.com/?q=SEO+Optimization).

Recently, I boosted my company's [website](https://www.kit.ae) from a lagging 10-30 seconds (I know, that's really embarassing!) to a smooth 1.7 to 2.5 seconds load speed, so that's why I thought of sharing my experiences and tips on this article.

Before we get there, let's first understand what could probably make your website perform bad or load slowly. Afterwards, there'll be some strategies on how you could fix those issues and make it optimal.

## Why is my website so slow?
You're not a developer if you've never heard this in your day-to-day life. In today's era, the standard average page load time is under 3 seconds, anything more than that, you might lose a visitor and that can affect your website's SEO in the long run.

Here are some of the reasons, in my opinion:

- [Too many HTTP requests](#reason1)
- [Inefficient database calls/queries](#reason2)
- [Images aren't optimized](#reason3)
- [Improper page caching](#reason4)
- [Your codebase stinks](#reason5)
- [Shared Hosting Service](#reason6)

### <a id="reason1"></a> Too many HTTP requests
According to GTMetrix, a web page should have an average of 92 requests but there are websites that have over 100+ requests and that's crazy, especially, if you try to access the website on a slower network.

There can be many factors that contributes to an increase in HTTP requests:

- Too many images on a page
- CSS and JS files are not compressed and minified
- Calling external libaries like jQuery or Bootstrap from a Content-Delivery Network
- Loading all JS files at one go

Since, each DOM element is generated in a top-down manner, it would display the completed page when all resources are loaded, hence is why you shouldn't have too many server requests.

### <a id="reason2"></a> Inefficient database queries
Let's say, you have a page that displays a list of products from your SQL database and you execute this query:

```sql
SELECT * FROM products
```

Sorry, it's inefficient. Why? In a real-life scenario, a table may contain a lot of columns and multiply that with **x** number of database calls the server has to make for EVERY request that comes from a visitor. You get it, right?

This could be worse if you have an unorganized database structure. Plan well, my friend.

### <a id="reason3"></a> Images aren't optimized
Images that are uncompressed, have a higher resolution or large file size can be detrimental to the site's performance which creates an unpleasant user experience.

### <a id="reason4"></a> Improper page caching
If you've built a dynamic page that displays a blog article, it probably performs a lot of requests/callbacks to generate a page with necessary information. Multiply that with **x** number of user sessions and that'll place a huge workload on the server.

### <a id="reason5"></a> Your codebase stinks
This is a very deep problem especially if the code is never refactored in a very long time.

Common causes of code smells are:

- Duplicate code
- Large methods or classes
- Too many parameters
- Long line of code
- Unnecessary uses of loops and conditions
- Unused code

There's much more to this but if you're facing this, it's about time that you start fixing your codebase and keep it mint condition.

### <a id="reason6"></a> Shared Server Hosting
Ah, this is the most common culprit. Many people host their websites on a shared server and guess what? Shared hosting means ***shared system resources*** because apart from your website, there could be 5 or more websites hosted on the same server.

## How to overcome these issues?
Before we move on, let me just clarify that the techniques I've used below worked out for me but it may or may not work for you.

Here are the following methods that worked out for me:

- [Compress & Resize Images](#tip1)
- [Minify Javascript](#tip2)
- [CSS Preprocessors to the rescue!](#tip3)
- [Defer Javascript](#tip4)
- [Efficient database queries](#tip5)
- [PHP Page Caching](#tip6)
- [Refactor your codebase](#tip7)
- [LazyLoad DOM Elements](#tip8)
- [Dedicated Server](#tip9)

### <a id="tip1"></a> Compress & Resize Images
I'm sure that there are multiple ways to compress and resize an image like using Adobe Photoshop but what if there are hundreds and thousands of images? It'd be time consuming to do all of that.

I created an ad hoc solution using a PHP-based image extension named [ImageMagick](https://github.com/Imagick/imagick). This library is used to create and modify images using the ImageMagick Library.

Since it can be used directly from the terminal, I wrote a small script using PowerShell to compress and resize the images in all folders in one go!

**Snippet to resize images:**
```bash
magick mogrify -resize 256x256 -format *.jpg *.jpeg *.png
```

**Snippet to compress images:**
```bash
magick mogrify -quality 70% *.jpg *.jpeg *.png
```

The logic of the code is pretty straightforward. All it has to do is get a list of files with ends with image extensions (.jpg, .jpeg, .png) and modify the resolution to 640x480 and reduce the quality to a 70%.

Previously, all images of the website combined was around 800MB and after executing the script, it went down to a mere 70MB. The quality of the images weren't ruined and the aspect ratio didn't change. That's quite astounding.

### <a id="tip2"></a> Minify Javascript
Ever inspected someone's CSS or JS code on Chrome Debugger and saw something like this:

```js
for(var a=[i=0];i<20;a[i]=i++);
```

This code above is unreadable but it still retains it's previous functionality:
```js
var array = [];
for (var i = 0; i < 20; i++) {
    array[i] = i;
}
```

This process is known as [minification](https://en.wikipedia.org/wiki/Minification_(programming)). It's a way of removing all spaces, unnecessary characters and comments that would help reduce the size of the source code and make it more efficient to be transferred over the network.

Using a module bundler like Webpack, you can minify and merge all of your Javascript files into one sizeable chunk. Webpack's documentation is one of the worst that I have seen and I had to take help from StackOverflow to figure it out but however, it gets the job done. 

Want to know to configure it? Check out this [thread from StackOverflow](https://stackoverflow.com/questions/43436754/using-webpack-with-an-existing-php-and-js-project) for more in detail.

### <a id="tip3"></a> CSS Preprocessors to the rescue!
Trust me, these are life-savers. I used to hate writing a lot of CSS but now, I like writing CSS because of this reason. I chose ***SASS*** as my CSS preprocessor and it's basically CSS-on-steroids!

It's got some cool features like reusable CSS code, writing functions a.k.a `@mixin` and calling them using `@include`, nested syntaxes and import multiple CSS modules.

Writing in ***SASS*** is no different than writing in CSS but it allows you to modularize and organize your code in a fashionable manner. This allows you to even split CSS code to different modules, especially, if your HTML component uses a lot of CSS elements.

Oh, you can also create a minified version of your CSS code and push it into production.

### <a id="tip4"></a> Defer Javascript
The `defer` attribute used in the `<script>` tag will allow the JS file to be executed after the page has finished parsing all the DOM elements.

When the attribute is used, it'll look like this:
```html
<script type="text/javascript" src="script.js" defer></script>
```

This could save a lot of time especially if it contains code that is not critical.

If you want to read more about it, click [here](https://stackoverflow.com/questions/10808109/script-tag-async-defer).

### <a id="tip5"></a> Efficient database queries
As mentioned above, inefficient database queries could be detrimental to your website's performance. You can get rid of it with the following methods:

- Maintain a good table structure
- Keep your database architecture organized. Read more about [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
- Keep your SQL query as simple as possible

Usage of clauses like `WHERE`, `JOIN` and `GROUP BY` are important but when it comes to performance, use it wisely.

### <a id="tip6"></a> PHP Page Caching
My company's website is mostly dynamic and I realized that all it does is fetch data from the servers to generate static information.

So, I thought of writing a caching module, in which, when any given page is accessed in the website, it would create a fully-generated static page with an expiry time of 5 minutes. So, when another user enters the same page, it will serve the static page, so no more delays for anyone.

This drastically reduced the load on the website's server because as mentioned [above](#reason4), it takes a lot of resources to create a page, dynamically.

You can find the source code of the caching module in my GitHub [repository](#).

### <a id="tip7"></a> Refactor your codebase
Refactoring has a lot of benefits and in fact, it could reduce the size of your website, fix any unfixed bugs and more. All of which can contribute to an improved performance of your website.

So, please do yourself a favor and start cleaning up your codebase. If you don't know where to start, [go here](https://refactoring.guru/refactoring).

### <a id="tip8"></a> LazyLoad DOM Elements
Usually, whenever a page is opened by a user, it's contents are downloaded in a single go but this could be annoying if it disrupts the first view of the page.

So, what LazyLoad does is that instead of loading all of the content in a bulk, it only displays part of the content when a part of the page is accessed. The pages are created with a placeholder and will replace it with actual content only when the user needs it.

Examples of this can be seen in the form of:

- Image galleries
- Social media posts
- Infinite scrolling
- Pagination

This technique helps in performance but might create a negative impact on SEO in terms of webpage rankings.

If you want to give it a shot, try using this jQuery [library](http://jquery.eisbehr.de/lazy/).

### <a id="tip9"></a> Dedicated Server
Most hosting websites offer this service, you just have to buy a server and it would only host your website. 

It's highly configurable and you won't have any issues regarding performance, however, it doesn't come without an expensive price tag on it but if you're willing to pay, it can be a great long-term investment.

## Conclusion
If you've reached here, thank you for reading!

Let me know if any of these strategies have helped boost your website's performance and share it with other people too! Got more suggestions? Please send me an [email](mailto:megacolorboy@gmail.com) and we can talk more about it.

Hope you liked reading this article!

Stay tuned for more!