title: Webscraping with Python
date: 7th February, 2020
slug: webscraping-with-python
category: Tutorial
summary: Learn to extract data from multiple websites by creating a bot using Python.
status: inactive

*Note: The commands used in this tutorial are for users with UNIX based operating system and if you're a Windows user, please download and install Git for Windows.*

One day, I was having a conversation with a friend of mine and he told me something along the lines of *I scrape websites for my company and collect data*, so I was a bit curious and looked up online and thought of exploring this interesting concept by writing my own webscraping bot using Python.

The term **webscraping** might sound easy but it's actually hard, regardless of whatever technology you use. Why is that? Because different websites are made by different developers with different skills using different technologies. Damn, that's a lot of differents' in one sentence.

In today's article, you'll learn about the concepts of webscraping and to build your own webscraping bot that scrapes for reviews from [Goodreads](https://www.goodreads.com) using the Scrapy framework.

## Prerequisites
Though, it's not necessary to be expert but it's recommended that you're familiar with the following concepts and technologies:
- HTTP requests
- JSON objects
- HTML DOM elements
- Programming with Python

## What is webscraping?
It's the process of extracting data from websites that is carried out by a webscraper that passes **GET** requests, parses the DOM elements in the HTML document and converts into a JSON, CSV or XML file format.

## What is it used for?
In a nutshell, it's main purpose serves to collect data and store it in a database to generate reports, sales leads, forecasts and much more that allows businesses to target customers and clients to market their products.

Another advantage is that if you're into machine learning, you'll realize that having a skill like this could come in handy.

## Is it challenging?
Well, it depends but mostly yes. I'd like to share a recent story:

I landed a freelance gig from a company that wanted scrape information about doctors from various hospitals that reside in the Middle East region. Thankfully, I was provided a list of websites that were targeted by the company.

It's at this point that I learnt that writing one webscraping bot can't be a "fits-for-all" solution because of the following challenges:

## Let's build our own webscraper
In today's article, we'll be building a simple web scraper that fetches data from [Goodreads](https://www.goodreads.com) using Python and Scrapy, a framework that makes it easier to scrape websites.

### Setting up the environment
This tutorial assumes that you have Python and it's dependencies installed in your system. If you don't have it installed, [click here](https://lmgtfy.com/?q=how+to+install+python) for more information.

### Install virtualenv
*This step is optional and you can skip it, if you wish to do so.*

We'll be installing a few extra libraries and dependencies on your system. If you don't want to mess up your current setup, you can set up an isolated environment using <mark>virtualenv</mark>, this will allow you to install all of your Python libraries, locally, instead installing them globally.

Write the following command in your terminal:
```bash
    pip install virtualenv
```

Once you've installed it, you can create a virtual environment by typing the following:
```bash
    virtualenv venv
    source venv/bin/activate
```

Voila, you've successfully created a virtual environment for your project. You can close the environment by simply typing the following:
```bash
    deactivate
```        

### Install scrapy framework
Type the following command to install scrapy in your system:
```bash
    pip install scrapy
```

## Hello, world!
Let's start by writing a basic spider that extracts HTML content of multiple pages that belongs to the GoodReads website.

### Create a new project
Create a new project named <mark>test_project</mark> by typing the following in your terminal:
```bash
    scrapy startproject test_project
```

### Write a basic spider class
Create a new file named "test.py" in the <mark>spiders</mark> folder of your project directory and copy-paste the following code:

```python
    import scrapy

    class GoodReadsSpider(scrapy.Spider):
        name = 'goodreads_spider'

        def start_requests(self):
            urls = [
                'https://www.goodreads.com/quotes?page=1',
                'https://www.goodreads.com/quotes?page=2',
                'https://www.goodreads.com/quotes?page=3'
            ]

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            page_number = response.url.split('=')[1]
            html_file = "{0}.html".format(page_number)
            with open(file, "wb") as f:
                f.write(response.body)
```

The above code is divided into 3 parts:

1. Identity
2. Requests
3. Response

#### Identity
The <mark>name</mark> variable is assigned a name that is used to identify the Spider. This name is unique and can't be used for different Spiders.

#### Requests
This reminds me of quote said by Stevie Wonder:

>If you don't ask, you don't get.

Yes, I'm talking about HTTP requests, a large part of web scraping involves passing GET and POST requests to a web server.

According to [Scrapy's documentation](https://docs.scrapy.org/en/latest), you need to define a method named <mark>start_requests()</mark> that'll return a list of requests for which the spider will begin to crawl from.

#### Response
The <mark>parse()</mark> method is called to handle the requests and download the requested response, in our case, it'll be just the HTML content of a webpage.

To execute the Spider, type the following:
```bash
    scrapy crawl goodreads_spider
```

After it's complete, you should be able to see 3 HTML pages in your project directory.

Before we complete the Spider, let's dive into a few concepts, shall we?

## XPath selectors
Just like CSS selectors, XPath is a query language used by webscrapers to select nodes in HTML webpages. It's syntax is similar to traversing files in the terminal, like this:

```xml
    div[class="someclass"]/span/p/text()
```

The version of XPath goes upto 3.1 but most browsers and scrapers support version XPath 1.0.:

### Terminology

### Syntax

### Axes and Predicates

## Completing the Spider

### Pagination

### Items and Item Loader

### I/O Processors

## The Crawler

## Avoid ban and robots.txt

## Conclusion

