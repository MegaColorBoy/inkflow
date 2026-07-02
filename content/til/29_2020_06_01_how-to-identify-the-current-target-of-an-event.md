title: How to identify the current target of an event?
date: June 1st, 2020
slug: how-to-identify-the-current-target-of-an-event
category: JavaScript
status: active

Using the `event.currentTarget` property which belongs to the `Event` interface can help you in many ways to identify target of the current event especially if you want to fetch attributes or modify the classname of an element that belongs to a group of elements sharing the same classname.

There are many examples but I chose to write a small snippet of highlighting a tab:

```js
function highlightTab(e){
    // Find elements that has the classname 'active' 
    // and remove them
    if(document.querySelector('div.tab_item.active') !== null){
        document.querySelector('div.tab_item.active').classList.remove('active');
    }

    // Add active class to target node
    e.currentTarget.className += " active";
    
    // Add active class to target's child node
    // e.currentTarget.querySelector('a.child_anchor_link').className += " active";
    
    // Add active class to target's parent node
    // e.currentTarget.parentNode.className += " active";
}
```

Read [Mozilla's official documentation](https://developer.mozilla.org/en-US/docs/Web/API/Event/currentTarget) to know more about getting the current target of an event and it's compatibility with different web browsers.