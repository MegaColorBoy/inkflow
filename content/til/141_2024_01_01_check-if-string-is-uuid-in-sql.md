title: Check whether a string is a UUID in SQL Server
date: August 9th, 2026
slug: check-if-whether-astring-is-a-uuid-in-sql-server
category: SQL
status: inactive

In my last project, I noticed that the specific column named `PaymentReferenceNumber` was either a UUID or a string of numbers. At that time, it was part of a data migration and the new system made use of UUIDs. So, as I was curious, I thought of checking how many UUIDs were really there and here's how I found out.

You can use `TRY_CONVERT` with `uniqueidentifier` to determine if the column contains a UUID or not:

```sql
SELECT CASE
    WHEN LEN(YourColumn) = 36
        AND TRY_CONVERT(uniqueidentifier, YourColumn) IS NOT NULL
    THEN 1
    ELSE 0
END AS IsUuid
FROM YourTable;
```

What `TRY_CONVERT` does is that if it's an empty or invalid value, it would return a `NULL` instead of throwing an error.

The length check does matter because SQL server can truncate strings longer than 36 characters during conversion.

Hope you found this article useful.
