title: How to Delete Multiple Git Branches from the Command Line?
date: February 5th, 2025
slug: how-to-delete-multiple-git-branches-from-the-command-line
category: Git + VCS 
status: active

Whether you're cleaning up local branches after a feature merge or tidying up remote branches, here’s how you can do it.

## Deleting Multiple Local Branches

To delete multiple local branches safely (only if they’ve been merged), use:

```bash
git branch -d branch1 branch2 branch3
```

If the branches haven't been merged and you still want to delete them, force delete with:

```bash
git branch -D branch1 branch2 branch3
```

## Deleting Multiple Remote Branches

For remote branches, you can delete them by running:

```bash
git push origin --delete branch1 branch2 branch3
```

Alternatively, you can use the colon `:` syntax:

```bash
git push origin :branch1 :branch2 :branch3
```

## Deleting Multiple Branches Using a Pattern

If you want to delete branches that follow a naming pattern (like `feature/` branches), you can use `grep` and `xargs`:

### For local branches:

```bash
git branch | grep 'feature/' | xargs git branch -d
```

To force delete:

```bash
git branch | grep 'feature/' | xargs git branch -D
```

### For remote branches:

```bash
git branch -r | grep 'origin/feature/' | sed 's/origin\///' | xargs -I {} git push origin --delete {}
```

## Final Tips

- **List branches before deleting:** Use `git branch` for local and `git branch -r` for remote branches to verify which ones you’re about to delete.
- **Be cautious with force delete (`-D`):** It will remove branches even if they haven’t been merged, so make sure you won’t lose important work.

Hope you found this useful!