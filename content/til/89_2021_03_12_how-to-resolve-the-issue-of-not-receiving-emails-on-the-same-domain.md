title: How to resolve the issue of not receiving emails on the same domain?
date: March 12th, 2021
slug: how-to-resolve-the-issue-of-not-receiving-emails-on-the-same-domain
category: cPanel + Email
status: active

Recently, we hosted our company's redesigned website on GoDaddy, which offers cPanel to manage your website. I was dealing with an annoying email bug in which I was able to send/receive emails to any account except the ones that share the company domain.

The company's current email setup makes use of Google Workspace and since we're using a Shared Hosting account, GoDaddy allows you to use their SMTP relay and prohibits the use of third-party SMTP services such as Google Workspace, Outlook, etc.

After configuring it with Google's MX records in the DNS settings, I wasn't receiving any email on my own company email yet I was able to receive on other email accounts that didn't share the company's domain.

I did a little R&D and ran into this documentation about [email routing](https://docs.cpanel.net/cpanel/email/email-routing/) and figured out that there could be an issue with it's configuration.

Here's what I did:

1. Open cPanel 
2. Search or look for **Email Routing**
3. Click on **Email Routing**
4. If your MX records are not pointing to the IP address of the hosting server, then select **Remote Mail Exchanger**
5. Save changes

After following these steps, I was able to receive mails on the same domain!

## So what really caused the issue?

Since, we didn't have a default email address set up in cPanel, the current mode to send all unrouted emails was set to `:blackhole:`, by default. I guess, it's set up that way to prevent the server from sending/receiving spam mails from the domain.

This makes sense because:

1. The MX records are not pointing to the current server
2. There are no email accounts created for the domain on cPanel
3. By setting the mode to `:blackhole`, all emails with the same domain are being discarded or rejected

Not really sure if this is what caused the issue but judging from the facts, I was able to reach to this conclusion.

Hope you found this tip useful.

## Reference

- [Can't send email to addresses at my own domain](https://stackoverflow.com/questions/1107730/cant-send-email-to-addresses-at-my-own-domain)