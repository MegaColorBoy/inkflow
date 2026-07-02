title: Build your own Static Site Generator using Python
date: October 27th, 2019
slug: build-your-own-static-site-generator-using-python
category: Tutorial
summary: Are you curious enough to build your own Static Site Generator? This article is for you.

If you are curious about web development, you must have came across names like Jekyll, Hugo, Gatsby and more. These names that I mentioned are called Static Site generators. In fact, this website that you're on, is powered by a static site generator and I really like it so far.

In today's article, you'll learn how to build your own Static Site Generator using Python, create a blog and host it on Netlify for free. Please note, that this is a basic tutorial that would show the bare-metals of this generator.

These are the pre-requisities to this tutorial:

- Basic understanding of Python, Git, HTML and Markdown
- Basic knowledge of file I/O
- Know-how on using the command-line

If you don't know them, it's okay, you can still do your own research on Google and learn on-the-go!

Before we jump in, let's see why is it the latest craze!

## Why is it popular?
Take a blog, it's a dynamic web application that consists of a lot of sections like blog posts, archives and categories. Each time, a user visits a blog post, it sends a GET request to the server, fetches the data, then generates a webpage along with the fetched data on-the-fly. However, with a static site generator, you only serve pre-rendered files, so you don't have to generate or create anything on-the-fly, it's already there!

Apart from that, applications like a blog are usually database-dependant and you need to host it somewhere with a price. Not only that, but it does have security risks. With static site generators, you write your content on a markdown file and then convert it into static HTML files, which can then be used to host your website on services like GitHub Pages or Netlify for free and you don't have to worry about any security issues.

## What are the functionalities?
These are the functionalities that we'd require in a blog:

- Display all blog articles
- Pagination module
- A page for each article

So, let's go ahead and start with building the project.

## Time to build it!
Let's plan before we dive in straight into coding it. This is the file structure we'll be following in this tutorial:

### Create file structure
This is the file structure we're going to follow in this tutorial, so create it before you proceed with the tutorial.
```text
\blog-ssg
    \content
    \output
    \templates
    make_entry.py
    ssg.py
    ssglib.py
```

Next, install the following dependencies using <mark>pip</mark>:
```bash
pip install markdown2
pip install jinja2
```

### Generate markdown files
Go to your <mark>make_entry.py</mark> file and copy-paste this code. This will be used to generate markdown file for you to edit instead of having to create it manually all the time.

```python
import os, sys
from glob import glob
from datetime import datetime

# This is the Markdown template
TEMPLATE = """
title: {title}
date: {date}
slug: {slug}
category: Write category here.
summary: Write summary here.

Write content here.
"""

def suffix(d):
    return 'th' if 11<=d<=13 else {'1':'st', '2':'nd', '3':'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

# Generate file number by looking at the number blog articles in the directory
def gen_file_no(file_path, existing_files):
    """
        If no files are found,
        then this is the first file.
    """
    if not existing_files:
        return 1

    """
        Look for the biggest file number
        and return the bigger one
    """
    prefixes = [filename.replace(file_path,"")[:2] for filename in existing_files]
    biggest_prefix = max(prefixes, key= lambda n: int(n))
    return int(biggest_prefix) + 1

# Generate slug for the blog article
def gen_slug(title):
    title = "".join(x for x in title if x.isalnum() or x == ' ')
    title = title.lower().strip("").replace(' ','-')
    return title

# Create entry
def make_entry(title, file_type):
    if file_type == "articles":
        file_path = "content/" + file_type + "/"

        # Create folders if they didn't exist
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path))

        today = datetime.today()

        slug = gen_slug(title)
        file_no = gen_file_no(file_path, existing_files=glob(file_path + "*.md"))
        blog_file_path = file_path + "{:0>2}_{}_{:0>2}_{:0>2}_{}.md".format(file_no, today.year, today.month, today.day, slug)
        
        post_date = datetime.strptime(str(today.date()), '%Y-%m-%d')
        post_date = custom_strftime('%B {S}, %Y', post_date)

        t = TEMPLATE.strip().format(title=title,
            year=today.year,
            month=today.month,
            date=post_date,
            slug=slug)      

        with open(blog_file_path, 'w') as w:
            w.write(t)

        print blog_file_path

if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_entry(sys.argv[1], sys.argv[2])
    else:
    print "Enter blog title and article type"
```

To create a blog entry, just type this in your terminal:
```bash
python make_entry.py "Article Name" articles
```

### Create a library
This library must have the following functionalities:

- [Fetch content from Markdown files](#stub-1)
- [Create templates](#stub-2)
- [Generate index page](#stub-3)
- [Generate articles from Markdown to HTML](#stub-4)
- [Generate pagination module](#stub-5)
- [Generate blog](#stub-6)

So, create a new file named <mark>ssglib.py</mark> and let's do each of the functionality step-by-step to gain a deeper understanding of each method/function in the library.

Before that, add the following lines to the file:
```python
import os, random, sys
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
from argparse import Namespace

# Jinja2 Environment
env = Environment(loader=PackageLoader('ssg','templates'))
```

#### <a id="stub-1"></a> Fetch content from Markdown files
This method will fetch content from all of the Markdown files that resides in the <mark>content/articles</mark> folder.
```python
# Get Markdown files from content directory
def get_markdown_files(section):
    POSTS = {}

    file_path = 'content/'
    
    for md_file in os.listdir(file_path):
        md_file_path = os.path.join(file_path, md_file)

        # if it's not a directory, read it
        if not os.path.isdir(md_file_path):
            with open(md_file_path, 'r') as file:
                POSTS[md_file] = markdown(file.read(), extras=['metadata'])

    return POSTS
```

#### <a id="stub-2"></a> Create templates
You'll need to create two templates, one for home page and the other is for your articles. All templates will reside in the <mark>templates</mark> folder.

This is the template for the home page of your blog and you can name this as <mark>index.html</mark>:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <base href="/"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <main>
        <div class="posts-list">
            {% for post in posts %}
            <a href="posts/{{ post.slug }}/">
                <p>{{ post.date }} &mdash; {{ post.title }}</p>
            </a>
            {% endfor %}
        </div>

        <div class="paginator">
            {% if curr == 2 %}
                <a class="prev" href="/" rel="prev">Newer</a>
            {% elif prev != 0 %}
                <a class="prev" href="/pages/{{prev}}" rel="prev">Newer</a>
            {% else %}
                <a class="prev inactive">Newer</a>
            {% endif %}

            <p>{{curr}} <span>of</span> {{total}}</p>

            {% if next != 0 %}
                <a class="next" href="/pages/{{next}}" rel="next">Older</a>
            {% else %}
                <a class="next inactive">Older</a>
            {% endif %}
        </div>

    </main>
</body>
</html>
```

This is the template for the article page and you can name this as <mark>article.html</mark>:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Your name">
    <meta name="description" content="{{ post.summary }}.">
</head>
<body>
    <main class="article-main">
        <div class="article-info">
            <div>
                <h5>{{ post.category }}</h5>
                <h1>{{ post.title }}</h1>
                <p>{{ post.summary }}</p>
                <h6>Your name &mdash; {{ post.date }}</h6>
            </div>    
        </div>
        <article class="article-container">
            <div class="content">
            {{ post.content }}
            </div>
        </article>
    </main>
</body>
</html>
```

Though, this is just a bare-bone template, you can be creative and make your own changes to it by making it visually-appealing!

#### <a id="stub-3"></a> Generate index page
This method will create your index page. The index page will contain the links for each article.

```python
def index(POSTS, isPaginate=True):
    posts_metadata = get_posts_metadata(POSTS)
    if not isPaginate:
        template = env.get_template('index-alt.html')
        html_content = template.render(posts=posts_metadata)
        index_path = 'output/index.html'
        write_to_file(index_path, html_content.encode('utf-8'))
    else:
        args = {
            "template": env.get_template('index.html'),
            "posts_metadata": posts_metadata,

            # Keeps tracks the current post
            "curr_posts_index": 0,
            
            # Total number of posts
            "total_posts": len(POSTS),
            
            # Number of posts per page
            "posts_per_page": 8,

            # Directory to hold the pages
            "main_pages_path": "output/pages/"
        }
        pagination(args)
```

#### <a id="stub-4"></a> Generate articles from Markdown to HTML
This method will convert your Markdown content into HTML pages. One thing to note, each blog post will have it's own folder name with it's own slug and <mark>index.html</mark> file, so that it'll be easier to access the article.

```python
# Generate all posts
def articles(POSTS, post_template):
    for post in POSTS:
        post_metadata = POSTS[post].metadata
        post_data = {
            'content': POSTS[post],
            'slug': post_metadata['slug'],
            'title': post_metadata['title'],
            'summary': post_metadata['summary'],
            'category': post_metadata['category'],
            'date': post_metadata['date']
        }
        post_html_content = post_template.render(post=post_data)
        post_file_path = 'output/posts/{slug}/index.html'.format(slug=post_metadata['slug'])
        create_directory(post_file_path)
        write_to_file(post_file_path, post_html_content.encode('utf-8'))
```

#### <a id="stub-5"></a> Generate pagination module
Depending on the amount of blog articles you want to display, it will create ***total number of posts / article per page*** pages on the home page. They will look identical to the index page and these pages will be created in <mark>output/pages</mark> folder.
```python
# Pagination module
def pagination(args):

    x = Namespace(**args)

    # Number of pages (for pagination)
    num_pages = (x.total_posts/x.posts_per_page)
    
    # Create a page directory, if it doesn't exist
    create_directory(x.main_pages_path) 

    for pagenum in range(0, num_pages+1):
        # This will contain metadata of every x number of posts per page
        page_metadata = []
        page_path = ""
        curr_page = pagenum+1

        if curr_page == 1:
            page_path = "output/index.html" 
        else:
            page_path = "output/pages/{page}/index.html".format(page=curr_page)
        
        create_directory(page_path)

        # Internal counter to keep track of posts per page
        posts_counter = 0

        for j in range(x.curr_posts_index, len(x.posts_metadata)):
            page_metadata.append(x.posts_metadata[j])
            posts_counter = posts_counter+1

            # If it reached it's limit, break
            if posts_counter == x.posts_per_page:
                x.curr_posts_index = j+1
                break

        # Create links for previous and next pages
        prev_page = 0 if curr_page == 1 else curr_page-1
        next_page = 0 if curr_page == num_pages+1 else curr_page+1

        # Render the page
        html_content = x.template.render(
            posts=page_metadata, 
            curr=curr_page,
            prev=prev_page, 
            next=next_page,
            total=num_pages+1
        )

        write_to_file(page_path, html_content.encode('utf-8'))
```

#### <a id="stub-6"></a> Generate blog
This is the main function that will generate the entire blog including all of the article pages.
```python
# Generate blog -- Main function
def main(section):
    sections = ['articles']
    if section in sections:
        POSTS = get_markdown_files(section)
        if section == "articles":
            posts_template = env.get_template('article.html')
            index(POSTS, True)
            articles(POSTS, posts_template)
    else:
        print "This section doesn't exist."
```

Take a look at the source code for both <mark>ssglib.py</mark> and <mark>ssg.py</mark> and feel free to tinker around with it.

**Source code for** <mark>ssglib.py</mark>:
```python
#!usr/bin/python
import os, random, sys
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
from argparse import Namespace

# Jinja2 Environment
env = Environment(loader=PackageLoader('ssg','templates'))

# Write to file
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
        file.close()

# Create directory
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path))

# Get Markdown files from content directory
def get_markdown_files(section):
    POSTS = {}

    file_path = 'content/'

    for md_file in os.listdir(file_path):
        md_file_path = os.path.join(file_path, md_file)

        # if it's not a directory, read it
        if not os.path.isdir(md_file_path):
            with open(md_file_path, 'r') as file:
                POSTS[md_file] = markdown(file.read(), extras=['metadata'])

    return POSTS

"""
Collect metadata of all the posts
for home page and sort them 
in reversed order

@param: 
    POSTS => Dictionary
"""
def get_posts_metadata(POSTS):
    posts_metadata = []
    for k,v in sorted(POSTS.items(), reverse=True):
        posts_metadata.append(v.metadata)
    return posts_metadata

"""
    @params:
    POSTS => Dictionary
    template => jinja template
    isPaginate => boolean to enable pagination
"""
def index(POSTS, isPaginate=True):

    posts_metadata = get_posts_metadata(POSTS)

    if not isPaginate:
        template = env.get_template('index-alt.html')
        html_content = template.render(posts=posts_metadata)
        index_path = 'output/index.html'
        write_to_file(index_path, html_content.encode('utf-8'))

    else:
        args = {
            "template": env.get_template('index.html'),
            "posts_metadata": posts_metadata,

            # Keeps tracks the current post
            "curr_posts_index": 0,
            
            # Total number of posts
            "total_posts": len(POSTS),
            
            # Number of posts per page
            "posts_per_page": 8,

            # Directory to hold the pages
            "main_pages_path": "output/pages/"
        }

        pagination(args)

# Generate all posts
def articles(POSTS, post_template):
    for post in POSTS:
        post_metadata = POSTS[post].metadata
        post_data = {
            'content': POSTS[post],
            'slug': post_metadata['slug'],
            'title': post_metadata['title'],
            'summary': post_metadata['summary'],
            'category': post_metadata['category'],
            'date': post_metadata['date']
        }
        post_html_content = post_template.render(post=post_data)
        post_file_path = 'output/posts/{slug}/index.html'.format(slug=post_metadata['slug'])
        create_directory(post_file_path)
        write_to_file(post_file_path, post_html_content.encode('utf-8'))

# Generate pages
def pagination(args):

    x = Namespace(**args)

    # Number of pages (for pagination)
    num_pages = (x.total_posts/x.posts_per_page)
    
    # Create a page directory, if it doesn't exist
    create_directory(x.main_pages_path) 

    for pagenum in range(0, num_pages+1):
        # This will contain metadata of every x number of posts per page
        page_metadata = []
        page_path = ""
        curr_page = pagenum+1

        if curr_page == 1:
            page_path = "output/index.html" 
        else:
            page_path = "output/pages/{page}/index.html".format(page=curr_page)
        
        create_directory(page_path)

        # Internal counter to keep track of posts per page
        posts_counter = 0

        for j in range(x.curr_posts_index, len(x.posts_metadata)):
            page_metadata.append(x.posts_metadata[j])
            posts_counter = posts_counter+1

            # If it reached it's limit, break
            if posts_counter == x.posts_per_page:
                x.curr_posts_index = j+1
                break

        # Create links for previous and next pages
        prev_page = 0 if curr_page == 1 else curr_page-1
        next_page = 0 if curr_page == num_pages+1 else curr_page+1

        # Render the page
        html_content = x.template.render(
            posts=page_metadata, 
            curr=curr_page,
            prev=prev_page, 
            next=next_page,
            total=num_pages+1
        )
        write_to_file(page_path, html_content.encode('utf-8'))

# Generate blog -- Main function
def main(section):
    sections = ['articles']
    if section in sections:
        POSTS = get_markdown_files(section)
        if section == "articles":
            posts_template = env.get_template('article.html')
            index(POSTS, True)
            articles(POSTS, posts_template)
    else:
        print "This section doesn't exist."
```

**Source code for** <mark>ssglib.py</mark>
```python
import ssglib
from ssglib import (os, random, sys, datetime, 
Environment, PackageLoader, markdown)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        ssglib.main(sys.argv[1])
    else:
        print "Enter section name you want to generate."
```

To generate your blog, type the following in your command-line:
```bash
python ssg.py articles
```

Make sure you have a local HTTP server running on your computer, if you don't install this using NPM on your command-line:
```bash
npm i live-server
```

Alright, your blog is generated and now, it's time to launch it to the internet!

### Deploy project on Netlify
As I had mentioned in the previous article, I'm currently hosting my blog on Netlify. If you want to know more about it, [click here](/posts/migrating-to-netlify).

Let's go through the steps to deploying your blog:

#### 1. Create a GitHub repository
If you have a GitHub account, continue reading. If not, [go here](https://github.com).

Create a repository with any name you like and push all your files into the repository.

#### 2. Connect to Netlify
Create an account on Netlify.com and then connect to your GitHub account. After that, you have to select the repository that has your static files (Not the python code).

#### 3. Sit and Relax
At this stage, your blog will be deployed automatically and you'll be given a unique URL to view your website.

If you have a custom domain, I suggest you follow the instructions and make the necessary changes in the <mark>CNAME</mark> and <mark>A</mark> records.

Don't worry about the SSL certificate, it does take some time to activate, it took me like 7-8 hours to get it working.

## Conclusion
If you've completed this tutorial, give a yourself a pat in the back because now you know how static site generators work and you've built and hosted your own blog on the internet.

Hope you liked reading this article and please share it to others too!

Stay tuned for more!