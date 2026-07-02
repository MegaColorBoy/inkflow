title: How to Send Test Emails via PowerShell?
date: January 21st, 2025
slug: how-to-send-test-emails-via-power-shell
category: PowerShell + SMTP + DevOps
status: active

## How to Send Test Emails via PowerShell

Whenever I wanted to send a test mail from a Windows Server, I make use of PowerShell. This makes it easier and is a quick yet efficient way to test email functionality, troubleshoot SMTP servers, or verify email delivery. 

Here’s what I usually do, including examples with and without user authentication.

## 1. Basic Command to Send a Test Email
The `Send-MailMessage` cmdlet in PowerShell makes it easy to send emails via an SMTP server. Here’s the basic command I used:

```powershell
Send-MailMessage -SmtpServer "0.0.0.0" -Port 25 -From "sample@example.com" -To "john.doe@example.com" -Subject "A subject" -Body "A body"
```

- `-SmtpServer`: The IP address or hostname of the SMTP server.
- `-Port`: The SMTP port (default is 25).
- `-From`: The sender’s email address.
- `-To`: The recipient’s email address.
- `-Subject`: The subject of the email.
- `-Body`: The content of the email.

This command works for SMTP servers that don’t require authentication (e.g., internal SMTP relays).

## 2. Sending Emails with User Authentication

If the SMTP server requires authentication, you can add the `-Credential` parameter to provide a username and password. Here’s how:

```powershell
$credential = Get-Credential
Send-MailMessage -SmtpServer "smtp.example.com" -Port 587 -From "sample@example.com" -To "john.doe@example.com" -Subject "A subject" -Body "A body" -Credential $credential -UseSsl
```

- `-Credential`: Prompts for a username and password. You can also create a `PSCredential` object programmatically.
- `-UseSsl`: Enables SSL/TLS encryption, which is often required for authenticated SMTP servers (e.g., port 587).

### Example with Hardcoded Credentials:

If you don’t want to be prompted for credentials, you can create a `PSCredential` object like this on PowerShell ISE:

```powershell
$username = "sample@example.com"
$password = ConvertTo-SecureString "YourPassword" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($username, $password)

Send-MailMessage -SmtpServer "smtp.example.com" -Port 587 -From "sample@example.com" -To "john.doe@example.com" -Subject "A subject" -Body "A body" -Credential $credential -UseSsl
```

## 3. Adding Attachments

You can also attach files to your email using the `-Attachments` parameter:

```powershell
Send-MailMessage -SmtpServer "smtp.example.com" -Port 587 -From "sample@example.com" -To "john.doe@example.com" -Subject "A subject" -Body "A body" -Attachments "C:\path\to\file.txt" -Credential $credential -UseSsl
```

## 4. Troubleshooting Tips

### Connection Issues: 

If the email fails to send, ensure the SMTP server is reachable and the port is open. Use `Test-NetConnection` to verify connectivity:

```powershell
Test-NetConnection -ComputerName smtp.example.com -Port 587
```

### Authentication Errors:

Double-check the username and password. If the SMTP server requires a specific authentication method (e.g., OAuth), you may need additional configuration.

### SSL/TLS Errors:

Ensure the `-UseSsl` parameter is used if the SMTP server requires encryption.

## Example Workflow:

Here’s a complete example with authentication and attachments:

```powershell
# Create credentials
$username = "sample@example.com"
$password = ConvertTo-SecureString "YourPassword" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($username, $password)

# Send email with attachment
Send-MailMessage -SmtpServer "smtp.example.com" -Port 587 -From "sample@example.com" -To "john.doe@example.com" -Subject "Test Email with Attachment" -Body "Please find the attached file." -Attachments "C:\path\to\file.txt" -Credential $credential -UseSsl
```

## Why do this way?

Using PowerShell to send test emails is a powerful way to:

- Test SMTP server configurations.
- Verify email delivery and troubleshoot issues.
- Automate email notifications in scripts.

Whether you’re working with an internal SMTP relay or an external server requiring authentication, PowerShell’s `Send-MailMessage` cmdlet makes it easy to get the job done.

Hope you found this useful!