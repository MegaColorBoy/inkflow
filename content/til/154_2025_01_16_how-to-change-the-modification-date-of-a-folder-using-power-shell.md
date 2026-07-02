title: How to Change the Modification Date of a Folder Using PowerShell?
date: January 16th, 2025
slug: how-to-change-the-modification-date-of-a-folder-using-power-shell
category: PowerShell + DevOps
status: active

Recently, I had an interesting experience with a client who can be a bit nosy—and occasionally bossy too. They have a strict policy of deploying updates during off-peak hours on Fridays. 

Like most developers, I’m not a fan of deploying on Fridays 😡.

To navigate this, I deploy the updates on the server earlier in the week (without their knowledge) and place them in a separate directory until we receive the green light to switch the website to the new directory via server settings.

If you’re wondering why I use a separate directory, it’s to ensure I have a quick rollback option if needed. Oh, and did I mention they’ve blocked `git` on the production server? So, no version control system (VCS) for us.

Anyway, once I deployed earlier than planned and realized they might check the deployment timestamps. To stay ahead, I wrote a quick PowerShell script to tweak the folder timestamps.

## Steps to Change Folder Modification Date

### Open PowerShell as Administrator

- Search for **"PowerShell"** in the Start menu.
- Right-click on it and select **Run as Administrator**.

### Run the Command 

Use the following command to set the modification date for a folder:

```powershell
$path = "C:\Path\To\Your\Folder"
$date = Get-Date "2025-01-01 10:00:00"
(Get-Item $path).LastWriteTime = $date
```

- Replace `C:\Path\To\Your\Folder` with the full path of the folder.
- Replace `2025-01-01 10:00:00` with the desired date and time in the format `yyyy-MM-dd HH:mm:ss`.

### Verify the Change 

To confirm the modification date has been updated, use:

```powershell
(Get-Item $path).LastWriteTime
```

## Other Timestamps You Can Modify
PowerShell allows you to adjust other timestamps as well:

### Creation Date:

```powershell
(Get-Item $path).CreationTime = $date
```

### Accessed Date:

```powershell
(Get-Item $path).LastAccessTime = $date
```

## Why This is Useful?

This method is great for:

- Organizing folders with custom timestamps.
- Simulating specific scenarios for testing.
- Avoiding the hassle of installing third-party tools.


Situations like this has made me realize that the flexibility of PowerShell makes it the perfect tool for quick tasks. It’s amazing how a simple command can give you full control over folder metadata!

Hope you found this useful (and keep your tracks clear!)