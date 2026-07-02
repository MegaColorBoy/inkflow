title: Generating custom snippets using Visual Studio Code
date: May 26th, 2024
slug: generating-custom-snippets-using-visual-studio-code
category: VSCode + Productivity
status: active

I've always wanted to write about this feature and I believe this is one of the most productivity hacks you can do to speed your work and worry-less about writing boilerplate code.

For example, if I wanted to write a piece of code that fetches a list of books asynchronously using JavaScript, I would have to type it or maybe copy-paste that stub from another file or project and edit it accordingly.
That's fine but when working on a large project or tight deadlines, it can be quite time-consuming if all you want is just a boilerplate code that's ready to begin with.

Here's how you can create your own snippet:

1. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>
2. Type **Configure User Snippets** and hit <kbd>Enter</kbd>
3. Select the language for which it should appear and hit <kbd>Enter</kbd>

Once done, a new tab will open up with simple instructions for you to get started with. The instructions are quite straight-forward and you can write something like this right below the note:

```json
{
	// Place your snippets for javascript here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
    "AJAX Get Method": {
        "prefix": "ajax-get",
        "body": [
            "$.ajax({",
            "\turl: '/',",
            "\tmethod: 'GET',",
            "\tdatatype: 'json',",
            "\tsuccess: (data) => {",
            "\t\tconsole.log(data);",
            "\t},",
            "\terror: (err) => {",
            "\t\tconsole.error(err);",
            "\t}",
            "});",
        ],
        "description": "A simple AJAX GET Method"
    }
}
```

Save the file and test if the snippet works fine by opening any file, in this case, open an empty `.js` file and type `ajax-get` and hit <kbd>Tab</kbd> at the end of the prefix. The generated snippet would look like this:

```javascript
$.ajax({
    url: '/',
    method: 'GET',
    datatype: 'json',
    success: (data) => {
        console.log(data);
    },
    error: (err) => {
        console.error(err);
    }
});
```

Learn more about generating snippets by reading the [documentation](https://code.visualstudio.com/docs/editor/userdefinedsnippets) about it.

Hope this tip helps you out!