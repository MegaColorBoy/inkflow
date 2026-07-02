title: Find your Public IP address using the Terminal
date: November 3rd, 2020
slug: find-your-public-ip-address-using-the-terminal
category: Linux
status: active

Previously, I used to determine my Public IP address on Google Search by typing ***"What is my IP?"*** and I was good with it.

Until, I thought of actually viewing it via the terminal itself. So, I wrote two lines of code in my `~/.bashrc` file:

```bash    
export myip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
alias myip="echo $myip"
```

Alternatively, you could try this too:
```bash
export myip="$(dig TXT +short o-o.myaddr.l.google.com @ns1.google.com)"
```

Save the file and apply your new configuration by typing the following command:
```bash    
source ~/.bashrc
```

That's it, now all you have to do is type `myip` in your terminal and it will display your Public IP address.

Hope you found this useful! &#x1F600;