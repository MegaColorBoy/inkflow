title: Find a Kubernetes pod and open a shell inside it
date: September 1st, 2026
slug: find-a-kubernetes-pod-and-open-a-shell-inside-it
category: Kubernetes + DevOps
status: active

At my new job as a Senior DevOps engineer, I have learnt a lot in a short amount of time. One of the first things I got comfortable with was finding an application's pod and opening a shell inside its container.

This is quite useful when you want to check file permissions or explore what is actually running inside your application container.

First, get the pods in your namespace:

```bash
kubectl get pods -n staging
```

For example, you might see:

```text
NAME                   READY   STATUS    RESTARTS   AGE
web-7c9d6f8b5d-k2m4p    1/1     Running   0          2h
worker-6b8f4d7c9-x5n2q  1/1     Running   0          2h
```

Here, `staging` is an example namespace. Replace it and the pod names with your own throughout this post. Also, make sure `kubectl` is connected to the intended cluster.

Once you have the pod name, open a shell:

```bash
kubectl exec -it web-7c9d6f8b5d-k2m4p -n staging -- /bin/sh
```

The `-i` flag keeps standard input open, and `-t` allocates a terminal. The `--` separates kubectl's options from the command you want to run inside the container.

If the pod has multiple containers, choose one explicitly:

```bash
kubectl exec -it web-7c9d6f8b5d-k2m4p -n staging -c app -- /bin/sh
```

The shell depends on the image. `/bin/sh` is common, while `/bin/bash` only works if Bash is installed. Some minimal images have no shell at all; in that case, a [debug container](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#debugging-with-an-ephemeral-debug-container) can help.

Type `exit` when you're done. This closes your shell session; it doesn't stop the application.

Hope you found this tip useful!
