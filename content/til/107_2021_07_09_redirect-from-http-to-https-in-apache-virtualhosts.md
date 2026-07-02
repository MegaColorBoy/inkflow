title: Redirect from HTTP to HTTPS in Apache VirtualHosts
date: July 9th, 2021
slug: redirect-from-http-to-https-in-apache-virtualhosts
category: DevOps
status: active

Here's a simple technique on how I learned to redirect a site from HTTP to HTTPS automatically using Apache's VirtualHost configuration.

Go to your configuration file or `000-default.conf` and modify your configuration to something like this:
```bash
<VirtualHost *:80>
    ServerName your.domain.com
    Redirect permanent / https://your.domain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName your.domain.com
    SSLEngine On
    # insert code here...
</VirtualHost>
```

Save the file and check if the configuration is correct before your restart the server:
```bash
sudo apachectl configtest
```

If you get the message, `Syntax OK`, then go ahead and restart the server:
```bash
sudo systemctl restart apache2
```

Now, your visitors will be redirected from HTTP to HTTPS automatically!

Hope you found this tip useful!