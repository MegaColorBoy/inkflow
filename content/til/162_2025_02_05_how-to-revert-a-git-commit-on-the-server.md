title: How to Revert a Git Commit on the Server?
date: February 5th, 2025
slug: how-to-revert-a-git-commit-on-the-server
category: Git + VCS 
status: active

Today I learned how to revert a Git commit after pulling it on a server. Whether you've made a mistake or just need to backtrack, Git offers several ways to undo commits depending on your situation. Here's a quick guide on how to handle it.

## If you haven't pushed the commit yet

If the commit hasn't been pushed to the remote repository, you can use `git reset` to undo it.

## Soft Reset (keeps changes staged)
```bash
git reset --soft HEAD~1
```
This moves the HEAD back by one commit but keeps your changes staged.

## Mixed Reset (keeps changes unstaged):
```bash
git reset --mixed HEAD~1
```
This moves the HEAD back by one commit and unstages your changes.

## Hard Reset (discards changes):
```bash
git reset --hard HEAD~1
```
This completely removes the last commit and discards any changes.

> **Tip:** Replace `HEAD~1` with `HEAD~2` to go back two commits, and so on.

## If you've already pushed the commit

### Revert the commit (safe for shared repos):
If you've already pushed the commit and want to undo it without rewriting history, use `git revert`. This creates a new commit that undoes the changes.

```bash
git revert <commit_hash>
```

Find the commit hash using:
```bash
git log --oneline
```

### Force Reset (i.e. if you're okay with rewriting history):
If you don't mind rewriting history (and no one else is working on the branch), you can force reset.

```bash
git reset --hard <commit_hash>
git push origin HEAD --force
```

<div class="post-notification">
    <h3>⚠️Warning</h3>
    <p>This is not recommended if others are working on the same branch as it can cause conflicts.</p>
</div>

## If you just pulled and want to undo

If you just pulled and want to undo the merge, you can reset to the previous state using `ORIG_HEAD`.

### Undo a merge pull:
```bash
git reset --hard ORIG_HEAD
```

This will bring your repository back to the state before the last pull.

### Final thoughts

Reverting commits can seem daunting at first, but once you understand the tools Git offers, it's pretty straightforward. Always double-check before using `--hard` or `--force` to avoid accidental data loss!

Hope this helps you get back on track!