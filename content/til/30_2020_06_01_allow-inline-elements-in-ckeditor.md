title: Allow inline elements in CKEditor
date: June 1st, 2020
slug: allow-inline-elements-in-ckeditor
category: JavaScript
status: active

Using CKEditor is awesome but I hate it when it removes inline elements like `<span>`, `<i>` or any DOM elements that contain attributes like classnames or ID, by default.

Well, CKEditor's [documentation](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_allowed_content_rules.html) states that you can allow it by adding this line to your configuration:
```js
var editor = CKEDITOR.replace('textarea_edit',{
    allowedContent: true,
});
```
After adding this line, CKEditor will stop removing those elements from your HTML content but it's also open to all tags. 

You can set rules to allow only specific ones like this:
```js
var editor = CKEDITOR.replace('textarea_edit',{
    allowedContent: 'span; i; ul; li; a[!href]'
});
```
Hope this helps you out! &#x1F60A;
