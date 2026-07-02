title: Connect to a Remote Windows machine from a Linux machine
date: January 1st, 2023
slug: connect-to-a-remote-windows-machine-from-a-linux-machine
category: Linux + Productivity
status: active

Last week, my Windows machine was down and I was struggling to connect to a remote server as I'm using Fedora Linux at home.

I tried installing and using GNOME Connections but it crashed and didn't work well for me. I found another tool named `rdesktop` which was stable and worked well for my case.

Installing it is as easy as typing the following command using the `dnf` package manager:

```bash
sudo dnf install rdesktop
```

Now, you can connect to your remote desktop machine using the following command:

```bash
rdesktop -d <domain> -u <username> -p - <ipaddress>
```

Upon execution of this command, you'll be prompted to enter the password and after that, you're all good to go!

Hope you found this tip useful!
