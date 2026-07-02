title: Built a new static site generator using Python 3.7
date: February 19th, 2021
slug: built-a-new-static-site-generator-using-python-37
category: Refactoring
summary: Thought of giving it some new upgrades and finally decided to open-source it.
status: active

Since [2019](/writings/posts/build-your-own-static-site-generator-using-python/), I always used a custom static site generator for the website. The previous one was written in Python 2.7 but ever since Python decided to [sunset](https://www.python.org/doc/sunset-python-2/) it, I decided to rewrite it using Python 3.7.

Unlike the previous one, it's quite flexible and I thought of giving it some new features that would help me maintain it with ease.

The new features I have added are:

- A neat CLI to build the entire site or certain parts of the website
- Able to switch between different templates 
- Archive mode
- Pagination
- Generates RSS Feeds and JSON files

## Why rewrite it again?
Over the past few months, I didn't really maintain my blog and when I visited the old codebase, I realized it wasn't flexible and it didn't have many features and it was slow, too.

Recently, I got new ideas of building different sections for the website and thus, is why I had the motivation to rewrite everything and make it modular and flexible enough to build a powerful yet simple custom static site generator.

## Have a look
I have decided to open-source my static site generator on my [GitHub repository](https://www.github.com/megacolorboy/megacolorboy-ssg) and I'm having plans of writing a new documentation for it, so that if people are interested, they could contribute or use it for their own personal uses.

## Conclusion
If you've been following my blog posts, you may know that I have a knack of displaying JavaScript widgets on some of my previous blog posts. Well, I've decided to rewrite all of those widgets, one-by-one, using ReactJS and hopefully, write more tutorials for each of them.

Hope you liked reading this article.
