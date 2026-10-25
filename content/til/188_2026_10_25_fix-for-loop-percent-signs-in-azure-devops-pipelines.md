title: Fix FOR loop percent signs in Azure DevOps pipelines
date: October 22nd, 2026
slug: fix-for-loop-percent-signs-in-azure-devops-pipelines
category: Azure DevOps + Windows + Troubleshooting
status: active

One day, a vendor told me they couldn't push updates to staging because the release pipeline was failing while extracting ZIP artifacts.

The error looked like this:

```text
i" -C "...\extracted" was unexpected at this time.
Cmd.exe exited with code '255'.
```

At first glance, the command looked fine:

```bash
for /r "drop" %i in (*.zip) do tar -xf "%i" -C "drop\extracted"
```

The part I'd missed was where the command was running. On Windows, Azure DevOps Command Line tasks put inline scripts into a temporary `.cmd` file. The [Microsoft task documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/command-line?view=azure-devops) describes this behavior.

Windows CMD uses `%i` for a `FOR` variable in an interactive session, but `%%i` in a batch script. That applies both when declaring the variable and when using it inside the loop.

So the corrected script was:

```bash
if not exist "drop\extracted" mkdir "drop\extracted"
for /r "drop" %%i in (*.zip) do tar -xf "%%i" -C "drop\extracted"
```

Here, `drop` is relative to the task's working directory. This assumes the Windows agent has a `tar` executable that supports ZIP extraction and that the output directory is dedicated to these artifacts. Archives with matching filenames can overwrite each other's extracted files.

After changing both occurrences to `%%i`, the deployment succeeded.

It was a small difference, but one I'll remember the next time a command works in a terminal and fails in a pipeline.

Hope you found this useful!
