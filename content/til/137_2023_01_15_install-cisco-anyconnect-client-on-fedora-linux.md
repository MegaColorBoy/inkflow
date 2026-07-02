title: Install Cisco Anyconnect Client on Fedora Linux
date: January 15th, 2023
slug: install-cisco-anyconnect-client-on-fedora-linux
category: Linux + DevOps + Productivity
status: active

Cisco Anyconnect Client is a SSL VPN Client with VPN functionalites that enables an organization to secure its endpoints. Although, I use it a lot at office, I have only used it on Windows 10 so far.

One day, when I was on my vacation, I had to connect to a server remotely but this time, I tried doing it via Linux and it worked well!

## Download Cisco AnyConnect Client for Linux

Fortunately, the client is available for Windows, macOS and Linux.  You can go to the [Downloads](https://software.cisco.com/download/home/286281283/type/282364313/release/4.10.06079) page and download the tarball archive for Linux.

After downloading, you can extract the tarball file:
```bash
tar -xvf anyconnect-linux64-4.10.00093-predeploy-k9.tar.gz
```

## Install Cisco AnyConnect Client for Linux

Now that the file has been extracted, you can navigate to the `vpn` directory in `anyconnect-linux64-*` directory:

```bash
cd anyconnect-linux64-*/vpn/
```

Execute the `vpn_install.sh` script:

```bash
sudo ./vpn_install.sh
```

Follow the instruction steps and you're ready to use it.

## Connect to VPN via Terminal

The GUI version was crashing on both KDE and GNOME desktop environments. Whereas, it was a smooth experience when connecting via the Terminal.

For easy access, you can create an alias in your `.bashrc` file:

```bash
alias anyconnectvpn="/opt/cisco/anyconnect/bin/vpn"
```

Save and restart your terminal for the changes to take effect.

After that, you can connect to VPN like this:

```bash
anyconnectvpn -s connect <IP_ADDRESS>
```

Once executed, you'll be prompted to enter your credentials and if all goes fine, you should be connected.

## Disconnect VPN via the Terminal

You can execute the following command to disconnect:

```bash
anyconnectvpn -s disconnect <IP_ADDRESS>
```

## Configuring your VPN connection

Sometimes, it can be tedious to write these commands all the time especially when you're in a rush, this can really get in your way.

To solve that, you can easily store your credentials in a file like `.my_vpn_creds` in your home directory:

```bash
y
<username>
<password>
```

Save the file and create another file named `my_vpn_connect.sh`:

```bash
#!/bin/bash

VPN_SERVER="<IP_ADDRESS>"

echo "Connecting to VPN.."
/opt/cisco/anyconnect/bin/vpn -s  < ~/.my_vpn_creds connect ${VPN_SERVER}
```

Save the file and make the file executable:

```bash
sudo chmod +x my_vpn_connect.sh
```

Now, you'll be connected to the VPN automatically by just executing this script:
```bash
./my_vpn_connect.sh
```

This saved me a lot of time and I hope it does the same for you as well! 🤗

Hope you found this article useful!
