title: Generate CSR with multiple subdomains using OpenSSL
date: December 31st, 2023
slug: generate-csr-with-multiple-subdomains-using-openssl
category: OpenSSL + SSL + CSR + DevOps
status: active

I have done this many times but I never got to write about it and I felt that I should write about it after I helped a friend of mine with this.

## Prerequisites

It doesn't matter which operating system you're going to do this on as long as you have `openssl` installed in your system, you should be fine.

All you have to do is just create a simple configuration file and give it a name like `multiple-domains.cnf`:

```ini
[req]
default_bits       = 2048
distinguished_name = req_distinguished_name
req_extensions     = req_ext

[req_distinguished_name]
countryName         = [COUNTRYCODE]
stateOrProvinceName = [STATE]
localityName        = [LOCALITY]
organizationName    = [ORGANIZATION]
commonName          = website.com

[req_ext]
subjectAltName = @alt_names

[alt_names]
DNS.1 = website.org
DNS.2 = wesbite.ae
DNS.3 = wesbite.co.uk
```

Save the file and copy-paste this into your command prompt or terminal:

```bash
openssl req -out <your-csr-name>.csr -newkey rsa:2048 -nodes -keyout <your-private-key-name>.key -config multiple-domains.cnf
```

Once executed, it should be generated for you and if not, verify your configuration file for any typos.

Hope this helps you out!