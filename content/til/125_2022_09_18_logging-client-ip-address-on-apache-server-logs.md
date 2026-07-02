title: Logging client IP addresses on Apache server
date: August 18th, 2022
slug: logging-client-ip-addresses-on-apache-server
category: DevOps + Apache
status: active

If you want to log the actual client IP address, you need to extract the `X-Forward-For` header from the request and in order to do that, you need to make a tiny edit in your `httpd.conf` file.

1. Go to `/etc/apache2/conf` or `/etc/httpd/conf` and open `httpd.conf` file.
2. Search for the string that starts with: `LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined`.
3. Modify the `%h` to `%{X-Forwarded-For}i`. Now, it should look like this: `LogFormat "%{X-Forwarded-For}i %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined`.
4. Test the config to ensure that there are no typos by typing: `apachectl configtest`.
4. Save and restart the service by typing: `systemctl restart httpd` or `systemctl restart apache2`.
5. In your terminal, type `tail -f /var/log/httpd/access.log` and you'll be seeing the client IP being logged in your logs.

Hope you found this tip useful!