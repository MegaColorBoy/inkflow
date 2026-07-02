title: Install TeamViewer on Fedora Linux 36/37
date: January 1st, 2023
slug: install-teamviewer-on-fedora-linux-3637
category: Linux + Productivity
status: active

If you are using Fedora Linux or any other Linux distribution and want a short guide on how to install TeamViewer on your workstation, then this article is for you.

Usually, I use it access remote servers or my computer at work but I myself never did it on a Linux workstation. It worked out for me, so it should work for you too!

## 1. Download TeamViewer RPM Package

You can find the [latest release](https://www.teamviewer.com/en/download/linux/) on TeamViewer's official site.

Make sure that you have install `wget` on your system to easily download it via the Terminal:
```bash
wget https://download.teamviewer.com/download/linux/teamviewer.x86_64.rpm
```

## 2. Download minizip module
During installation, it failed for me as I was missing a certain `libminizip.so` module. So, I looked up online and found the module and downloaded it on my workstation:

```bash
wget https://rpmfind.net/linux/fedora/linux/updates/36/Everything/x86_64/Packages/m/minizip-compat-1.2.11-33.fc36.x86_64.rpm
```

Once the download is complete, you can install it:

```bash
rpm -i minizip-compat-1.2.11-33.fc36.x86_64.rpm
```

## 3. Install TeamViewer

Now, the final step is to install the RPM package for TeamViewer:

```bash
rpm -i teamviewer_15.37.3.x86_64.rpm
```

Hope you found this short guide useful!
