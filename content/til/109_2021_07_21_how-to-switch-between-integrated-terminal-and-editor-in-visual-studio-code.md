title: How to switch between integrated terminal and editor in Visual Studio Code?
date: July 21st, 2021
slug: how-to-switch-between-integrated-terminal-and-editor-in-visual-studio-code
category: VSCode
status: active

While, I'm trying to adjust myself to using Visual Studio Code, I found it quite annoying that there isn't a shortcut to switch focus between the editor and the integrated terminal. For a guy, like me, who makes use of the keyboard all the time, that's pretty important.

I did some research and found a way on how to do it. Just type `Ctrl+Shift+P` and type `Open Keyboard Shortcuts` and add these lines:

```json
[
    {"key": "ctrl+`", "command":"workbench.action.terminal.focus"},
    {"key": "ctrl+`", "command":"workbench.action.focusActiveEditorGroup", "when": "terminalFocus"},
]
```

Save the file and now, you'll be able to switch between the two by pressing <code>Ctrl+`</code> keys.

Hope you found this tip useful!