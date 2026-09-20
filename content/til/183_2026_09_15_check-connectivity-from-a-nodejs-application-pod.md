title: Check connectivity from a Node.js application pod
date: September 15th, 2026
slug: check-connectivity-from-a-nodejs-application-pod
category: Node.js + Kubernetes + Networking + DevOps
status: active

I've deployed quite a few Node.js applications over the past three months. Sometimes I just want to do a basic connectivity check from the application's container without installing another tool.

Since Node.js is already there, why not use it?

For a hostname lookup using the container's operating-system resolver, try this:

```bash
kubectl exec web-7c9d6f8b5d-k2m4p -n staging -c app -- node -e "require('node:dns').lookup('example.com', { all: true }, (error, addresses) => { if (error) { console.error(error); process.exitCode = 1; return; } console.log(addresses); })"
```

Replace the pod name, namespace, container name, and hostname with your own. An illustrative result might look like this:

```text
[ { address: '192.0.2.10', family: 4 } ]
```

That address is only an example, not the actual address of `example.com`. Also, `dns.lookup()` uses the system's name-resolution facilities, which may include `/etc/hosts`; it isn't necessarily a direct DNS query. The [Node.js DNS documentation](https://nodejs.org/api/dns.html) explains the distinction.

To go a step further and make an HTTPS request, use a Node.js runtime with built-in `fetch` and `AbortSignal.timeout` support, such as Node.js 18 or later:

```bash
kubectl exec web-7c9d6f8b5d-k2m4p -n staging -c app -- node -e "fetch('https://example.com', { signal: AbortSignal.timeout(10000) }).then(response => { console.log('HTTP status:', response.status); if (!response.ok) process.exitCode = 1; }).catch(error => { console.error(error); process.exitCode = 1; })"
```

An example response is:

```text
HTTP status: 200
```

This checks more than name resolution: the request must also connect and complete TLS negotiation before receiving an HTTP response. A `401` or `403` still shows that an HTTP server responded, even though access wasn't granted. See the [Node.js fetch documentation](https://nodejs.org/api/globals.html#fetch).

These commands start a new Node.js process, so they won't automatically reproduce proxy settings or custom HTTP clients configured inside your running application.

Hope you found this tip useful!
