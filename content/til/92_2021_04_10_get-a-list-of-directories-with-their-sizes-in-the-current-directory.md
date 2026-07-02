title: Get a list of directories with their sizes in the current directory
date: April 10th, 2021
slug: get-a-list-of-directories-with-their-sizes-in-the-current-directory
category: UNIX
status: active

If you want to sizes of each directory in a list, try the following command:

```bash
du -sh * | sort -h >> directories-sorted.txt
```

And, if you wanted to find the directory that takes consumes a lot of space in your directory, you can try this:

```bash
du -sh * | sort -h | tail -n 1
```

Hope these tips do come in handy! &#x1F60A;