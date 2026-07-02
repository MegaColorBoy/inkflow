title: Filtering results by weekdays in SQL Server
date: February 18th, 2024
slug: filtering-results-by-weekdays-in-sql-server
category: SQL Server
status: active

Ever wanted to know how many people are actively posting something on a Monday? Or maybe during the weekends?

You can do that by using the `DATEPART` and `DATENAME` functions. Let me show you how they work.

## Using DATEPART

The `DATEPART` function represents weekdays as integers from 1 (Sunday) to 7 (Saturday).

Let's say that you wanted to filter between Monday and Friday, you can achieve something like this:

```sql
SELECT * FROM dbo.YourTable WHERE DATEPART(WEEKDAY, YourDateColumn) BETWEEN 2 and 6;
```

One thing to note, in SQL Server, Sunday is the first day of the week. So, if you wanted to set the first day of the week, you can write the following statement before executing your query:

```sql
SET DATEFIRST 1;  -- Set Monday as the first day of the week
SELECT * FROM dbo.YourTable WHERE DATEPART(WEEKDAY, YourDateColumn) BETWEEN 1 and 5;
```

In the example above, you'll achieve the same results as the previous one.


## Using DATENAME

The `DATENAME` function represents weekdays as a string from Monday to Sunday.

Let's replicate the previous example using this function:

```sql
SELECT * FROM dbo.YourTable WHERE DATENAME(WEEKDAY, YourDateColumn) IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday');
```

If you want to know more about filtering your records effectively using these methods, you can the read the documentation:

- [DATENAME (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/datename-transact-sql?view=sql-server-ver16)
- [DATEPART (Transact-SQL)](https://learn.microsoft.com/en-us/sql/t-sql/functions/datepart-transact-sql?view=sql-server-ver16)

Hope you found this tip useful!