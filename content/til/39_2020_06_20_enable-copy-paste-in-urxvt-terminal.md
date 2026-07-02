title: Enable copy-paste clipboard in URxvt Terminal Emulator
date: June 20th, 2020
slug: enable-copy-paste-clipboard-in-urxvt-terminal-emulator
category: Linux
status: active

In my current Arch Linux installation, I decided to use a window manager called i3. It's really awesome and it comes with a really lightweight terminal emulator called **urxvt**. It's very minimal and I lked it but when I tried to copy-paste text from one terminal to another, I wasn't able to.

However, thanks to the internet, I did some research and figured a way out.

## 1. Install xClip
First, you need to ensure that you have installed the `xclip` package, which will be used to copy-paste text in the emulator.

Type the following command to install the package:
```bash
pacman -S xclip
```

## 2. Activate Clipboard using Perl
Now, you have to paste these custom commands into your `clipboard` file, which is found in `/usr/lib/urxvt/perl` directory:
```perl
# paste selection from clipboard
sub paste {
     my ($self) = @_;
     my $content = `/usr/bin/xclip -loop 1 -out -selection clipboard` ;
     $self->tt_write ($content);
}

# copy text to clipbard on selection
sub on_sel_grab {
     my $query = $_[0]->selection;
     open (my $pipe, '| /usr/bin/xclip -in -selection clipboard') or die;
     print $pipe $query;
     close $pipe;
 }
```

## 3. Modify your .Xresources
Add these keybindings to your `.Xresources` file:
```bash
URxvt.keysym.Shift-Control-V: perl:clipboard:paste
URxvt.iso14755: False
URxvt.perl-ext-common: default,clipboard
```

After adding it, refresh your `.Xresources` settings:
```bash
xrdb -merge .Xresources
```

Reboot your terminal and try selecting some text from your terminal using your mouse and paste it using `Ctrl`+`Shift`+`V` and it should work! 

That's it! Enjoy &#x1F603;
