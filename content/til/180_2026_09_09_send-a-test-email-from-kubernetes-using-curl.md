title: Send a test email from Kubernetes using curl
date: September 9th, 2026
slug: send-a-test-email-from-kubernetes-using-curl
category: Kubernetes + SMTP + curl + DevOps
status: active

When troubleshooting email delivery, I sometimes want to send a test message from inside the cluster. This helps narrow down whether the SMTP server is reachable from that environment.

For a quick test, you can start a temporary pod with curl installed:

```bash
kubectl run smtp-test -n staging --rm -it --restart=Never --image=curlimages/curl --command -- sh
```

Replace `staging` with your namespace. This creates a separate pod. `--command` selects the shell, and `--restart=Never` prevents the container from restarting when it exits. During a normal attached session, `--rm` cleans up the pod when you're done. See the [kubectl run reference](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run/).

Inside the shell, send a message through your internal SMTP relay:

```bash
curl -v --connect-timeout 5 --max-time 30 \
  --url smtp://mail.example.com:25 \
  --mail-from 'sender@example.com' \
  --mail-rcpt 'recipient@example.com' \
  --crlf --upload-file - <<'EOF'
From: sender@example.com
To: recipient@example.com
Subject: Test email from Kubernetes

This is a test message.
EOF
```

Replace the hostname and addresses with real ones before running it. This example assumes an internal relay that allows unauthenticated, unencrypted SMTP from the test pod.

For an authenticated server using STARTTLS on port 587, use these options in the same command:

```bash
--url smtp://mail.example.com:587 --ssl-reqd --user 'smtp-user'
```

With only a username supplied, curl prompts for the password. For implicit TLS, use `smtps://mail.example.com:465` instead. These options are described in the [curl manual](https://curl.se/docs/manpage.html).

An illustrative excerpt after uploading the message might look like this:

```text
< 250 2.0.0 Ok: queued as A1B2C3D4
> QUIT
< 221 2.0.0 Bye
```

That means the relay accepted the message, not that it has reached the recipient's inbox. Check delivery logs if it never arrives.

Also, a separate test pod may have different labels and network policies from your application. Treat this as a test from that pod, rather than proof that the application has identical access.

Type `exit` to finish. If the session was interrupted and the pod remains, remove it with `kubectl delete pod smtp-test -n staging`.

Hope you found this useful!
