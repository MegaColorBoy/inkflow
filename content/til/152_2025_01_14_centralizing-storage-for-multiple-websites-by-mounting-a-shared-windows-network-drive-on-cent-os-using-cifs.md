title: Centralizing Storage for Multiple Websites by Mounting a Shared Windows Network Drive on CentOS Using CIFS
date: January 14th, 2025
slug: centralizing-storage-for-multiple-websites-by-mounting-a-shared-windows-network-drive-on-cent-os-using-cifs
category: CentOS + DevOps + Linux
status: active

Running more than 45 websites on a CentOS server can be a challenge, especially when it comes to managing storage. In my case, these websites are hosted across two different servers, and each site has its own storage folder for images and uploads.

To streamline this, I came up with a solution: centralizing all storage uploads in one place by hosting a shared Windows network drive and mounting it on the CentOS servers. 

This way, all websites can access the same centralized storage, making management much easier.

Here’s how I did it, step by step:

#### Step 1: Install cifs-utils
First, you need to install the `cifs-utils` package, which provides the necessary tools to mount CIFS shares.

```bash
yum install cifs-utils
```

#### Step 2: Create a Service Account
Next, I created a service account on the CentOS server. This account will be used to access the shared drive. I named it `svc_library_core` and assigned it a UID of 5000. You can choose any name and UID that isn’t already in use.

```bash
useradd -u 5000 svc_library_core
```

#### Step 3: Create a Group for the Share
I also created a group on the CentOS server that will map to the shared drive. This group will contain all the Linux accounts that need access to the share. I named the group `share_library_core` and gave it a GID of 6000.

```bash
groupadd -g 6000 share_library_core
```

#### Step 4: Add Users to the Group
After creating the group, I added the necessary users to it. For example, if you want the `apache` user to have access to the share, you can add it like this:

```bash
usermod -G share_library_core -a apache
```

#### Step 5: Prepare Credentials
To mount the drive, you’ll need to provide the credentials for the Windows share. You can either pass them directly using the `-o` option or save them in a file. I opted to save them in a file for security reasons.

Switch to the root user and create a file to store the credentials:

```bash
su - root
touch /root/creds_smb_library_core
chmod 0600 /root/creds_smb_library_core
vi /root/creds_smb_library_core
```

Add the following lines to the file, replacing the placeholders with your actual Windows or Active Directory username and password:

```text
username=YourWindowsUsername
password=YourWindowsPassword
```

#### Step 6: Mount the Drive
Now, you’re ready to mount the shared drive. Use the following command, replacing the placeholders with your actual values:

```bash
sudo mount -t cifs //<destination_ip>/path/to/directory /test-directory -o credentials=/root/creds_smb_library_core,uid=5000,gid=6000,iocharset=utf8,file_mode=0774,dir_mode=0775
```

- `//<destination_ip>/path/to/directory` is the path to the shared drive on the Windows server.
- `/test-directory` is the local directory where you want to mount the drive.
- `credentials=/root/creds_smb_library_core` points to the file containing your credentials.
- `uid=5000` and `gid=6000` map the mounted drive to the service account and group you created earlier.
- `iocharset=utf8` ensures proper character encoding.
- `file_mode=0774` and `dir_mode=0775` set the file and directory permissions.

#### Step 7: Unmounting the Drive
If you need to unmount the drive later, you can do so with the following command:

```bash
sudo umount /test-directory
```

### Bonus: Automount Script for Server Reboots
One challenge I faced was ensuring that the shared drives were automatically remounted in case the servers went down or were rebooted. To handle this, I wrote a simple script that mounts the drives on startup.

#### Create the Script
Create a new script file, for example, `/usr/local/bin/mount_shares.sh`:

```bash
#!/bin/bash
mount -t cifs //<destination_ip>/path/to/directory /test-directory -o credentials=/root/creds_smb_library_core,uid=5000,gid=6000,iocharset=utf8,file_mode=0774,dir_mode=0775
```

Make sure to replace the placeholders with your actual values.

#### Make the Script Executable
Set the executable permission on the script:

```bash
chmod +x /usr/local/bin/mount_shares.sh
```

#### Add the Script to Startup
To ensure the script runs on startup, add it to the `/etc/rc.local` file:

```bash
/usr/local/bin/mount_shares.sh
```

Make sure `/etc/rc.local` is executable:

```bash
chmod +x /etc/rc.local
```

#### Test the Script
Reboot your server and verify that the shared drives are automatically mounted.

And that’s it! 

You’ve successfully mounted a shared Windows network drive on CentOS using CIFS and ensured it remounts automatically on server reboots. 

This setup has made managing storage for multiple websites much more efficient and centralized.

Hope you found this article useful!