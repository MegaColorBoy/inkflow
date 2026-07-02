title: Migrating to Netlify
date: September 14th, 2019
slug: migrating-to-netlify
category: Update
summary: My thoughts on why I made the switch and how it improves my workflow.

When I converted my website to a static site using a custom-built static site generator using Python, I came across topics like ***"Hosting your website on GitHub Pages"***. At the time, I thought that I didn't really need it because my website was hosted on [Hostinger](https://www.hostinger.in) and it pretty much had everything that I needed until it started to get on my nerves.

Recently, my blog had been facing a lot of issues such as my website would face random downtime, hosting prices wasn't consistent and the FTP service for it was really annoying.

So, I decided that I need to find a better hosting service for my blog.

## Exploring GitHub Pages
Setting up your website was pretty easy using GitHub Pages, all you have to do was create a repository named <mark>websitename.github.io</mark> and you're done.

Plus, unlike other hosting services, GitHub Pages hosts your website for free. That sounded like really amazing and it has really good security, caching and speed too.

However, it was my first choice and like every other free hosting services, it does come with a few drawbacks that didn't fit my requirements. GitHub Pages offers a bandwidth limit of ***1GB*** and it didn't have good custom domain support. Also, I read that it had weird caching issues once you commit your changes to your repository.

## Here comes, Netlify!
When I discovered Netlify, I was happy because it had free hosting, good custom domain support and a ***100GB*** soft bandwidth, which is really fitting my requirements.

According to Netlify:
>Make your site or web-app many times faster by bringing it closer to your users.

The cool thing is that your website is not only pushed to a single server but to a global network of CDN nodes that can handle operations like automatic caching, smart rewrite and redirect rules and yes, blazing, fast loading speeds.

Hosting your website on Netlify is simple as few clicks, all you have to do is upload your website on a Git repository then connect it to Netlify and it will deploy your website in less than 5 minutes.

Updating my blog is easier now as now I just have to push my new commits to my GitHub repo and Netlify would automatically deploy it. Goodbye, FTP!

## Configuring HTTPS and custom domain settings
Since I have a custom domain, I configured my domain to point to Netlify's load balancer IP address by changing the <mark>A</mark> and <mark>CNAME</mark> records in the DNS Zone editor. The HTTPS/SSL part was a bit annoying and it took some time, like 5-6 hours, but apart from that, it was a great experience in migrating to Netlify.

## Conclusion
In short, my blog's static files are hosted on GitHub and automatically deployed on Netlify for free. I do have some future plans, like trying to roll out a commenting engine and light/dark themes for the blog.

Hope you liked reading this article!

Stay tuned!