title: Transfer files remotely using SCP
date: June 13th, 2020
slug: transfer-files-remotely-using-scp
category: Linux
status: active

Do you want to transfer files remotely from one UNIX-based system to another? Try using the `scp` tool, which is a shorthand for **Secure Copy Protocol**. It's based off the SSH protocol using it as a means to securely transfer files from a local machine to one or more remote machines.

Here's a code snippet that can help you out to transfer from computer A to computer B:
```bash
scp your_local_file user@ipaddress:/directory_to_store
```
And transfer from computer B to computer A:
```bash
scp user@ipaddress:/directory/file_name your_local_directory
```
Oh, before you transfer files to another computer, make sure that you have permissions to access it first. If you don't have one, then create a new account using `useradd` on your remote system.
