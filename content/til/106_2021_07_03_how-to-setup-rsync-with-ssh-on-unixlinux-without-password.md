title: How to setup rsync with passwordless SSH on UNIX/Linux?
date: July 3rd, 2021
slug: how-to-setup-rsync-with-passwordless-ssh-on-unixlinux
category: DevOps
status: active

Tired of ensuring if whether each file in every server is synced? Planning on doing automated backups? If so, then this technique should come in handy for you.

Interested? Then follow the steps below:

## Check if rsync over SSH works
Before you start, please ensure that you can `rsync` to your intended server over `ssh` using a password.
With the following example, you can just send a simple file over to the intended server and see if it works or not:

```bash
rsync -avz -e ssh test.txt username@REMOTE_SERVER_IP_OR_DOMAIN:/path/to/folder/
```

Once you execute this command on the terminal, it'll prompt you for a password on the remote server, if it does, then it works.

## Generate SSH Keys
If you want to do a passwordless SSH, you need to generate public and private SSH keys on the local server by typing the following command on the terminal:
```bash
ssh-keygen
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

If you're prompted to enter a passphrase, just hit `Enter` and proceed until the key is generated. Once the keys are generated, they'll be in the `~/.ssh` directory on your local server.

## Copy public key to remote server
Using `ssh-copy-id`, you can copy the public key to the remote server:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub REMOTE_SERVER_IP_OR_DOMAIN
```

Once executed, you'll be prompted to enter the password of the account on the remote server and if successful, the public key will be copied to the remote server and will be stored in it's appropriate location.

## Perform Rsync over passwordless SSH
If you've come this far, then you should be able to SSH to the remote server without entering the password:

```bash
ssh REMOTE_SERVER_IP_OR_DOMAIN
```

If it works, then perform the `rsync` operation again [(above)](#rsync-operation) and this time, it shouldn't prompt you to enter any password.

Hope you liked reading this short article!