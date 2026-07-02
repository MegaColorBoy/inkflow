title: Accessing WAMP Server from other computers on LAN
date: September 13th, 2020
slug: accessing-wamp-server-from-other-computers-on-lan
category: Apache + WAMP
status: active

Whenever you develop a website using the **LAMP** or **WAMP** stack, you'll want to access the website, locally, via different systems and devices solely for testing purposes.

## Modify your VirtualHosts configuration
Setting up your WAMP Server for LAN access only requires you to tweak your **VirtualHosts** configuration file found in `C:\wamp64\bin\apache\apache2.4.41\conf\extra\httpd-vhost.conf`

```apache
<VirtualHost *:80>
  ServerName example.test
  ServerAlias example.test
  DocumentRoot "c:/wamp64/www/yourprojectname"
  <Directory "c:/wamp64/www/yourprojectname/">
    Options +Indexes +Includes +FollowSymLinks +MultiViews
    AllowOverride All
    Require all granted
  </Directory>
</VirtualHost>
```

Oh, if you're using Linux, you'll find the file `000-default.conf` in `/etc/apache2/sites-available` directory.

## Update your hosts file
If you type the URL of the website that you want to visit, the computer will first refer to the `hosts` file and then it'll go out to fetch DNS information. So, if you want `http:\\example.test` url to point to your local system, you just have add it in your `hosts` file:

Open the hosts file(`C:\Windows\System32\drivers\etc\hosts`) using a text editor and add this line to your `hosts` file:
```text
127.0.0.1   example.test
```

Once done, save the file and restart your WAMP Server and you're all set to go!

Hope you found this tip useful!