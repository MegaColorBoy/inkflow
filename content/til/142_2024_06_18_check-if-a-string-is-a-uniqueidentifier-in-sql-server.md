title: Check if a string is a UNIQUEIDENTIFIER in SQL Server
date: February 18th, 2024
slug: check-if-a-string-is-a-uniqueidentifier-in-sql-server
category: SQL Server
status: active

Recently, when I was performing a data migration that contained previous payment history, I came across a table that had a column named `PaymentId` which is supposed to have a UUID styled format but funnily enough, it was kind of confusing because some of them had numbers in it.

Luckily, the ones that weren't in UUID format are not supposed to be migrated, so I decided to write a `SELECT` query and filter the records using the `TRY_CONVERT` function:

```sql
SELECT 
    * 
FROM 
    dbo.YourTable 
WHERE 
    TRY_CONVERT(UNIQUEIDENTIFIER, YourColumn) IS NOT NULL;
```

Yes, it's that simple. You don't need to write any complex regular expressions for such operations.

Hope you found this tip useful!