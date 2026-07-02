title: Use MySQL 8.0 with Native Password Authentication
date: March 12th, 2021
slug: use-mysql-80-with-native-password-authentication
category: MySQL
status: active

Last month, I was configuring an Ubuntu Server to deploy a client's project that uses MySQL 8.0 and PHP 7.2.
So, I installed the necessary dependencies and finally installed MySQL 8.0, created a new schema and imported the database tables required for the project.

Next, I typed the project URL and ran into this error:

```text
Unable to load plugin 'caching_sha2_password'
```

If you're running PHP 7.2 and facing this error, you should know that PHP 7.2 doesn't support native password authentication by default. But it's a simple fix, all you have to do is either one of the following:

1. [Alter the current user's authentication to native password](#opt1)
2. [Create a new user with native password authentication](#opt2)

## <a id="opt1"></a> Alter the current user's authentication to native password

```mysql
ALTER USER 'your_user'@'your_server_host' IDENTIFIED WITH mysql_native_password BY 'your_password';
```

## <a id="opt2"></a> Create a new user with native password authentication

```mysql
CREATE USER 'your_user'@'your_server_host ' IDENTIFIED WITH mysql_native_password BY 'your_password'
```

For the changes to take effect, you need to reload the privileges by typing the following:

```mysql
FLUSH PRIVILEGES;
```

Hope this helps you out!
