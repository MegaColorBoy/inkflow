title: Find directories created within a date range
date: April 10th, 2021
slug: find-directories-created-within-a-date-range
category: UNIX
status: active

Executing these commands helps me create a sorted list of files/directories created within a specific date range:

```bash
touch -t 202104100000 start
touch -t 202104150000 stop
find . -type d -maxdepth 1 -newer start \! -newer stop | sort >> directories.txt
```

Someday, these commands shall come in handy, bud! &#x1F60E;