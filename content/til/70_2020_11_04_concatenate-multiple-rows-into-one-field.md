title: Concatenate multiple rows into one field
date: November 4th, 2020
slug: concatenate-multiple-rows-into-one-field
category: MySQL
status: active

Say, you have a table named `hobbies` and wanted to display a list of hobbies based on `user_id`, you'd probably do something like this:
```sql
SELECT title FROM hobbies WHERE user_id = 8;
```

This would return a list of hobbies like this:
```text
Boxing
Coding
Reading
Fishing
```

That's simple but what if you wanted to display them in one row? Like this:
```text
Boxing, Coding, Reading, Fishing
```

You can make use of the `GROUP_CONCAT` method to achieve the same result by executing the following SQL query:
```sql
SELECT GROUP_CONCAT(title, SEPARATOR ', ') FROM hobbies WHERE user_id = 8;
```

Nice, what if you wanted to view a list of hobbies of all users? In most cases, a table like this might have a many-to-many relationship, so in order to avoid possible duplicates, you can try this:
```sql
SELECT user_id, GROUP_CONCAT(title, SEPARATOR ', ') FROM hobbies
GROUP BY user_id
```

Hope this tip helps you out!