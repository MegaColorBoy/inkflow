title: Find and remove duplicate lines using Regular Expressions
date: November 7th, 2020
slug: find-and-remove-duplicate-lines-using-regular-expressions
category: Regular Expressions
status: active

Open up your text editor and use the following RegEx pattern to find and remove the duplicate lines:

```text
^(.*)(\r?\n\1)+$
```

I found this technique on [Regular-Expressions.info](http://www.regular-expressions.info/duplicatelines.html) and I'm going to quote their explanation over here:

```text
The caret will match only at the start of a line. So the regex engine will only attempt to match the remainder of the regex there. The dot and star combination simply matches an entire line, whatever its contents, if any. The parentheses store the matched line into the first backreference.

Next we will match the line separator. I put the question mark into `\r?\n` to make this regex work with both Windows `(\r\n)` and UNIX `(\n)` text files. So up to this point we matched a line and the following line break.

Now we need to check if this combination is followed by a duplicate of that same line. We do this simply with `\1`. This is the first backreference which holds the line we matched. The backreference will match that very same text.

If the backreference fails to match, the regex match and the backreference are discarded, and the regex engine tries again at the start of the next line. If the backreference succeeds, the plus symbol in the regular expression will try to match additional copies of the line. Finally, the dollar symbol forces the regex engine to check if the text matched by the backreference is a complete line. We already know the text matched by the backreference is preceded by a line break (matched by `\r?\n`).

Therefore, we now check if it is also followed by a line break or if it is at the end of the file using the dollar sign.

The entire match becomes `line\nline` (or `line\nline\nline` etc.). Because we are doing a search and replace, the line, its duplicates, and the line breaks in between them, are all deleted from the file. Since we want to keep the original line, but not the duplicates, we use `\1` as the replacement text to put the original line back in.
```

Hope you found this tip useful!
