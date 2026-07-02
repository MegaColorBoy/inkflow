title: Convert string from snake case to camel case
date: March 12th, 2021
slug: convert-string-from-snake-case-to-camel-case
category: VIM
status: active

Thought of sharing a simple regular expression that I use on VIM to convert **snake_case** letters to **camelCase** letters (see what I did there) &#x1F61C;

Here's the pattern for you to use:

```vim
:s/ \([a-zA-Z]\)/\u\1/g
```

Hope you found this tip useful!