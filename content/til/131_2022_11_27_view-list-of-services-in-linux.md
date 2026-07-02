title: View list of services in Linux
date: November 27th, 2022
slug: view-list-of-services-in-linux
category: Linux + DevOps
status: active

If you wanted to see a list of services available on your Linux server/desktop, try the following command:

```bash
systemctl list-unit-files --type=service
```

Upon executing this command, you'll be able to see a list of services along with their statuses i.e whether the service is enabled or disabled.

This can come in handy if you want to know the status of a specific service like `nginx`:

```bash
systemctl list-unit-files --type=service | grep "nginx"
```

Hope you found this tip useful.
