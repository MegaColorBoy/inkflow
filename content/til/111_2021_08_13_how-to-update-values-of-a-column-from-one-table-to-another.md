title: How to update values of a column from one table to another?
date: August 13th, 2021
slug: how-to-update-values-of-a-column-from-one-table-to-another
category: MySQL
status: active

Sometimes, I come across situations where I would need to update a newly added in a pivot table and this query does come in handy:
```mysql
UPDATE table_a INNER JOIN table_b ON table_b.col_x = table_a.col_x SET table_a.col_y = table_b.col_y;
```

Hope you found this useful too!