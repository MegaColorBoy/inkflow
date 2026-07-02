title: Clean removal of Linux from a Windows dual-boot machine
date: May 13th, 2026
slug: clean-removal-of-linux-from-a-windows-dual-boot-machine
category: Linux + Windows + UEFI
status: active

Recently, I purchased a ThinkPad X1 Carbon Gen 13 to replace my old Dell XPS 13 9360. It came with Windows 11, and instead of wiping it, I decided to set up a dual-boot system with Linux. I still need Windows for .NET development, but I use Linux most of the time.

I eventually settled on Fedora, but I tried several distributions and desktop environments before getting there. Each time I removed Linux, I needed to clean up the old partitions and boot entries properly so they would not interfere with the next installation.

If you are doing the same kind of distro-hopping on a UEFI system, this is the cleanup process that worked for me.

This note covers UEFI systems only.

If you want to remove Linux from a Windows dual-boot setup, there are two things to clean up:

1. Delete the Linux partitions.
2. Remove the Linux bootloader files and firmware entries.

Before making changes, make sure Windows is working normally and back up anything you want to keep from your Linux installation.

## 1. Delete the Linux partitions

Open Windows Disk Management and identify the partitions that belong to Linux. These are usually the Linux root partition, swap partition, and optionally a separate `/home` partition.

Do not delete:

- The Windows partition
- The EFI System Partition
- The Windows recovery partition

Delete only the Linux partitions, then either leave the space unallocated or extend your Windows partition into it.

## 2. Remove Linux bootloader files from the EFI partition

Open Command Prompt as Administrator and assign a drive letter to the EFI System Partition:

```bash
diskpart
list vol
select vol <EFI volume number>
assign letter=S
exit
```

Then remove the Linux bootloader directories from the EFI partition:

```bash
S:
cd EFI
dir
rmdir /s /q <linux-folder>
```

Only delete the directory that matches your Linux installation. Common names include `fedora`, `ubuntu`, `debian`, and similar distro-specific folders.

Do not delete `Microsoft`.

## 3. Remove stale UEFI firmware boot entries

List the firmware boot entries:

```bash
bcdedit /enum firmware
```

Look for entries that reference your removed Linux installation, such as descriptions containing `Fedora`, `ubuntu`, `GRUB`, or a path that points to the distro's EFI loader.

Delete only the matching Linux entry:

```bash
bcdedit /delete {xxxx-xxxx-xxxx-xxxx}
```

Replace `{xxxx-xxxx-xxxx-xxxx}` with the actual identifier from the previous command.

## 4. Reboot and verify

Reboot the machine and confirm that the Linux boot entry is gone from the firmware boot menu and that Windows starts normally.

Hope you found this article useful!