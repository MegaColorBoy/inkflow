title: Enable HTTPS/SSL on WAMP Server
date: September 13th, 2020
slug: enable-httpsssl-on-wamp-server
category: Apache + WAMP
status: active

Building a website with HTTPS/SSL in mind can help resolve a lot of problems when you're going to deploy it on production server.

So, here's a small tutorial on how to enable HTTPS mode and install SSL certificate on your local WAMP Server.

**Note: This tutorial assumes that you have a Windows PC and have installed WAMP Server 3.2.0 in your local system, if not, [download it from here](https://www.wampserver.com/en/).**

## Download OpenSSL
Based on your system's architecture, you can download either a 32 or 64-bit installer. You can find the latest version of OpenSSL from here. While installing, please make sure all the options selected are default.

## Generate SSL Key and Certificate
Open your terminal or command-line prompt and navigate to the following folder:
```bash
cd "C:\Program Files\OpenSSL-Win64\bin"
```

Next, you need to create a private key. While generating a private key, you'll have to enter a passphrase, it can be anything but make sure that you can remember it for the next step &#x1F602;.

Execute the following command:
```bash
openssl genrsa -aes256 -out private.key 2048
```

Good, now let's generate our certificate and in this step, you'll be prompted with several questions. You can fill as per your wish or just hit "Enter" to leave it as default. The only thing that matters is **Common Name** and this should named as `localhost`

Execute the following command:
```bash
openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -days 36500
```

## Move the certificate and key to Apache's directory
Create a folder named `keys` and move both `private.key` and `certificate.crt` to this directory: `C:\wamp64\bin\apache\apache2.4.41\conf`.

## Modify your httpd.conf file
You have to uncomment 3 lines from `C:/wamp64/bin/apache/apache2.4.41/conf/httpd.conf`:
```apache
LoadModule ssl_module modules/mod_ssl.so
Include conf/extra/httpd-ssl.conf
LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
```

## Modify your httpd-ssl.conf file
Go to `C:/wamp64/bin/apache/apache2.4.41/conf/extra/httpd-ssl.conf` and modify the following parameters:
```apache
DocumentRoot "c:/wamp64/www"
ServerName localhost:443
ServerAdmin admin@youremail.com
ErrorLog "${SRVROOT}/logs/error.log"
TransferLog "${SRVROOT}/logs/access.log"
SSLSessionCache "shmcb:${SRVROOT}/logs/ssl_scache(512000)"
SSLCertificateFile "${SRVROOT}/conf/keys/certificate.crt"
SSLCertificateKeyFile "${SRVROOT}/conf/keys/private.key"
CustomLog "${SRVROOT}/logs/ssl_request.log"
```

`DocumentRoot` is the location of where your website files are located. `ServerName` can be anything but preferable to use `localhost`.

## Restart your WAMP Server
Just restart your WAMP Server for the changes to take effect. If the WAMP icon turns green, you're good else, an typo or syntax error must have occurred.

Hope you found this tutorial useful! &#x1F600;