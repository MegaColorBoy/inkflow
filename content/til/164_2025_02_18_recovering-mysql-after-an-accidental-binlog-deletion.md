title: Recovering MySQL After an Accidental Binlog Deletion
date: February 18th, 2025
slug: recovering-my-sql-after-an-accidental-binlog-deletion
category: MySQL + Databases + DevOps
status: active

Last night, I found myself debugging a MySQL issue at an ungodly hour. The **MySQL80 service refused to start**, throwing a vague error:  

> *The MySQL80 service started and then stopped…*  

Digging into `mysql.err`, I discovered the culprit—someone (not me! 😤) had **accidentally deleted a binary log (`mysql-bin.000xxx`)** while MySQL was still tracking it. Since MySQL relies on binlogs for replication and crash recovery, it panicked when it couldn't find the missing file.  

## The Fix

To get MySQL running again, I had to:  

- **Disable binary logging** (since this is a standalone server)  
- **Delete the corrupt binlog index file** (`mysql-bin.index`)  
- **Purge all old binlog files** that were hogging disk space  

## How to Properly Disable Binary Logging in MySQL 8.0?

Since **MySQL 8.0 enables binlogs by default**, simply removing `log-bin=mysql-bin` from `my.ini` wasn’t enough. I had to:  

### Comment out the existing binlog setting in my.ini  
```ini
# log-bin=mysql-bin
```
### Explicitly disable binary logging
```ini
[mysqld]
skip-log-bin
```

### Delete the old `mysql-bin.index` file

- This file keeps track of all binary log files.  
- Since a referenced binlog file was deleted, MySQL would **fail to start** if the index still contained entries for missing files.  
- Deleting it ensures that MySQL doesn’t look for non-existent logs.  

After restarting the service, I confirmed binlogging was off with:  

```sql
SHOW VARIABLES LIKE 'log_bin';
```

Output:  
```bash
log_bin | OFF
```

In conclusion, crisis averted, disk space reclaimed and finally got some sleep. 😴

Hope you found this useful!