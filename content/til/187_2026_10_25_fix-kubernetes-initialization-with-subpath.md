title: Fix Kubernetes initialization with subPath
date: October 21st, 2026
slug: fix-kubernetes-initialization-with-subpath
category: Kubernetes + Storage + Troubleshooting + DevOps
status: active

While deploying a .NET Core application to production, I came across an error that hadn't appeared in staging:

```text
System.InvalidOperationException: Fresh setup refused: existing private files, keys or uploads requires operator recovery.
```

At first, I suspected a permissions issue. The application needed persistent directories for uploads, encryption keys, and configuration, with a separate PVC for each one. This was the container's mount configuration:

```yaml
volumeMounts:
  - name: uploads
    mountPath: /var/lib/app/storage
  - name: keys
    mountPath: /var/lib/app/keys
  - name: configuration
    mountPath: /var/lib/app/configuration
```

These are mount entries from the workload, not a complete manifest. Each name refers to a volume backed by its corresponding PVC.

The vendor confirmed that the directories had to be empty during initial setup. To inspect them, I temporarily replaced the container's startup command with `sleep` and opened a shell inside it.

Listing the storage directory revealed an unexpected entry:

```bash
ls -la /var/lib/app/storage
```

Alongside `.` and `..`, there was a `lost+found` directory. The other two mounts had one too.

Filesystems such as ext4 typically create `lost+found` during initialization for filesystem recovery. So a freshly provisioned PVC doesn't necessarily expose an empty directory. In this case, the application treated that entry as existing application data and refused to initialize.

The fix was to mount a dedicated subdirectory using `subPath`:

```yaml
volumeMounts:
  - name: uploads
    mountPath: /var/lib/app/storage
    subPath: app-data
  - name: keys
    mountPath: /var/lib/app/keys
    subPath: app-data
  - name: configuration
    mountPath: /var/lib/app/configuration
    subPath: app-data
```

Each of the three separate PVCs then had this layout:

```text
PVC root/
├── lost+found/
└── app-data/
```

The application now saw only `app-data` at each mount path, without the `lost+found` entry. After restoring the normal startup command, initialization succeeded.

The [Kubernetes volume documentation](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) explains how `subPath` selects a directory within a volume. Make sure that directory has the permissions required by the container's runtime user. If you reuse one PVC for several mounts, use different subdirectories when the data needs to stay separate.

For an existing deployment, back up the data and plan the move first: files at the PVC root won't automatically appear inside the new subdirectory.

Hope you found this useful!
