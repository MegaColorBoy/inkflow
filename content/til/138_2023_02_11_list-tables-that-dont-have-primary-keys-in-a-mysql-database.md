title: List tables that don't have primary keys in a MySQL database
date: February 11th, 2023
slug: list-tables-that-dont-have-primary-keys-in-a-mysql-database
category: MySQL
status: active

Whenever I restore a database dump on a MySQL InnoDB Cluster, most of the time, the error I face is related to missing `PRIMARY KEY` attribute because as per [MySQL's official documentation](https://dev.mysql.com/doc/refman/8.0/en/group-replication-requirements.html):

> Every table that is to be replicated by the group must have a defined primary key, or primary key equivalent where the equivalent is non-null unique key.

What I would usually do is, run a simple query to determine the list of the tables that don't the `PRIMARY KEY` attribute:

```mysql

select tab.table_schema as database_name,
       tab.table_name
from information_schema.tables tab
left join information_schema.table_constraints tco
          on tab.table_schema = tco.table_schema
          and tab.table_name = tco.table_name
          and tco.constraint_type = 'PRIMARY KEY'
where tco.constraint_type is null
      and tab.table_schema not in('mysql', 'information_schema', 'performance_schema', 'sys')
      and tab.table_type = 'BASE TABLE'
      and tab.table_schema = 'your_database_name_here'
order by tab.table_schema,
         tab.table_name;
```

Hope you found this tip useful!
