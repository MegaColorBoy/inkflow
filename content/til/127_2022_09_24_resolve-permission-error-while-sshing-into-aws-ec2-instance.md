title: Resolve permission error while SSH-ing to AWS EC2 instance from a Linux machine
date: September 24th, 2022
slug: resolve-permission-error-while-sshing-to-aws-ec2-instance-from-a-linux-machine
category: AWS + DevOps + SSH
status: active

If you are someone who's trying to access a AWS EC2 instance via SSH using a private key from a linux machine, you might have or will come across this error:

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'your-aws-private-key.pem' are too open.
It is recommended that your private key files are NOT accessible by others.
This private key will be ignored.
bad permissions: ignore key: your-aws-private-key.pem
Permission denied (publickey).
```

## Why am I getting this?
From what I have read, EC2 instances will simply not accept a private key that are publicly visible to others especially if it's somewhere stored in your Desktop or Downloads folder.

So basically, your private key should be accessible to others.

## Oh, how can I fix it?
It's pretty straightforward, you just have to make sure that the private key is **read-only** like this:

```bash
chmod 400 your-aws-private-key.pem
```

After that, try connecting again and it should work fine!

Hope you found this tip useful!
