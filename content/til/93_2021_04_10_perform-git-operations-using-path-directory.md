title: Perform Git operations using path directory
date: April 10th, 2021
slug: perform-git-operations-using-path-directory
category: Git
status: active

The `-C` flag means the path of the directory and using this flag, you can perform any Git operations outside the project's directory without having to enter the directory all the time:

```bash
git -C /path/to/directory <command>
```

Hope this tip helps you out!