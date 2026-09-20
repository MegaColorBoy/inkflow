title: Connect to MySQL using a Kubernetes debug container
date: September 5th, 2026
slug: connect-to-mysql-using-a-kubernetes-debug-container
category: Kubernetes + MySQL + DevOps
status: active

What if you wanted to connect to a database server from an application's pod, but the application image didn't include a MySQL client?

You can add an ephemeral container with the client and run it directly. Here's a quick way to do it:

```bash
kubectl debug -it web-7c9d6f8b5d-k2m4p -n staging \
  --image=mysql:8.4 -- \
  mysql --host=mysql.staging.svc.cluster.local --port=3306 --user=app_reader --password
```

Replace the pod, namespace, database hostname, and username with your own values. This example uses the MySQL image to run its client; it doesn't start a database server.

The client prompts you for a password. Once connected, you can run a small query:

```sql
SELECT CURRENT_USER(), DATABASE();
```

For example:

```text
+----------------+------------+
| CURRENT_USER() | DATABASE() |
+----------------+------------+
| app_reader@%   | NULL       |
+----------------+------------+
1 row in set (0.00 sec)
```

Here, `NULL` means no default database has been selected. To select one and list its tables:

```sql
USE app_db;
SHOW TABLES;
```

The debug container shares the pod's network, but it doesn't automatically inherit the application's environment variables, credentials, or mounted certificates. Supply the connection settings yourself, including your database's required TLS options.

A successful connection verifies this client's network access and authentication. Your application may still have a different configuration.

Type `exit` to leave the MySQL client. The ephemeral container stops, although its record remains attached to the pod. You also need permission to add debug containers; see the [Kubernetes debugging guide](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#debugging-with-an-ephemeral-debug-container).

Hope you found this tip useful!
