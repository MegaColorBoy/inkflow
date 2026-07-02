title: Temporarily disable IPV6 protocol on Ubuntu
date: November 27th, 2022
slug: temporarily-disable-ipv6-protocol-on-ubuntu
category: DevOps + Linux + Ubuntu
status: active

Few days ago, I resolved an issue that I faced on an Ubuntu server that was related to SMTP not working, as a result, the server was always throwing a `504 Gateway Timeout` error.

During troubleshooting, I found out that `telnet smtp.office365.com 587` was not giving any response and thought that the port was blocked on the client's network but no, it wasn't.

I did a little digging and learnt that it could be due to the fact that SMTP traffic over IPV6 might be blocked on the client's network.

So, I tried executing the following commands to disable IPV6 temporarily:

```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
```

And voila, the mails were going and SMTP traffic was working over IPV4.

If you want to enable it again, try the following:

```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0
```

Hope you found this tip useful!
