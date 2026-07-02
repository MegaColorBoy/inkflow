title: Convert IIS web.config to Apache .htaccess using Javascript
date: February 24th, 2018
slug: convert-iis-webconfig-to-apache-htaccess-using-javascript
category: Programming
summary: Last week, I built a small tool that converts IIS web.config to Apache .htaccess using Javascript

Last week, I was migrating my company's website from our in-house IIS
Virtual Private Server to a Dedicated Apache Server in order to improve
the website's overall performance and handle more traffic efficiently.
For those of you who have hosted a website using Microsoft's IIS
Manager, you'll know that it makes use of an XML document named
***web.config*** file, whereas in an Apache Server, it's an ***.htaccess***
file, which is also used to store rules to write clean and friendly
URLs.

Converting from ***.htaccess*** to ***web.config*** is easy as it's a matter
of importing the rules directly on IIS Manager's ***URL Rewrite*** module
but doing the other way around was also possible but only if you did it
manually and I really don't want to waste time on such mundane tasks.

## How did I convert it?

A little bit of [Regular
Expressions](https://en.wikipedia.org/wiki/Regular_expression), a dash
of Javascript and an understanding on how Apache's ***mod_rewrite***
works, I decided to build a tool that converts ***web.config*** to
***.htaccess*** format.

**How to use this converter:**

+ Paste your ***web.config*** XML code on the textfield
+ Hit ***"Convert"*** to convert to ***.htaccess*** format
+ Please use a valid XML format before converting your code

<!-- DEMO -->

<div id="js-code"></div>
<script defer src="/static/projects/iis-to-apache/script.js" type="text/javascript"></script>
<!-- DEMO -->

**Code snippet:**

```js
//web.config to .htaccess converter
function webConfigToHtaccess()
{
    
    // Take input from textarea
    // and parse it into XML
    
    var xml = $("#webconfig-xml").val(), 
    xmlDoc = $.parseXML(xml), 
    $xml = $(xmlDoc);

    
    // - Inside each "rule", look for the "action" child node
    // - If it contains multiple parameters, follow the 
    // regular expression pattern: /{R:(d{1})}/
    // - Replace that pattern with a dollar sign and it's parameter
    // - Append "RewriteRule" along with the url and it's rules
    
    $xml.find('rule').each(function(){
        var str = $(this).find("rule>action").attr('url');
        var regex = /{R:(d{1})}/;
        while(regex.test(str))
        {
            str = str.replace(regex, '$' + RegExp.$1);
        }

        $("#htaccess-code").append("RewriteRule " + $(this).find("rule>match").attr('url')
            + " " + str + "<br>"
        );
    });
}
```

Although, I can't really say that it's perfect because I had to make
some changes but hey, it's just minor changes and yes, it did save me a
lot of time!

Hope you found this article useful!