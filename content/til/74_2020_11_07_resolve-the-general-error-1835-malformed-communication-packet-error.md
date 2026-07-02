title: Resolve the "General error: 1835 Malformed communication packet" error
date: November 7th, 2020
slug: resolve-the-general-error-1835-malformed-communication-packet-error
category: PHP
status: active

This happened like two days ago, when one of the client sites went down. Upon inspecting the error logs, I found this:

```text
SQLSTATE[HY000]: General error: 1835 Malformed communication packet
```

If you got the same error as the one above, don't worry, it's not your fault. According to this [forum](https://jira.mariadb.org/browse/MDEV-24121), **a recent MariaDB update introduced a new bug for PHP versions < 7.3** that uses PDO and MySQL connectors. You can easily resolve this by simply upgrading it to PHP 7.3.

Hope this tip helps you out!