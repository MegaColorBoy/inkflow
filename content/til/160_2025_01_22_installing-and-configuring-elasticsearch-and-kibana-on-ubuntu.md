title: Installing and Configuring Elasticsearch and Kibana on Ubuntu
date: January 22nd, 2025
slug: installing-and-configuring-elasticsearch-and-kibana-on-ubuntu
category: Elastic Search + Kibana + Ubuntu
status: active

I've always wanted to write this article but never got the chance to do so, I had written some notes on how to set up Elasticsearch and Kibana on an Ubuntu server (20.04 or later). Whether you're building a search engine, analyzing logs, or just exploring the Elastic Stack, this guide will help you get everything up and running smoothly. 

Here's how I did it:

## Setting up Elasticsearch

### Add the Elasticsearch GPG key and repository

```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
```

### Install Elasticsearch

```bash
sudo apt update
sudo apt install elasticsearch
```

### Configure Elasticsearch by editing /etc/elasticsearch/elasticsearch.yml

```yaml
network.host: localhost
http.port: 9200
http.host: 0.0.0.0
```

### Start and enable Elasticsearch

```bash
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```

### Set up an NGINX reverse proxy for Elasticsearch

Add this server block to your NGINX config (e.g., `/etc/nginx/sites-available/your_domain`):
```nginx
server {
   listen 8834;

   # Uncomment for SSL
   # listen 8834 ssl;
   # ssl_certificate /path/to/certificate/crt.pem;
   # ssl_certificate_key /path/to/key/key.pem;
   # ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   # ssl_prefer_server_ciphers on;
   # ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

   server_name your_domain;

   location / {
      proxy_pass http://localhost:9200;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
   }
}
```

and then test and restart NGINX service:
```bash
sudo nginx -t
sudo systemctl restart nginx
```

Once done, you can verify if Elasticsearch is running by visiting `http://yourdomain.com:8834` in your browser. You should see a JSON response with Elasticsearch details.

## Setting up Kibana

### Install Kibana

```bash
sudo apt install kibana
```

### Configure Kibana by editing /etc/kibana/kibana.yml

```yaml
server.port: 5601
server.host: 0.0.0.0
elasticsearch.hosts: ["http://localhost:9200"]
```

### Start and enable Kibana

```bash
sudo systemctl enable kibana
sudo systemctl start kibana
```

### Create an admin user for Kibana

```bash
echo "your_admin_username:`openssl passwd -apr1`" | sudo tee -a /etc/nginx/htpasswd.users
```

Make sure that you enter a strong password when prompted.

### Set up an NGINX reverse proxy for Kibana
Add this server block to your NGINX config:
```nginx
server {
   listen 8833;

   # Uncomment for SSL
   # listen 8833 ssl;
   # ssl_certificate /path/to/certificate/crt.pem;
   # ssl_certificate_key /path/to/key/key.pem;
   # ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
   # ssl_prefer_server_ciphers on;
   # ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

   server_name your_domain;

   auth_basic "Restricted Access";
   auth_basic_user_file /etc/nginx/htpasswd.users;

   location / {
      proxy_pass http://localhost:5601;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection 'upgrade';
      proxy_set_header Host $host;
      proxy_cache_bypass $http_upgrade;
   }
}
```
and then test and restart NGINX service:
```bash
sudo nginx -t
sudo systemctl restart nginx
```

Once done, you can try to access Kibana by visiting `http://yourdomain.com:8833`. You'll be prompted for the admin credentials you created earlier.

## Wrapping Up

And there you go! Elasticsearch and Kibana are now up and running on your Ubuntu server, ready to help you search, analyze, and visualize your data. Whether you're diving into logs, building a search feature, or just experimenting with the Elastic Stack, this setup should give you a solid foundation.

## References

- [Burnham Forensics: NGINX for Kibana](https://burnhamforensics.com/2019/02/06/how-to-install-and-configure-nginx-for-kibana/)
- [ITNixPro: NGINX Reverse Proxy for Kibana](https://itnixpro.com/configure-nginx-reverse-proxy-for-kibana/)
- [DigitalOcean: Elastic Stack on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elastic-stack-on-ubuntu-22-04)

Hope you found this useful!