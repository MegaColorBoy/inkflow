title: Find files containing specific text
date: May 25th, 2020
slug: find-files-specific-text
category: Terminal

This helped me a lot whenever I'm in a remote server trying to find a keyword or specific text amongst a bunch of files.

This command will save you a lot of time:
```bash
grep -rwn [path] -e 'pattern'
```

- `r` stands for recursion
- `n` displays the line number
- `w` matches the whole word

Refer to `man find` pages for more info.