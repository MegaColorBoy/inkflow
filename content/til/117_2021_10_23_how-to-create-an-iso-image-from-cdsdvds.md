title: How to create an ISO image from CDs/DVDs?
date: October 23rd, 2021
slug: how-to-create-an-iso-image-from-cdsdvds
category: Linux
status: active

I used to create ISO images using DAEMON Tools but I wanted to try something different and see if there's a way to create it using the Linux CLI.

Turns out, you can do in just a single line using the `dd` utility like so:

```bash
dd if=/dev/cdrom of=/path/to/your/directory/image.iso
```

The `if` stands for input file and `of` stands for output file.

Looks like, I don't have to use DAEMON Tools for stuff like this, I guess.

Hope you found this tip useful!
