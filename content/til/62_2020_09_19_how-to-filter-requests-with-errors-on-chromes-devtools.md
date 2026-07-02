title: How to filter requests with errors on Chrome's DevTools
date: September 19th, 2020
slug: how-to-filter-requests-with-errors-on-chromes-devtools
category: Chrome DevTools
status: active

Tired of trying to look for errors in DevTools by scrolling a long list of HTTP responses?

Open up your **Chrome DevTools** and hit the **Network** tab and then try filtering the responses by typing the `status-code` property in the filter box.

It comes in handy when you want to narrow down to a specific list of HTTP responses. For instance, if you're looking for responses with error 404, you can filter it by typing like this: `status-code:404`.

Another trick is, you can filter out the responses that you don't want to see by just adding a hyphen like this: `-status-code:200`.

Hope this tip helps you out!
