title: Extract private key and certificate from .pfx file
date: March 12th, 2022
slug: extract-private-key-and-certificate-from-pfx-file
category: DevOps
status: active

Ever wondered what's a `.pfx` file? It's just a combination of both private key and the certificate and this file is usually used in Microsoft IIS Servers.

However, you can't use this file in Linux servers as both private key and the certificate are supposed to be individual files.

Here's how you can extract both private key and certificate files:

```bash
openssl pkcs12 -in file.pfx -nocerts -out privatekey.pem -nodes
openssl pkcs12 -in file.pfx -nokeys -out certificate.crt
```

Hope this tip helps you out!