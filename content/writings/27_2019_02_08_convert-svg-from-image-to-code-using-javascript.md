title: Convert SVG from Image to Code using Javascript
date: February 24th, 2018
slug: convert-svg-from-image-to-code-using-javascript
category: Programming
summary: Two weeks ago, I wrote a small script to convert SVG from Image to Code using Javascript that allowed me to play around with it's attributes and properties.

Have you ever downloaded minimal and beautiful looking SVG icons and
added them into your HTML code as an ***&lt;img&gt;*** instead of
***&lt;svg&gt;*** tag? The answer is: ***"yes, you're right!"***.

Okay, how about another question?

What would you do if you want to change all of those SVG icons to black,
red or blue? Your answer would be: ***"Well, I would edit the colors of
all the vector images in Adobe Illustrator and then refresh my page to
see the changes."***, if that's your answer, then what would you do if
you have to do it for multiple icons in multiple pages in a short amount
of time?

Two weeks ago, I faced this same scenario and I found a quick solution
to it and I will be sharing it in this article on how to convert SVG
from image to code using Javascript and how it allowed me to play around
with attributes and properties.

## Why convert from Image to Code?

Well, as a developer, it allows me to interact with every part of the
SVG such as changing the colors, adjusting the height and width, animate
it and so on. In this article, I will show you an example on how I could
do a simple color change on an SVG image that I had downloaded from
[flaticon](https://www.flaticon.com).

<figure>
    <img src="/static/images/space.svg"/>
    <figcaption>
        Figure 1. Original SVG Space Icon
    </figcaption>
</figure>

## How to convert from Image to Code?

Simple, just convert the SVG image into an XML format using
***XMLSerializer()*** then give it a class name like ***"custom-svg-icon"***
and execute the code! Below, I have provided a code snippet, I hope the
comments will help you out!

**Code snippet:**

```js
    $(function(){
     //Change the class name, if it has to be applied for more SVG elements
     jQuery('img.custom-svg-icon').each(function(){
     var $img = jQuery(this); // The image
     var imgID = $img.attr('id'); // ID attribute
     var imgClass = $img.attr('class'); // Class Name
     var imgURL = $img.attr('src'); // URL of the SVG image

     jQuery.get(imgURL, function(data) {
     //The data param contains the XML data of the SVG image
     //alert(new XMLSerializer().serializeToString(data));

     // Get the SVG tag, ignore the rest
     var $svg = jQuery(data).find('svg');

     // Give the image's ID to the SVG
     if(typeof imgID !== 'undefined') 
     {
     $svg = $svg.attr('id', imgID);
     }

     // Give the image's class to the SVG
     if(typeof imgClass !== 'undefined') 
     {
     $svg = $svg.attr('class', imgClass+' replaced-svg');
     }

     // Remove any invalid XML tags as per http://validator.w3.org
     $svg = $svg.removeAttr('xmlns:a');

     // Check if the viewport is set, else we gonna set it if we can.
     if(!$svg.attr('viewBox') && $svg.attr('height') && $svg.attr('width')) 
     {
     $svg.attr('viewBox', '0 0 ' + $svg.attr('height') + ' ' + $svg.attr('width'))
     }

     // Replace image with new SVG
     $img.replaceWith($svg);
     
     }, 'xml'); //Returns as XML
     });
    });
```

Give it some custom CSS to change the color and width of the SVG image:

```css
    svg path, svg rect
    {
        fill: #ff5a5f;
    }

    .custom-svg-icon
    {
        width: 170px;
        height: 170px;
    }
```

Right-click on the image, hit ***"Inspect Element"*** and view the
converted image below but this time, you'll see it as an SVG element:

<script defer src="/static/projects/svg-img-to-code/script.js"></script>

<figure>
    <img class="custom-svg-icon" src="/static/images/space.svg"/>
    <figcaption>
        Figure 2. Converted SVG Space Icon
    </figcaption>
</figure>

However, there are a few downsides to this as SVG code is hard to
maintain, pretty messy and sometimes quite complex especially if it
contains a lot of paths, circles and rectangles but in a scenario that
is similar to what I have faced, I think it's pretty useful, otherwise,
just stick to adding your SVG images using the ***&lt;img&gt;*** tag.

Hope you have found this article useful!

## Credit

Icons made by [Eucalyp](https://www.flaticon.com/authors/eucalyp) from [www.flaticon.com](https://www.flaticon.com/) is licensed by [CC 3.0
BY](http://creativecommons.org/licenses/by/3.0/)