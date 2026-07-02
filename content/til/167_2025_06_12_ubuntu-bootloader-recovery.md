title: Ubuntu Bootloader Recovery
date: June 12th, 2025
slug: ubuntu-bootloader-recovery
category: Ubuntu + DevOps + Linux + GRUB
status: active

This is a guide on how to recover Ubuntu's GRUB Bootloader in the case of whenever a LVM UUID is changed or corrupted.

## The Problem
The error `"disk not found: /xxx-xxx"` in `grub rescue>` mode suggests GRUB can't find the device or logical volume it was previously configured to boot from. 

This usually happens when:
* LVM volumes weren't activated during boot
* The volume group UUID changed or became corrupted

## The Context

The `/xxx-xxx` in the message is likely referring to a **LVM volume by UUID**, e.g.:

```bash
error: disk 'lvmid/XXX-XXX-XXX' not found
```

This typically means GRUB is referencing a **missing or renamed LVM LV or VG**

## The Solution

Boot from a live ISO, open a terminal and follow these steps:

### 1. Check Disks and LVM State

```bash
sudo lsblk
sudo fdisk -l
```

Then:

```bash
sudo vgscan
```

This activates any found LVM volume groups and logical volumes.

Then verify with:

```bash
sudo lvdisplay
```

### 3. Mount the System Manually

Assuming your root volume is `/dev/mapper/your_lvm_drive`:

```bash
sudo mkdir /mnt/recovery
sudo mount /dev/mapper/your_lvm_drive /mnt/recovery
```

### 4. Prepare for chroot

```bash
sudo mount --bind /dev /mnt/recovery/dev
sudo mount --bind /proc /mnt/recovery/proc
sudo mount --bind /sys /mnt/recovery/sys
sudo chroot /mnt/recovery
```

The `chroot` command changes the root directory for the kernel, effectively making a specified directory the new starting point for any file access within the chrooted process. 

### 5. Reinstall GRUB

```bash
grub-install /dev/sdX  # Replace sdX with the actual disk (like /dev/sda)
update-grub
```

Exit `chroot` mode, unmount the recovery path from live-boot OS and reboot the system:

```bash
exit
sudo umount -R /mnt/recovery
sudo reboot
```

Hope you found this article useful!