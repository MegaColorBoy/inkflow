title: Display list of files with their extension and file sizes
date: September 20th, 2021
slug: display-list-of-files-with-their-extension-and-file-sizes
category: Linux
status: active

Last month, I was trying to free up some space in my company servers and I realized that there were a lot of `.zip` files taking up a lot of space.

So, I wrote the following command to list files by their extension:

```bash
find . -iname \*.extension -exec du -sh {} \; &gt; file-list.txt
```

And later to determine which files are the largest, I executed this command to sort the list by file size:

```bash
sort -rh file-list.txt > newfile.txt
```

Hope this tip helps you too! &#x1F604;