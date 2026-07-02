title: Enable password asterisks for sudo on Fedora
date: May 14th, 2026
slug: enable-password-asterisks-for-sudo-on-fedora
category: Linux
status: active

After switching from Linux Mint to Fedora, one small difference I noticed was the password prompt behavior in the terminal. On Mint, `sudo` showed asterisks while typing the password. On Fedora, it stayed blank.

Some people prefer the blank prompt, but I like having visual feedback when typing, especially if I am not fully sure whether I missed a key.

If you want the same behavior on Fedora, you can enable `sudo` password feedback with a small `sudoers` change.

This note applies to `sudo` prompts in the terminal, not graphical login screens.

## 1. Open the `sudoers` file safely

Do not edit `/etc/sudoers` directly with a normal text editor. Use `visudo` so syntax errors are caught before the file is saved:

```bash
sudo visudo
```

## 2. Enable password feedback

Add this line:

```bash
Defaults pwfeedback
```

If you already have other `Defaults` lines such as `Defaults env_reset`, leave them as they are. Just add `Defaults pwfeedback` as a separate line.

## 3. Save and test

Save the file and exit the editor. Then run a `sudo` command again, for example:

```bash
sudo -k
sudo true
```

When prompted for your password, you should now see asterisks as you type. This setting makes password length visible on screen. If that matters in your environment, leave the default behavior in place.

Hope you found this article useful!