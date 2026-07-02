title: Quick Search for file in your workspace in Visual Studio Code
date: July 9th, 2021
slug: quick-search-for-file-in-your-workspace-in-visual-studio-code
category: VSCode
status: active

Recently, started using Visual Studio Code as I'm yet figure out a way to install Sublime Text on Void Linux (using it as my current daily driver).

I'm always used to looking for my files using keyboard shortcuts in Sublime Text and I was kind of surprised this feature isn't enabled by default in Visual Studio Code.

Anyway, after a little digging, I found out that adding this line to your `settings.json` file would allow you to look for files in your workspace:
```json
"search.useIgnoreFiles": false
```

And, now try `Ctrl+P` and you'll be able to search for your file(s) easily.

Hope you found this tip useful!