title: How to Filter Records Based on a String Column Containing Numbers with Commas and Dots?
date: January 19th, 2025
slug: how-to-filter-records-based-on-a_string-column-containing-numbers-with-commas-and-dots
category: SQL + MySQL + Databases + Data Manipulation
status: active

Last month, I encountered a scenario where I needed to filter records in a database based on a "revenue" column. The challenge? The `revenue` column was stored as a string data type, and some of the values contained commas (`,`) and dots (`.`). Here’s how I tackled the problem and wrote an SQL query to filter records based on the numeric value of the `revenue` column.

## What I faced?
The `revenue` column was stored as a string, and the values looked like this:

- "50,000,000"
- "75.000.000"
- "10000000"

I needed to filter records where the revenue was greater than **"50,000,000"**. However, since the column was a string, I couldn’t directly compare it to a numeric value.

## What I did?

To handle this, I used a combination of SQL functions:

1. `REPLACE`: To remove commas (`,`) and dots (`.`) from the string.
2. `CAST`: To convert the cleaned string into a numeric data type (`DECIMAL` in this case).

Here’s the SQL query I wrote:

```sql
SELECT *
FROM your_table
WHERE CAST(REPLACE(revenue, ',', '') AS DECIMAL(18, 2)) > 50000000;
```

Need a breakdown? Here you go:

1. `REPLACE(revenue, ',', '')`:
This removes commas from the `revenue` string. For example, **"50,000,000"** becomes **"50000000"**.
2. `CAST(... AS DECIMAL(18, 2))`:
This converts the cleaned string into a `DECIMAL` value with 18 total digits and 2 decimal places. For example, **"50000000"** becomes **50000000.00**.
3. `> 50000000`:
Finally, the query filters records where the numeric value of `revenue` is greater than **50,000,000**.

## Handling Dots as Thousand Separators
If the `revenue` column uses dots (`.`) as thousand separators (e.g., **"75.000.000"**), you can extend the `REPLACE` function to remove dots as well:

```sql
SELECT *
FROM your_table
WHERE CAST(REPLACE(REPLACE(revenue, ',', ''), '.', '') AS DECIMAL(18, 2)) > 50000000;
```

This ensures that both commas and dots are removed before converting the string to a numeric value.

## Why did I do this?
This approach is helpful when:

- You’re working with data stored as strings but need to perform numeric comparisons.
- The data contains formatting characters like commas or dots.
- You want to avoid manual data cleaning or preprocessing.

By using SQL functions like `REPLACE` and `CAST`, you can handle these scenarios directly in your queries.

Oh, this works for SQL and MySQL as well!

Hope you found this article useful!