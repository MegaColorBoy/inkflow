title: Configuring audio drivers in Arch Linux
date: June 20th, 2020
slug: configuring-audio-drivers-in-arch-Linux
category: Linux
status: active

Yesterday, I thought of testing my Arch Linux system's audio and turns out, I didn't even install it yet! &#x1F612;

Well, thanks to [ArchWiki](https://wiki.archlinux.org), it was simple enough to install to make the audio work on my old laptop. Just install the following packages:
```bash
pacman -S alsa-firmware alsa-lib alsa-utils
```

Reboot the system once you're done installing the packages. Depending on your window manager, you should be able to see your sound icon being active.

## Bonus: Bash script to control your volume from the terminal

In my current laptop, I still haven't mapped out the keys to control the audio volume, so I thought of writing a small method in my `.bashrc` file, so that I can control it from my terminal.

Open your favorite text editor and Add this method in your `.bashrc` file:
```bash
# simple volume control
volume(){
    x=5
    if [ $1 == 'up' ]
    then
        amixer set Master $x%+ &> /dev/null
    elif [ $1 == 'down' ]
    then
        amixer set Master $x%- &> /dev/null
    elif [ $1 == 'toggle' ]
    then
        amixer set Master toggle &> /dev/null
    fi
}
``` 
Save the file, close your edit and refresh your file by typing:
```bash
source .bashrc
```
Now, it should work when you type any of these commands:
```bash
volume up
volume down
volume toggle
```
Hope this tiny script helps you out! 
