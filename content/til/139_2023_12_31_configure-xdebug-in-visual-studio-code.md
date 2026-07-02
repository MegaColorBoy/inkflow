title: Configure XDebug in Visual Studio Code
date: December 31st, 2023
slug: configure-xdebug-in-visual-studio-code
category: VSCode + PHP + XDebug + Development
status: active

For the past 6 months, I've been writing code in C# 11 and .NET 7 Core and of course, using the amazing Visual Studio 2022 IDE was quite an amazing experience especially when it comes to debugging your code.

Recently, I had to switch back to classic ol' PHP and now, I wanted a similar debugging experience in Visual Studio Code.

Using XDebug and if configured correctly, it'll be quite useful in your debugging journey instead of using `var_dump()` or `dd()` your variables everytime.

## Prerequisites

The only thing you need here is Visual Studio Code and ensure that it's the latest version. I'm writing this from a Windows Machine using the latest version of WAMP Server.

## 1. Download PHP Debug

The official XDebug team has released an extension that could be installed in your editor. So, here you go, first [download it](https://xdebug.org/download).

## 2. Install XDebug

In the previous step, we just installed the extension for the editor but that's just an adapter used between the editor and XDebug.
Whereas, XDebug is a PHP extension that needs to be installed on your local system.

I'm not going to show you the installation process as this [documentation](https://xdebug.org/docs/install) explains that well enough and you can follow it based on your operating system of choice.

## 3. PHP Configuration

After you're done with installing the extension, open your `php.ini` file and add the following line in this file:

```ini
zend_extension=path/to/xdebug
```

Now, it's time to enable remote debugging. Depending on your XDebug version:

For XDebug `v3.x.x`:

```ini
xdebug.mode = debug
xdebug.start_with_request = yes
```

For XDebug `v2.x.x`:

```ini
xdebug.remote_enable = 1
xdebug.remote_autostart = 1
xdebug.remote_port = 9000
```

If you are looking for more specific options, please see read the [documentation on remote debugging](https://xdebug.org/docs/remote#starting). Please note that the default port in XDebug `v3.x.x` has been changed from `9000` to `9003`.

Once done, restart your PHP service and check if the configuration has taken effect. You can do this by creating a simple `test.php` with a `phpinfo();` statement in there and look for your XDebug extension under the **Loaded Configuration File** section.


## 4. Visual Studio Code Configuration

In your editor, hold <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> and type "Debug: Add Configuration" and it'll prompt you to select your language of preference and this case, of course, you should "PHP".

Upon selecting, it'll automatically generate a `launch.json` file in your `.vscode` folder in your project folder.

There'll be three different configurations in your file:

- Listen for XDebug: This setting will simply start listening on the specified port (by default `9003`) for XDebug.
- Launch currently open script: It will launch the currently opened script as a CLI, show all stdout/stderr output in the debug console and end the debug session once the script exits.
- Launch Built-in web server: This configuration starts the PHP built-in web server on a random port and opens the browser with the `serverReadyAction` directive.

Now, to test if it works, hit <kbd>F5</kbd> and add a breakpoint in your PHP code and if it lands on your breakpoint, that means it works fine.

Hope you found this article useful!

## References
- [PHP Debug for VS Code](https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug)
- [XDebug Installation Manual](https://xdebug.org/docs/install)