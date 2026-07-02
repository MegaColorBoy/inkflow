title: How to change the character encoding of a file via Terminal?
date: April 10th, 2021
slug: how-to-change-the-character-encoding-of-a-file-via-terminal
category: UNIX
status: active

Sometimes, I face character encoding issues while making minor edits via a SFTP console connected to a Linux server. I found a quick hack to change the file encoding using `vim` on the command line.

In this example, I'm changing the encoding of the file to `unix`:

```bash
vim $filename +"set ff=unix" +wq
```

Hope you found this helpful!