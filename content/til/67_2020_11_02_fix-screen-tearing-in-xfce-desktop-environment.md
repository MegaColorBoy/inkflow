title: Fix screen tearing in XFCE desktop environment
date: November 2nd, 2020
slug: fix-screen-tearing-in-xfce-desktop-environment
category: XFCE+Linux
status: active

Yesterday, I decided to try XFCE desktop environment and boy, it's really faster than the GNOME desktop environment.

As soon as I started to play around with it, I noticed a good amount of [screen tearing](https://en.wikipedia.org/wiki/Screen_tearing) and to my surprise, I came to know that the XFCE environment is known to have such issues.

After a few minutes of research, I was able to fix it. Here are the steps:

**Note: This is done on Ubuntu 18.04 Bionic Beaver**

If you dont have the package `inxi` installed in your system, do it right now:
```bash
sudo apt install inxi
```

After you're done installing, type the following command to find out which graphics you're using:
```bash
inxi -G
```

If you're using an Intel Graphics Driver, you'll probably get something like this:
```bash
Graphics:  Card: Intel Device 5926
           Display Server: x11 (X.Org 1.19.6 ) driver: i915 Resolution: 1920x1080@60.00hz
           OpenGL: renderer: Mesa DRI Intel Iris Plus Graphics 640 (Kaby Lake GT3e) (KBL GT3)
           version: 4.6 Mesa 20.0.8
```
You can try go to **Settings Manager->Window Manager Tweaks->Compositor" and enable **Synchronize drawing to the vertical blank**. From [what I've read](https://techstop.github.io/fix-screen-tearing-xfce/), if you do that, it should stop but it didn't do anything for me.

If the above technique didn't work, go to `/usr/shar/X11/xorg.conf.d/` and create a file for your graphics card named `10-intel.conf`.

Copy-paste the following configuration into the file:
```bash
Section "Device"
  Identifier  "Intel Graphics"
  Driver      "intel"
  Option "TearFree" "true"
EndSection
```

Save the file, reboot your system and look for any screen tearing issues. If you didn't face any, that means it worked! &#x1F601;
