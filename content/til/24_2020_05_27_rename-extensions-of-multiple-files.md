title: Rename extensions of multiple files
date: May 27th, 2020
slug: rename-extensions-of-multiple-files
category: Bash
 
In this example, we're going to change a list of `.txt` files to `.md` files:
```bash
#!/bin/bash

shopt -s nullglob
files=($(ls -v *.txt))

for file in "${files[@]}"
do
    mv ${file} ${file}.md
done
```
s
You can use modify this script to rename any extension you want.