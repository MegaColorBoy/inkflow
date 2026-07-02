title: Find a file by extension
date: May 25th, 2020
slug: find-file-by-ext
category: Terminal

This comes in handy whenever I want to look for files that exists with a specific extension in a computer or server:

```bash
find . -name "*.ext"
```

In addition, sometimes, you might want to look for a bunch of files with a specific extension but with matching keywords:

```bash
find .name "*.ext" | grep "keyword"
```

Hope you found this helpful!