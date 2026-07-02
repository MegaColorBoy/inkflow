title: How to Find Users with Duplicate Email Addresses in SQL?
date: January 20th, 2025
slug: how-to-find-users-with-duplicate-email-addresses-in-sql
category: Databases + SQL + MySQL
status: active

When managing a database with user information, ensuring data integrity is crucial. One common issue that can arise is duplicate email addresses in the `users` table. 

Let me show you how to write a simple yet powerful SQL query to identify such duplicates!

## The Problem

In many applications, email addresses should be unique identifiers for users. However, duplicates can sneak into the database due to bugs, manual data imports, or other anomalies. Detecting and resolving these duplicates is essential to maintain data integrity and ensure proper functionality of user-related features, such as authentication.

## The Solution

Using SQL, you can quickly find all duplicate email addresses in your `users` table by leveraging the `GROUP BY` and `HAVING` clauses.

Here’s the query:

```sql
SELECT email, COUNT(*) AS email_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

## How It Works:

1. `GROUP BY email`: Groups the rows in the `users` table by the email column, so each group represents a unique email.
2. `COUNT(*)`: Counts the number of rows in each group.
3. `HAVING COUNT(*) > 1`: Filters the groups to only include those where the count is greater than 1, i.e., duplicate email addresses.

## Enhanced Query for User Details

If you want to see more details about the users who share the same email address (e.g., user IDs, names), you can use a subquery:

```sql
SELECT u.*
FROM users u
JOIN (
    SELECT email
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1
) dup_emails ON u.email = dup_emails.email;
```

## Explanation

- The subquery identifies all duplicate email addresses.
- The main query joins this result with the `users` table to retrieve detailed information about each user associated with the duplicate emails.

## Final Thoughts

This simple query can save you a lot of time when auditing your database for duplicate entries. Whether you’re cleaning up data or debugging an issue, identifying duplicates is an important step toward ensuring a robust and reliable application.

Hope you found this tip useful!