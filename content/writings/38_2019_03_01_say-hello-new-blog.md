title: Say Hello, New Blog
date: March 1st, 2019
slug: say-hello-new-blog
category: Update
summary: Everything from new updates to shifting to a static site generator.

Hello, 2019!

Uhh, I guess it's a bit too late, but better late than never!

Lately, the concept of using a static site generator has become the new rage. This blog that you are seeing now is powered by a custom-built static site generator written on Python and trust me, I love it!

## Why shift from a dynamic to static website?
It took me some time to make a decision on why I would need to make a shift from a dynamic website to a website that serves static files, here are some of my reasons:

+ Edit posts using Markdown
+ Increased speed
+ Eliminates the use of CMS and Databases
+ Pre-generated and will be served on request without any delay
+ Lightweight
+ Ease of Maintenance
+ More secure

Apart from that, I wanted to understand the concept of Static Site Generators, so I thought of writing a static site generator using Python.

Sure, there are many static site generators available online but I always like to be the curious cat!

## How it works
Nothing complicated, the concept is pretty simple. All you have to do is write down your articles in Markdown and when you execute your static site generator, it will compile all your posts from your directory into individual static files using a template, which can then be served to your visitors.

For example, let's say you have a markdown file named <mark>hello-world.md</mark> and you wrote your content:

```markdown
title: Hello World
date: 2019-03-01 20:00

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sollicitudin dui, 
pulvinar vulputate nibh. Cras eu nunc mauris. Vestibulum quis diam at diam feugiat semper vitae at sem. 
Mauris in orci iaculis mauris semper gravida at nec augue. Phasellus luctus accumsan velit, 
in molestie odio luctus at. Curabitur neque erat, pretium vitae condimentum placerat, sodales eu 
nisi. Cras pretium nulla ac est interdum, vitae tempor mauris ornare. 
Nullam tortor nisi, scelerisque vel purus id, dictum finibus erat. Nulla tincidunt egestas 
sodales. Sed sit amet elit placerat, pellentesque est in, bibendum enim. Nam dolor lorem, venenatis sit 
amet sem at, sagittis feugiat risus. Fusce turpis felis, sodales a tortor vitae, volutpat semper 
justo. Donec porta id mi non porttitor. Fusce id est sit amet leo consectetur consequat.
```

Also, this is your template:
```html
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
    <div>Published on: {{ date }}</div>
    {{ content }}
    </body>
</html>
```

And when you execute the application, this is what happens:
```html
<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
    <div>Published on: 2019-03-01 20:00</div>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut sollicitudin dui, 
    pulvinar vulputate nibh. Cras eu nunc mauris. Vestibulum quis diam at diam feugiat semper vitae at sem. 
    Mauris in orci iaculis mauris semper gravida at nec augue. Phasellus luctus accumsan velit, 
    in molestie odio luctus at. Curabitur neque erat, pretium vitae condimentum placerat, sodales eu 
    nisi. Cras pretium nulla ac est interdum, vitae tempor mauris ornare. 
    Nullam tortor nisi, scelerisque vel purus id, dictum finibus erat. Nulla tincidunt egestas 
    sodales. Sed sit amet elit placerat, pellentesque est in, bibendum enim. Nam dolor lorem, venenatis sit 
    amet sem at, sagittis feugiat risus. Fusce turpis felis, sodales a tortor vitae, volutpat semper 
    justo. Donec porta id mi non porttitor. Fusce id est sit amet leo consectetur consequat.
    </body>
</html>
```

The generator just parsed your article on Markdown and put the details on the template and tada, the article is generated. Easy peasy!

The next step is to deploy it, I wrote a bash script to deploy all static files via FTP onto my server.

It's a simple but powerful idea and gives me a lot of flexibility to create my future blog posts with each having a different look (not always, but sometimes).

## Refreshed look, Creative energy
Although, the old one was good and minimal, something felt empty about it and I decided to change it.

I experimented with different fonts and chose Fira Sans as the blog's primary font. As for colors, I took inspiration from Dropbox's recent change in branding and they combined various colors to create dynamic elements to their brand.

So, I wrote a pattern generator on Javascript that would create a background image for every blog post and make it look colorful (See above).

<figure>
    <img src="https://cdn-images-1.medium.com/max/2600/1*-egs-meZ08WEmAhlwa481Q.png"/>
    <figcaption>“Floating Lines in the DeepSpace”. A generative artwork by Miguel Neto & Rodrigo Carvalho.</figcaption>
</figure>

Also, I have been exploring the concept of Generative Art, I found it really interesting especially it's creative and mathematical aspect. I have plans on replacing these colorful patterns with the random generative artworks, after all, I don't aim to make it look boring.

## Discovery and Experimentation
I have been working on some side projects like Pac-Man clone, a text-editor based on C and a terminal-based to-do list application on Linux, learning and customizing VIM, tinkering with Vagrant boxes, Capture-The-Flags challenges, experiments with UI frameworks like ReactJS and so much more.

## Hang in there, it's not over!
It's a work-in-progress and I'm trying to make my blog to be more creative, interactive and colorful.

I will be hosting a separate section called ***"Projects"***, which is currently under the works, it will contain all of my projects, UI/UX components to play around with, games and much more. I hope it will be the coolest section of this blog.

Hope you liked reading this article and the new changes!

Peace Out!