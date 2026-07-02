title: UI Design Pattern: Edit-in-Place
date: March 24th, 2018
slug: ui-design-pattern-editinplace
category: User Interface + User Experience
summary: I implemented a design pattern that could help my team edit content on-the-fly instead of having to navigate through a sea of web pages in a separate portal.

Two weeks ago, I was thinking of making an improvement on my [company
website](https://www.kit.ae)'s custom-built Content Management System
(CMS) in order to make it easier for my team to edit and push content
with ease.

As a matter of coincidence, I came across a book named [Designing
Interfaces: Patterns for Effective Interaction
Design](http://www.designinginterfaces.com) by Jennifer Tidwell, which
contains several User Interface and Interaction Design patterns that
inspired me to implement one of the patterns that I had discovered in
the book, ***"Edit-in-Place"***.

## What's Edit-in-Place?

It's like a tiny WYSIWYG text-editor that allows users to change the
text directly on top of the original text instead of going through a
separate portal or dialog box.

## Why did I build it?

The fact that my team has to navigate through a sea of pages in the CMS
to edit content is annoying and sometimes, it could be just opening a
lot of new tabs on the browser. Hence, a feature like this would allow
them to edit content ***"on-the-fly"*** with zero navigation.

Below, I have made an implementation of it using Javascript and an
experimental design for my blog.

**How to use Edit-in-Place:**

+ Hover on top of any text element.
+ Double-click on the selected element.
+ Click ***Save*** to save changes.
+ Click ***Cancel*** to cancel changes.

<figure>
    <iframe width="500" height="1993" src="/static/projects/edit-in-place">
    </iframe>
</figure>

The book claims that ***Flickr*** is one of them who implemented this
feature, you can find this feature in most modern Content Management
Systems like Wordpress, Joomla or Drupal or a better example, you have
used this feature while renaming a file on your computer.

However, there are some limits to this i.e. you can only apply this
feature on dynamic webpages as you'll have to write a few additional
lines of ***AJAX*** that sends a ***POST*** request to your server to
reflect the saved changes on your database.

Hope you guys found this article useful!

## Credit

Icons used are from [www.flaticon.com](https://www.flaticon.com/) is licensed by [CC 3.0 BY](http://creativecommons.org/licenses/by/3.0/)
