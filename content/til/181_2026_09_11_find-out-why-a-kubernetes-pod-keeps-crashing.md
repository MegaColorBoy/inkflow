title: Find out why a Kubernetes pod keeps crashing
date: September 11th, 2026
slug: find-out-why-a-kubernetes-pod-keeps-crashing
category: Kubernetes + Troubleshooting + DevOps
status: active

If you've been deploying applications to Kubernetes for a while, you've probably come across `CrashLoopBackOff`. Seeing it is annoying, but the useful part is finding out what happened just before the container stopped.

Here's how I would start:

```bash
kubectl get pod web-7c9d6f8b5d-k2m4p -n staging
```

Replace the pod name and namespace with your own. For example, the output might be:

```text
NAME                  READY   STATUS             RESTARTS      AGE
web-7c9d6f8b5d-k2m4p   0/1     CrashLoopBackOff   5 (34s ago)   8m
```

That shows the symptom. To investigate it, get the pod's details:

```bash
kubectl describe pod web-7c9d6f8b5d-k2m4p -n staging
```

Look at the container's state, last termination reason, exit code, and the events near the bottom. An illustrative excerpt could look like this:

```text
State:          Waiting
  Reason:       CrashLoopBackOff
Last State:     Terminated
  Reason:       Error
  Exit Code:    1
```

Next, check the application logs:

```bash
kubectl logs web-7c9d6f8b5d-k2m4p -n staging -c app --tail=100
```

If the container has already restarted, the previous instance's logs can be more useful:

```bash
kubectl logs web-7c9d6f8b5d-k2m4p -n staging -c app --previous --tail=100
```

Here, `app` is the container name. The `--previous` flag retrieves logs from its previous terminated instance when available; it isn't a history of every restart. See the [kubectl logs reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/).

For example, your application might have logged:

```text
Error: Missing required environment variable DATABASE_URL
```

Now you have something specific to investigate: the application's configuration.

If you see `ImagePullBackOff` or `ErrImagePull` instead, the image couldn't be pulled, so application logs may not exist yet. Start with the events from `describe` and check the image name, tag, registry access, and image-pull credentials. The [Kubernetes debugging guide](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/) covers these checks.

Hope you found this tip useful!
