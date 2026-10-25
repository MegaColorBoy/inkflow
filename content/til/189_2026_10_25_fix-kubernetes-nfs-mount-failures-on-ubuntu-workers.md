title: Fix Kubernetes NFS mount failures on Ubuntu workers
date: October 23rd, 2026
slug: fix-kubernetes-nfs-mount-failures-on-ubuntu-workers
category: Kubernetes + Linux + Storage + Troubleshooting
status: active

While deploying an application to staging, I noticed its pod was stuck in `ContainerCreating`. Restarting it didn't help, so I checked the pod's events:

```bash
kubectl describe pod <pod_name> -n <namespace>
```

Replace the placeholders with your pod name and namespace. The relevant error was:

```text
MountVolume.SetUp failed for volume:
mount failed: exit status 32

Mounting command: mount
Mounting arguments: -t nfs ...

Output:
mount: bad option; for several filesystems
(e.g. nfs, cifs) you might need a
/sbin/mount.<type> helper program.
```

I initially suspected the PVC or NFS server, but the missing helper message pointed me toward the worker node.

To see which node the pod was assigned to:

```bash
kubectl get pod <pod_name> -n <namespace> -o wide
```

In my case, it was a newly installed Ubuntu worker. For this NFS volume setup, the mount was performed on the node, before the application container could start.

After logging into that worker, I checked for the helper:

```bash
which mount.nfs
```

There was no output. That suggested the helper wasn't available on the command search path; checking the installed package was the next step:

```bash
dpkg-query -W nfs-common
```

On Ubuntu, `nfs-common` provides the NFS client utilities. The [Ubuntu NFS guide](https://ubuntu.com/server/docs/how-to/networking/install-nfs/) covers client installation.

The package was missing on this worker, so I installed it there:

```bash
sudo apt update
sudo apt install -y nfs-common
```

Once the utilities were installed, the pod started successfully after I restarted it. Kubernetes also retries failed volume mounts, so a restart isn't always necessary.

The useful lesson for me was to include the NFS client utilities in the setup for every worker that can run these workloads. Installing them inside the application image wouldn't fix this node-level mount failure.

Hope you found this useful!
