title: How to duplicate tables in MySQL?
date: July 18th, 2020
slug: how-to-duplicate-tables-in-mysql
category: MySQL
status: active

This trick comes in handy whenever you wanted to reuse a table, perform data migrations or maybe even take a backup of the table before any of your experiments mess up your data.

Executing the following query will help you create a new table with the structure of the old table:
```mysql
CREATE TABLE schema.new_table LIKE schema.old_table;
```

If you want the data as well, try this:
```mysql
CREATE TABLE schema.new_table LIKE schema.old_table;
INSERT schema.new_table SELECT * FROM schema.old_table;
```

You can use this query to copy tables from one schema to another schema too. Hope this helps you out! &#x1F604;