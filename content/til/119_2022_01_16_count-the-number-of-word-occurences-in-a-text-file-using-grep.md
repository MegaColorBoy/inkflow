title: Count the number of word occurences in a text file using grep
date: January 16th, 2022
slug: count-the-number-of-word-occurences-in-a-text-file-using-grep
category: Terminal
status: active

If you are using a GUI based application like Microsoft Word of Google Docs, it would be easier for you to know the number of word occurences in a file. But what if you are in a terminal? That's where both `grep` and `wc` comes handy tools.

Let's say you have the following text:

```text
The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary.
```

Now, you can use the `grep` and `wc` tool to count the number of times `"the"` appears in the file:

```bash
grep -o -i "the" file.txt | wc -l
```

Hope this helps you out!
