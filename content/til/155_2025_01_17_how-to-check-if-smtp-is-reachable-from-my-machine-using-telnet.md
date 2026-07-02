title: How to Check if SMTP is Reachable from My Machine Using Telnet?
date: January 17th, 2025
slug: how-to-check-if-smtp-is-reachable-from-my-machine-using-telnet
category: SMTP + Telnet + DevOps
status: active

Recently, I learned how to test SMTP server connectivity using `telnet`. This is a handy way to verify if an SMTP server is reachable, troubleshoot email delivery issues, and manually interact with the server to diagnose problems. 

Here’s how I did it:

## 1. Ensure Telnet is Installed
First, I made sure `telnet` was installed on my machine. Most Linux distributions come with `telnet` pre-installed, but if it’s missing, here’s how to install it:

### For Ubuntu/Debian:

```bash
sudo apt install telnet
```

### For CentOS/RHEL:

```bash
sudo yum install telnet
```

### For Windows

Ironically, `telnet` is not enabled by default on Windows, but you can enable it:

1. Open the Control Panel.
2. Go to **Programs** > **Programs and Features** > **Turn Windows features on or off**.
3. Check the box for **Telnet Client** and click **OK**.
4. Once enabled, open the Command Prompt (`cmd`) to use Telnet.

## 2. Open a Telnet Connection to the SMTP Server
To connect to the SMTP server, I used the following command:

```bash
telnet <smtp_server_address> 25
```

Replace `<smtp_server_address>` with the SMTP server’s hostname or IP address. For example:

```bash
telnet smtp.example.com 25
```

If the connection is successful, the server responds with a `220` message, like this:

```text
220 smtp.example.com ESMTP Postfix
```

This means the SMTP server is reachable and ready to accept commands.

## 3. Test SMTP Commands (Optional)
To further test the SMTP server, I manually interacted with it using basic SMTP commands:

### Greet the Server:
I sent an `EHLO` command to introduce myself:

```text
EHLO example.com
```

The server responded with a list of supported features.

### Start an Email Transaction:
I specified the sender using the `MAIL FROM` command:

```text
MAIL FROM:<test@example.com>
```

The server responded with `250 OK`.

### Specify the Recipient:
I added the recipient using the `RCPT TO` command:

```text
RCPT TO:<user@example.com>
```

The server responded with `250 OK`.

### Enter the Email Data:
I typed `DATA` to start composing the email:

```text
DATA
```

After entering the email content, I ended the message with a single `.` on a new line:

```text
Subject: Test Email
This is a test email sent via Telnet.
.
```

The server responded with `250 OK`, confirming that the email was accepted.

### Quit the Session:
Finally, I ended the session with the `QUIT` command:

```text
QUIT
```

## 4. Troubleshoot Connection Issues
If the connection fails, I might see an error like:

```text
telnet: Unable to connect to remote host: Connection refused
```

This could mean:

- The SMTP server is not running.
- The port is blocked by a firewall.
- The server uses a different port (e.g., 587 for submission or 465 for SMTPS).

To resolve this, I checked:

- If the SMTP server is running and listening on the correct port.
- If my firewall or network allows outbound connections to the SMTP port.

## Example Workflow:
Here’s what a successful Telnet session looks like:

```bash
$ telnet smtp.example.com 25
Trying 192.0.2.1...
Connected to smtp.example.com.
Escape character is '^]'.
220 smtp.example.com ESMTP Postfix
EHLO example.com
250-smtp.example.com
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
MAIL FROM:<test@example.com>
250 2.1.0 Ok
RCPT TO:<user@example.com>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Subject: Test Email
This is a test email sent via Telnet.
.
250 2.0.0 Ok: queued as 12345
QUIT
221 2.0.0 Bye
Connection closed by foreign host.
```

## Why This is Useful?
Using Telnet to test SMTP connectivity is a quick and effective way to:

- Verify if the SMTP server is reachable.
- Diagnose email delivery issues.
- Manually test SMTP commands and server responses.

Hope you've found this article useful!