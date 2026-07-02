title: Install MariaDB 10.3 on Void Linux
date: January 16th, 2022
slug: install-mariadb-103-on-void-linux
category: Databases
status: active

I tried to find a proper guide on how to install MySQL 8.0 on Void Linux but I couldn't really find any. So, I thought of installing MariaDB 10.3 on my laptop instead.

Don't worry about using MariaDB as it meets the same standard enterprised requirements as MySQL. The only difference is that MySQL belongs to Oracle and MariaDB is for people who wanted to get out of Oracle's hands.

Anyway, let's get started.

## Prerequisites

- Need to have root privileges in order to install packages.
- Basic know-how of Void Linux and it's `xbps` package manager.

Alright, go ahead and follow these steps one-by-one:

### 1. Install MariaDB

Type the following command to install the package:

```bash
sudo xbps-install -S mariadb
```


### 2. Initialize MySQL data directory

The following command will initialize a MariaDB data directory and create system tables in the MySQL database, if they are not present.

```bash
mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

The options used:

- `--user`: The login user name to use for running the `mysqld` process.
- `--basedir` The path to the MariaDB installation directory.
- `--datadir`: The path to the MariaDB directory.

To know more about it, you can refer to [MariaDB's documentation](https://mariadb.com/kb/en/mysql_install_db/).

### 3. Enable MySQL service

If you are used to Ubuntu or CentOS, enabling services in Void Linux is a bit different but quite simple. Once a process is symlinked, it will start on boot and restarts if it stops unless you stop the service deliberately.

Type the following command to enable the `mysqld` service:

```bash
sudo ln -s /etc/sv/mysqld /var/service/mysqld
```

### 4. Start MySQL service

Type the following command to start the `mysqld` service:

```bash
sudo sv start mysqld
```

To confirm, if the service is running, type the following:

```bash
sudo sv status mysqld
```

And you'll see something like this:
```bash
run: mysqld: (pid 15136) 1116s; run: log: (pid 15025) 1172s
```

### <a id="secure-mysql-installation"></a> 5. Secure MySQL installation

It's recommended to secure your installation, so type the following command:
```bash
sudo mysql_secure_installation
```

Once the command is executed, you'll be prompted with a few questions, respond according to your needs and you're done!

### 6. Test MariaDB connection

Now, all you have to do is, try to log in to your database by typing the following:

```bash
mysql -u root -p
```

Once executed, it would prompt you for your password (which you must have set in the [previous step](#secure-mysql-installation) and if you are able to log in, you are good to go!

Hope this guide helps you out!
