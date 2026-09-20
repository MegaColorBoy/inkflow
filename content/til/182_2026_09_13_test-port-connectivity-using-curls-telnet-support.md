title: Test port connectivity using curl's Telnet support
date: September 13th, 2026
slug: test-port-connectivity-using-curls-telnet-support
category: Linux + Networking + curl + DevOps
status: active

Honestly, I discovered this for the first time recently. I had always used `telnet` to check whether I could connect to a port, but I never knew curl could do this too.

Here's a quick example:

```bash
curl -v --connect-timeout 5 --max-time 10 telnet://mail.example.com:25
```

Replace the hostname and port with the service you're testing. The connection timeout gives it five seconds to establish a connection, while `--max-time` limits the whole session to ten seconds.

An illustrative excerpt from a reachable SMTP server might look like this:

```text
*   Trying 192.0.2.25:25...
* Connected to mail.example.com (192.0.2.25) port 25
220 mail.example.com ESMTP Postfix
```

The `Connected` line confirms that the TCP connection opened. In this example, the SMTP banner also tells us that the server responded. Other services might stay silent until you send something.

Don't be surprised if the command eventually reports a timeout: the TCP connection may have succeeded and then remained open until the ten-second limit. Read the connection messages instead of relying only on the final exit code.

This doesn't verify authentication, TLS, or the health of an entire application. It's just a handy first check when troubleshooting connectivity.

If your curl build reports that Telnet isn't supported, run `curl --version` and check its protocol list. The [curl tutorial](https://curl.se/docs/tutorial.html) includes more about its Telnet support.

Hope you found this useful!
