title: Add search functionality to your static site
date: June 6th, 2020
slug: add-search-functionality-to-your-static-site
category: JavaScript
status: active

If you have a static site or a blog generated using a static-site generator but want to add a simple search functionality? This could be of your interest.

I'll take you through an example on how to build a simple search engine using a JSON file and AJAX requests.

## 1. Generate a JSON dump of your site
Although, it's not a database but it can act as an alternative to having one. Your JSON dump can contain any metadata that you wanted your users to search in your site. In my case, I thought of allowing the user to search `title` and `category`. 

Is your site generated using Python and want to create a JSON dump? [Read this article](til/posts/read-and-write-json-to-a-file-in-python) for more information.

## 2. Build search functionality
I won't go through the aspects of UI design in this article as I feel that it's subjective and depends on one's preferences but let's keep it simple enough for this tutorial.

Before you begin writing the function, place this component in your HTML template:
```html
<div class="searchbox">
    <input id="searchinput" type="text">
    <div id="searchresults">
        <ul></ul>
    </div>
</div>
```

Anyway, here's the function and you can place it directly on your template or in a separate `.js` file:
```js
var _url = "path-of-your-file.json";

$(document).ready(function(){
    $('#searchinput').keyup(function(e){
        var keyword = $(this).val();
        var code = e.keyCode ? e.keyCode : e.which;

        if(code == 13){
            $.ajax({
                url: _url,
                type: "GET",
                async: false,
            }).done(function(data){
                var results = "";
                if(data.articles.length > 0){
                    $.each(data.articles, function(key, value){
                        if(v.title.search(pattern) != -1 || v.category.search(pattern) != -1){
                            results += `<li><a href="${v.slug}">${v.title}</a></li>`;
                        }
                    });
                    $("#searchresults ul").html(results);
                }
            });
        }
    });
});
```
That's it! Now, when you execute your script, you should be able to view your search results just like as if it were using a database.

If you want to make it similar to mine, please feel free to inspect the code on the browser or go to my [repository](https://github.com/megacolorboy/personal-blog/blob/master/static/js/search.js) to see how it works.