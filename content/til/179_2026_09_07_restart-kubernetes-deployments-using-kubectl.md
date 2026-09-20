title: Restart Kubernetes deployments using kubectl
date: September 7th, 2026
slug: restart-kubernetes-deployments-using-kubectl
category: Kubernetes + DevOps
status: active

I usually restart application pods using Argo CD or Rancher. That's convenient for one or two applications, but when there are several deployments to restart, I'd rather do it from the terminal.

First, check the current cluster context and the deployments in your namespace:

```bash
kubectl config current-context
kubectl get deployments -n staging
```

Then trigger a restart for one deployment:

```bash
kubectl rollout restart deployment/web -n staging
```

An example response is:

```text
deployment.apps/web restarted
```

Replace `web` and `staging` with your deployment and namespace. The response confirms that the restart was requested, so I also watch its progress:

```bash
kubectl rollout status deployment/web -n staging --timeout=120s
```

Once complete, you might see:

```text
deployment "web" successfully rolled out
```

To restart all deployments in that namespace:

```bash
kubectl rollout restart deployment -n staging
```

Or narrow it down using a label that exists on your deployments:

```bash
kubectl rollout restart deployment -n staging -l app=web
```

One distinction worth remembering: this replaces the pods managed by the selected deployments. It doesn't restart every kind of pod in the namespace. Replacement behavior follows each deployment's strategy, so availability still depends on its configuration and available capacity.

You can find more examples in the [kubectl rollout reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/).

Hope you found this useful!
