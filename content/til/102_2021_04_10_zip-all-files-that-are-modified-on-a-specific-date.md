title: Zip all files that are modified on a specific date
date: April 10th, 2021
slug: zip-all-files-that-are-modified-on-a-specific-date
category: UNIX
status: active

I wrote a nifty command to make an archive of the files that I have modified on a particular date. By doing so, this script comes in handy during urgent deployments, so that I don't lose track of the files that I should be updating.

Here's the command at your disposal:

```bash
find . -maxdepth 10 -type f -newermt "2021-04-10" | zip -qur archive.zip -@
```

## How this works?
Let's see what this command does in pieces:

`find` is the utility tool used to return the filenames that match the specified parameters in the given directory.

`-maxdepth` is the flag that allows you to specify the depth of recursive searches it should perform.

`-type` is the flag that determines if you're looking for file or a directory.

`-newermt` is the flag that determines if the file has been modified on and/or after the given date.

Once, the file has been found, the output is being [redirected](https://www.geeksforgeeks.org/piping-in-unix-or-linux/) to the `zip` utility function, which would then add the files to the `.zip` file.
The `-q` flag would perform the operation in silent mode, `-u` flag would update the files in the archive if modified or add it as a new file if it doesn't exist and `-@` takes the list of files from the standard input.

If you want to ignore certain directories or file extensions, in that case, you can exclude them like so:

```bash
find . -maxdepth 30 -type f ! -path "./path/to/directory/*" !  -path "*.ext" -newermt "2021-04-10" | zip -qur archive.zip -@
```

Or, you can even archive the modified files by specifying a date range:

```bash
touch --date "2021-04-10" startdate
touch --date "2021-04-15" enddate
find . -maxdepth 30 -type f -newer startdate -not -newer enddate | zip -ur archive.zip -@
```

Hope you found this tip useful! &#x1F601;