title: Install Microsoft SQL Server Driver for PHP on Amazon Linux 2
date: September 18th, 2022
slug: install-microsoft-sql-server-driver-for-php-on-amazon-linux-2
category: DevOps + PHP + AWS
status: active

Recently, I tried to install Microsoft SQL Server driver for PHP on Amazon Linux and searching on how-to do was really annoying.

I read a few articles on StackOverflow and found some samples on GitHub Gists and thought of sharing on how I installed it.

## Prerequisites
1. Amazon Linux 2 installed.
2. Ensure the ports 80 and 443 are open on your instance.
3. PHP >= v5.6 and the following extensions: `php-devel`, `php-pear`, `php-pdo`, and `php-xml`.
3. Know-how on using the terminal.

## Installation steps
These are the commands used to install the SQL Server driver:

```bash
sudo su
sudo yum-config-manager --add-repo https://packages.microsoft.com/config/rhel/7/prod.repo
sudo yum update
sudo ACCEPT_EULA=Y yum install -y msodbcsql mssql-tools unixODBC-devel re2c gcc-c++ gcc
sudo pecl install sqlsrv
sudo pecl install pdo_sqlsrv
```

## Modify php.ini
You can either to go to your `php.ini` file and add the `extension=sqlsrv` extension or add it like this:
```bash
echo "extension=sqlsrv" >> `php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"`
echo "extension=pdo_sqlsrv" >> /etc/php.d/30-pdo_sqlsrv.ini
```

## Restart the service
Ensure that the server can connect and restart the service:

```bash
sudo setsebool -P httpd_can_network_connect_db 1
sudo systemctl restart httpd && sudo apachectl restart
```

Next, run the following the command to see that both `pdo_sqlsrv` and `sqlsrv` are installed:
```bash
php -m | grep "sqlsrv"`
```

## Test if the driver works
Create a `test.php` file in your root directory and copy-paste this snippet to test if it works:

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$serverName = "YOUR_DB_HOST";
$connectionOptions = array(
    "Database" => "YOUR_DB_NAME",
    "Uid" => "YOUR_DB_USER",
    "PWD" => "YOUR_DB_PASSWORD"
);

$conn = sqlsrv_connect($serverName, $connectionOptions);

if($conn) {
    print "Connected successfully."; 
} else {
    print "Error while connecting to server.";
}
?>
```

Hope you found this tip useful!