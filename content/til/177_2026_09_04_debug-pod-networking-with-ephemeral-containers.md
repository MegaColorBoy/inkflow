title: Debug pod networking with ephemeral containers
date: September 4th, 2026
slug: debug-pod-networking-with-ephemeral-containers
category: Kubernetes + Networking + DevOps
status: active

Ever needed to check whether your application pod could reach a database or an HTTP endpoint, only to find that it didn't have `curl`, `telnet`, or any other useful tools installed?

Your first instinct might be to install the missing packages inside the application container. But there's a handy alternative: an ephemeral debug container.

This adds a separate container to the existing pod, sharing its network namespace. You can investigate connectivity without adding packages to the application's image. It still uses resources in the pod, so it isn't completely without impact.

I found an image called [Netshoot](https://github.com/nicolaka/netshoot) that includes tools such as `curl`, `dig`, and `nc`. Here's how you can open a debugging shell:

```bash
kubectl debug -it web-7c9d6f8b5d-k2m4p -n staging --image=nicolaka/netshoot -- /bin/bash
```

Replace the pod name and namespace with your own. Your cluster must allow ephemeral containers and the chosen image.

After startup messages, an illustrative shell prompt might look like this:

```text
web-7c9d6f8b5d-k2m4p:~#
```

Inside that shell, try resolving a database service or checking an HTTP endpoint:

```bash
dig +short mysql.staging.svc.cluster.local
curl -I --connect-timeout 5 --max-time 10 https://example.com
```

An example DNS response would be:

```text
10.96.42.18
```

Use your own service hostname; this example assumes the cluster's DNS domain is `cluster.local`.

If you also need to inspect another container's processes, add `--target=app` to the debug command, replacing `app` with that container's name. This depends on runtime support and isn't needed just to share the pod's network.

When you're done, type `exit`. The debug container stops, but its entry remains in the pod until the pod is removed. It isn't a regular sidecar, and it doesn't automatically restart. The [ephemeral container documentation](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) explains these lifecycle restrictions.

Pretty cool, huh?
