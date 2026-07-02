title: Truncate a file using redirection in Linux
date: October 2nd, 2021
slug: truncate-a-file-using-redirection-in-linux
category: Linux
status: active

Simply put, sometimes, there are situations in where you just want to clear the contents of a file without deleting it.

This could be for many reasons like to avoid permission related issues, or maybe the file could be having useless logs that amasses to a size that measures in GBs.

So, the easiest solution is to clear it away from a terminal is by shell redirection like so:

```bash
:> filename
```

Let me break down the command here:

- The `:` symbol means `true` and doesn't produce any output.
- The '>' symbol is used for redirecting the output of the preceding command (in this case, it's empty!)
- `filename` is the file that you want to truncate. If it doesn't exist, the file will be created.

Alternatively, you can do the same by using the `cat` command to output the contents of the `/dev/null` device (which only contains a EOL character) to empty a file:

```bash
cat /dev/null > filename
```

Hope this comes in handy!