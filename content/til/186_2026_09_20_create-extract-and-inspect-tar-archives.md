title: Create, extract, and inspect tar archives
date: September 20th, 2026
slug: create-extract-and-inspect-tar-archives
category: Linux + DevOps
status: active

Whenever I need to bundle a directory before moving it between servers, `tar` is a useful tool to have around. I thought I'd write down the few commands I keep coming back to.

Let's say you have an `uploads` directory in your current location. To create a gzip-compressed archive:

```bash
tar -czf uploads.tar.gz uploads/
```

Here, `-c` creates the archive, `-z` uses gzip compression, and `-f` specifies the archive filename.

If the directory is somewhere else, you can use `-C` to choose the source directory without storing its entire path:

```bash
tar -czf uploads.tar.gz -C /var/www/html/public uploads/
```

These are alternative ways to create the same archive. Replace the paths with your own and choose the one that suits your situation.

Before extracting it, you can inspect the contents:

```bash
tar -tzvf uploads.tar.gz
```

For example, a listing might look like this:

```text
drwxr-xr-x devops/devops       0 2026-09-20 09:00 uploads/
-rw-r--r-- devops/devops    2048 2026-09-20 09:00 uploads/logo.png
-rw-r--r-- devops/devops    4096 2026-09-20 09:00 uploads/banner.jpg
```

The `-t` flag lists entries, and `-v` adds details such as permissions and sizes.

To extract into your current directory:

```bash
tar -xzvf uploads.tar.gz
```

Or extract into a specific directory, creating it first if needed:

```bash
mkdir -p ./restored
tar -xzvf uploads.tar.gz -C ./restored
```

This puts the files under `./restored/uploads/`. The `-x` flag extracts the archive, and verbose output might look like this:

```text
uploads/
uploads/logo.png
uploads/banner.jpg
```

I find it helpful to list the contents first so I know which directory structure to expect. Extracting into an empty directory also helps avoid overwriting existing files.

Hope you found this useful!
