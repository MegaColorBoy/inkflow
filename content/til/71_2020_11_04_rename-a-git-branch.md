title: Rename a Git Branch
date: November 4th, 2020
slug: rename-a-git-branch
category: Git
status: active

Using branches are one of the most powerful features of Git and becomes a part of the software development process.

Last night, I came across an issue where I created a new branch and committed my changes until the `git` tool rejected it because the branch was already created by someone else in the repository.

Luckily, I was able to resolve this issue by renaming my branch using `git branch -m` command.

Here's a short guide on how you can do that too!

## 1. Switch to the remote branch you want to rename
```bash
git checkout &lt;your_old_branch&gt;
```

## 2. Rename the current remote branch
```bash
git branch -m &lt;your_new_branch&gt;
```

Proceed to the next step, if you've pushed your old branch to the remote repository.

## 3. Push the renamed remote branch 
```bash
git push origin -u &lt;your_new_branch&gt;
```

## 4. Delete the old remote branch
```bash
git push origin --delete &lt;your_old_branch&gt;
```

If you've come this far without any issues, you've successfully renamed your local and remote Git branch.

Hope you found this useful!