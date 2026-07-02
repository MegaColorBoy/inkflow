title: Install PFX certificate on a Linux server
date: September 24th, 2022
slug: install-pfx-certificate-on-a-linux-server
category: DevOps + Linux
status: active

I would consider this as an extended post to my [previous post](https://www.megacolorboy.com/til/posts/extract-private-key-and-certificate-from-pfx-file/) that I had written six months ago.

A PFX Certificate usually contains the following in PKCS#12 format:

- The actual certificate.
- The private key to the certificate.
- The Intermediate authority certificate that ensures the trustworthiness of the certificate.

To extract all those files, here are the steps that I have documented:

<div class="post-notification warning">
    <h3><i class="ph-warning-light"></i> Note</h3>
	<p>If the .PFX file prompts you for a passphrase, please check with your project manager or client regarding this information.</p>
</div>

## Extract the Encrypted Private Key

```bash
openssl pkcs12 -in <filename.pfx> -nocerts -out encrypted.key
```

## Extract RSA Private Key

```bash
openssl rsa -in encrypted.key -out private.key
```

## Extract Certificate

```bash
openssl pkcs12 -in <filename.pfx> -clcerts -nokeys -out certificate.crt
```

## Extract Combined Chain Certificate (Optional)

```bash
openssl pkcs12 -in <filename.pfx> -cacerts -nokeys -chain | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > combined_chain_certificate.crt
```

Once you are done extracting all the required files, you can add the certificates like this:

### Apache configuration:

```bash
SSLCertificateFile /path/to/certificate.crt
SSLCertificateKeyFile /path/to/private.key

# Optional, if you have it, else skip.
SSLCertificateChainFile /path/to/combined_chain_certificate.crt
```

Test if it works:
```bash
apachectl configtest
systemctl restart httpd
```

### Nginx configuration:

```bash
# If you don't have a combined chain certificate:
ssl_certificate /path/to/certificate.crt;
ssl_certificate_key /path/to/private.key;

# If you have a combined chain certificate:
ssl_certificate /path/to/combined_chain_certificate.crt
ssl_certificate_key /path/to/private.key;
```

Test if it works:
```bash
nginx -t
systemctl restart nginx
```

Hope you found this tip useful.
