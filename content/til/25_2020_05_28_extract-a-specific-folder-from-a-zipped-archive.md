title: Extract a specific folder from a zipped archive
date: May 28th, 2020
slug: extract-a-specific-folder-from-a-zipped-archive
category: Terminal

First, you need to view what's inside of the `.zip` archive:
```bash
unzip -v archive.zip
```
Once, you've found the folder you wanted to extract, just type this:
```bash
unzip archive.zip "folder_to_extract/*" -d .
```
