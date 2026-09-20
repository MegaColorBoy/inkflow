title: Copy files to and from Kubernetes pods
date: September 2nd, 2026
slug: copy-files-to-and-from-kubernetes-pods
category: Kubernetes + DevOps
status: active

Every now and then, I need to copy files into an application pod. One use case for me is moving uploaded assets while migrating an application from staging to production.

For this, you can use `kubectl cp`. The remote path uses a namespace and pod name, so there's no SSH username or server address involved.

Here's an example of copying a local file into a container:

```bash
kubectl cp ./logo.png staging/web-7c9d6f8b5d-k2m4p:/var/www/html/public/logo.png -c app
```

Replace `staging`, the pod name, `app`, and the paths with your own values. The destination directory must exist and be writable by the container's user.

You can also do the reverse and copy a file into your current directory:

```bash
kubectl cp staging/web-7c9d6f8b5d-k2m4p:/var/www/html/public/logo.png ./logo.png -c app
```

For a directory of uploaded assets, I would copy it locally first, then into the destination pod:

```bash
kubectl cp staging/web-7c9d6f8b5d-k2m4p:/var/www/html/public/uploads ./uploads -c app
kubectl cp ./uploads production/web-5f7c8d9b6-m3q8r:/var/www/html/public/ -c app
```

Use a fresh local destination and check the target directory before copying, as existing files can be overwritten.

One detail that's easy to miss: `kubectl cp` needs `tar` inside the container. Without it, the copy fails. The [kubectl cp reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cp/) also covers cases that need a more explicit tar-based copy.

Also, think about where these files will live. Files written into a container's writable layer won't survive its replacement. For uploaded assets that need to persist, use the application's persistent volume or shared storage, and coordinate the copy if uploads are still changing.

Hope you found this useful!
