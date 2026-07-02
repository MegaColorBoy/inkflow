title: A Faster Way to Apply Linux Permissions for Large Laravel Projects Using xargs and find
date: January 12th, 2025
slug: a-faster-way-to-apply-linux-permissions-for-large-laravel-projects-using-xargs-and-find
category: Linux + DevOps + Laravel
status: active

Today, I learned a more efficient way to apply Linux permissions to large projects by leveraging the power of `xargs` and `find`. This method is particularly useful when dealing with Laravel projects that have many files and directories, as it allows for parallel processing and excludes specific folders (like a `storage` directory) from the permission changes.

Here’s the step-by-step process I followed:

## 1. Set Ownership of the Entire Project Folder

To ensure the correct ownership for the entire project, I used the `chown` command recursively:

```bash
sudo chown -R [username]:[groupname] [foldername]
```

This command sets the owner and group for all files and directories within the specified folder.

## 2. Set Permissions for the Project Folder and Its Top-Level Directories

Next, I applied the desired permissions to the project folder and its top-level directories using `chmod`:

```bash
sudo chmod 2775 [foldername]
```

The `2775` permission sets the folder to allow read, write, and execute for the owner and group, and read and execute for others. The `2` enables the **setgid bit**, which ensures that new files and directories inherit the group of the parent folder.

## 3. Find and Change Permissions for All Directories (Except the Storage Folder) in Parallel

To apply permissions to all directories while excluding the `storage` folder, I combined `find`, `xargs`, and `chmod`:

```bash
find [foldername] -path [foldername]/storage -prune -o -type d -print0 | sudo xargs -0 -P 2 chmod 2775

```

- `find [foldername] -path [foldername]/storage -prune -o -type d`: Finds all directories except the `storage` folder.
- `-print0`: Outputs the results in a null-terminated format to handle spaces in filenames.
- `xargs -0 -P 2`: Processes the results in parallel (2 processes at a time) for faster execution.
- `chmod 2775`: Applies the desired permissions to the directories.

## 4. Find and Change Permissions for All Files (Except the Storage Folder) in Parallel

Similarly, I applied permissions to all files while excluding the `storage` folder:

```bash
find [foldername] -path [foldername]/storage -prune -o -type f -print0 | sudo xargs -0 -P 2 chmod 0664
```

- `-type f`: Finds all files.
- `chmod 0664`: Sets read and write permissions for the owner and group, and read-only for others.

## 5. Handle the Storage Folder Separately (If It’s Too Large)

For the `storage` folder, I applied permissions separately to avoid overloading the system:

```bash
find [foldername]/storage -type d -print0 | sudo xargs -0 -P 2 chmod 2775
find [foldername]/storage -type f -print0 | sudo xargs -0 -P 2 chmod 0664
```

This ensures that the `storage` folder and its contents have the correct permissions without affecting the rest of the project.

## Why This Approach?

Using `xargs` with `-P` allows for parallel processing, which speeds up permission changes significantly for large projects. Additionally, excluding specific folders (like `storage`) ensures that sensitive or frequently accessed directories are handled separately.

This method has saved me a lot of time and effort when managing permissions for large projects.

Hope you found this article useful!