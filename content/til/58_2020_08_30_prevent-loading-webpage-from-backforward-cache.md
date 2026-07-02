title: Prevent loading a webpage from Back-Forward cache
date: August 30th, 2020
slug: prevent-loading-webpage-from-backforward-cache
category: JavaScript
status: active

I'm working on an eCommerce project and I encountered a really weird problem, whenever I saved items into my cart and proceed to the checkout page and then go back to previous page, my cart isn't updated until I refresh the page.

Honestly, I thought this was a bug until I came around to learn about [Back-Forward Caching](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/1.5/Using_Firefox_1.5_caching) a.k.a **bfcache**, which allows the user to navigate between pages faster. That's a good thing, though!

But that didn't help resolve my issue, so I thought of going around with a tiny hack:
```js
window.onpageshow = function(event) {
    if (event.persisted) {
        window.location.reload() 
    }
};
```

The code above will look any persistence of the `onpageshow` event. Initially, it's set to `false` and if the page is loaded from **bfcache**, it'll set to `true`.

I wouldn't really consider this as a solution as it only worked on Safari instead of Chrome or Firefox.

But hey, it gets the job done! &#x1F602;