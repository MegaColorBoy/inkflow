title: How to perform mysqldump without a password prompt?
date: April 10th, 2021
slug: how-to-perform-mysqldump-without-a-password-prompt
category: UNIX
status: active

If you're performing a mass database backup using `mysqldump`, you'll pretty much find it annoying to type in the password every single time.

To get rid of it, open `/etc/mysql/my.cnf` configuration file and add your database credentials:
```mysql
[mysqldump]
user="your_username"
password="your_password"
```

Once done, save the `my.cnf` configuration file and now, you can try exporting your database without a hassle like this:
```bash
mysqldump -u your_username database_name > database.sql
```

Hope this trick helps you out!