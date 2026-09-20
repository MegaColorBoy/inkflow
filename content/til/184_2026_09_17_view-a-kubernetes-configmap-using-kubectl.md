title: View a Kubernetes ConfigMap using kubectl
date: September 17th, 2026
slug: view-a-kubernetes-configmap-using-kubectl
category: Kubernetes + DevOps
status: active

When checking an application's configuration, I often want to see what is actually stored in its ConfigMap. You can get that straight from the terminal.

First, list the ConfigMaps in your namespace:

```bash
kubectl get configmaps -n staging
```

Then view the one you're interested in as YAML:

```bash
kubectl get configmap web-config -n staging -o yaml
```

Replace `web-config` and `staging` with your own values. Here's an illustrative response with some metadata omitted:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: web-config
  namespace: staging
data:
  APP_ENV: staging
  LOG_LEVEL: info
  API_BASE_URL: https://api.example.com
```

If you only need a single value, JSONPath keeps the output small:

```bash
kubectl get configmap web-config -n staging -o jsonpath='{.data.LOG_LEVEL}{"\n"}'
```

For the example above, that prints:

```text
info
```

One thing to remember: this shows the ConfigMap stored in Kubernetes. It doesn't prove that the application is already using its latest values.

Values injected as environment variables require a pod restart to pick up changes. Mounted ConfigMap files generally update eventually, but `subPath` mounts don't receive those updates, and the application may still need to reload the file. The [ConfigMap documentation](https://kubernetes.io/docs/concepts/configuration/configmap/) explains these differences.

ConfigMaps are intended for non-confidential configuration. Passwords and tokens belong in Secrets or your existing secrets-management system.

Hope you found this useful!
