title: List Plesk hosted sites and PHP handlers
date: October 25th, 2026
slug: list-plesk-hosted-sites-and-php-handlers
category: Plesk + SQL + DevOps
status: active

If you need a quick inventory of the sites hosted on a Plesk server, `plesk db` is useful to have around. I find it especially handy when checking which PHP handler each site uses.

From an administrative shell on the Plesk server, run:

```bash
plesk db -e "SELECT d.name AS Domain, h.php AS PHP_ENABLED, h.php_handler_id AS PHP_Handler FROM domains d JOIN hosting h ON h.dom_id = d.id ORDER BY d.name ASC;"
```

An illustrative result might look like this:

```text
+---------------------+-------------+-----------------+
| Domain              | PHP_ENABLED | PHP_Handler     |
+---------------------+-------------+-----------------+
| example.com         | true        | plesk-php83-fpm |
| staging.example.com | true        | plesk-php82-fpm |
+---------------------+-------------+-----------------+
```

The query joins domain names to their hosting settings. Plesk uses the same tables and handler field in its [PHP handler management examples](https://support.plesk.com/hc/en-us/articles/12377435963927-How-to-change-PHP-version-handler-for-a-domain-or-all-domains-in-Plesk).

Because this is an inner join with `hosting`, it lists domains with hosting records. It isn't an inventory of every alias or forwarding-only domain. Also, a handler ID identifies the configured handler, not its exact installed PHP patch version.

To narrow the list to domains whose database status is `0` (active), add a `WHERE` clause:

```bash
plesk db -e "SELECT d.name AS Domain, h.php AS PHP_ENABLED, h.php_handler_id AS PHP_Handler FROM domains d JOIN hosting h ON h.dom_id = d.id WHERE d.status = 0 ORDER BY d.name ASC;"
```

For example, if only `example.com` from the first listing is active, the result would be:

```text
+-------------+-------------+-----------------+
| Domain      | PHP_ENABLED | PHP_Handler     |
+-------------+-------------+-----------------+
| example.com | true        | plesk-php83-fpm |
+-------------+-------------+-----------------+
```

That status filter reflects Plesk's domain status; it doesn't test whether the website responds successfully.

If you only need a count of those active hosted domains:

```bash
plesk db -e "SELECT COUNT(*) AS Active_Hosted_Domains FROM domains d JOIN hosting h ON h.dom_id = d.id WHERE d.status = 0;"
```

All three queries only read the database, which makes them handy for a quick inventory before reviewing site settings.

Hope you found this useful!
