title: How to identify which Linux distribution is running in your system?
date: October 2nd, 2021
slug: how-to-identify-which-linux-distribution-is-running-in-your-system
category: Linux
status: active

If you've read my [earlier post](/til/posts/check-ubuntu-version/), I was using Ubuntu, at that time, and I thought that was how you identify which distro is running in your system but using `lsb_release -a` is not always going to work as some distributions may not have it installed.

Try the following command to identify the distribution you are running in your system:

```bash
cat /etc/os-release
```

And you'll get the following output:
```bash
NAME="XXXX"
ID="XXXX"
DISTRIB_ID="XXXX"
PRETTY_NAME="XXXX"
```

Hope this helps you out!