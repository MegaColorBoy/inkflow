title: Using zipcloak to encrypt files within an archive
date: July 7th, 2020
slug: using-zipcloak-to-encrypt-files-within-an-archive
category: Linux
status: active

Whenever you're sending a bunch of files or an archive that contains sensitive or confidential information, it's wise to encrypt before you send it to the person that you intend to.

Using `zipcloak`, you'll be able to encrypt files within your existing archive.

Do the following after you've [created a zip archive](til/posts/zip-a-file):
```bash
zipcloak files.zip    
```
Now, you'll be prompted twice to enter a new password and verify your entered password. If they match, your archive will get encrypted. So whenever, you try to unzip or open using an Archive Manager, you'll be prompted to enter the password or else, you won't be able to access it.

You also have the choice of not encrypting the original archive and creating a new one instead, just like this:
```bash
zipcloak files.zip -O encrypted.zip    
```

On the other hand, if you do wish to remove the encryption from your archive, just type the following:
```bash
zipcloak -d files.zip
```
And you'll be prompted again to enter your password before it removes it's encryption.

Hope this helps you out! &#x1F601;