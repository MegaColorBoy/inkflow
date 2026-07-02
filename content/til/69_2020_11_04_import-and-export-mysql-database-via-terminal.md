title: Import and Export MySQL database via Terminal
date: November 4th, 2020
slug: import-and-export-mysql-database-via-terminal
category: MySQL
status: active

Sometimes, phpMyAdmin can be painful to use especially when you want to import/export a MySQL database.

If you're not afraid of using the Terminal, try these commands to save your time:

## Import MySQL database
```bash
mysql -u username -p database_name < your_sql_file.sql
```

Before you run this command, please make sure that you've created the `database_name` schema in your database or else, you might get an error especially if the `.sql` file doesn't have a `CREATE DATABASE` statement.

## Export MySQL database
```bash
mysqldump -u username -p database_name > your_sql_file.sql
```

This command will export your database with the file name `your_sql_file.sql` to your current path.

Hope this helps you out!
