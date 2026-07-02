title: Using SSH with a private key
date: May 25th, 2020
slug: ssh-with-private-key
category: Terminal

Got a *.pem* key but don't know how to SSH to your server, just do this:
```bash
ssh -i name_of_key user@domain -p 22
```

## BONUS: Convert .ppk to .pem key

Recently, I started working from home and as a programmer, it's pretty common to access the company server for development purposes. 

Back in the office, I used to access it using [PuTTY](https://www.putty.org) but now that I'm using a linux machine, I thought of accessing it via Terminal but there's a catch, I can't use *.ppk* key to access it.

So, I did a little research and figured that I can easily convert it using `puttygen`

Open up your terminal and type:
```bash
sudo apt install putty-tools
```

Now, convert your private key to PEM format:
```bash
puttygen yourprivate.ppk -O private-openssh -o your_new_key.pem
```

That's it and you're good to go!