title: How to resolve the "fatal: refusing to merge unrelated histories" Git error?
date: April 10th, 2021
slug: how-to-resolve-the-fatal-refusing-to-merge-unrelated-histories-git-error
category: Git
status: active

This error shows up when two different projects are merged (i.e. they both could be the same project but unaware of each other's existence and have different commit histories).

If you are facing this, chances are that:

1. You must have cloned a project and the `.git` directory must have corrupted or got deleted and at this point, Git is unaware of the changes being made and will throw this error when you try to *push to* or *pull from* the remote repository.

2. You created a new repository, made some changes and added the commits and then you tried to pull from the remote repository.

Well, you can easily resolve by passing the `--allow-unrelated-histories` flag when pulling the latest updates from the remote repository:

```bash
git pull origin master --allow-unrelated-histories
```

Hope you found this useful!