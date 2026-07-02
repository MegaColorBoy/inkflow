title: How to Cherry-Pick Commits from One Git Branch to Another?
date: January 18th, 2025
slug: how-to-cherry-pick-commits-from-one-git-branch-to-another
category: Git + VCS
status: active

Although I had heard of Git's `cherry-pick` command, I never used it until a few months ago when I encountered a situation that demanded it. A client required us to work on multiple incidents and change requests (CRs), but they only wanted specific, approved updates pushed to the repository.

This created a challenge, especially when I was simultaneously working on CRs and incidents. I needed a way to isolate and push only the approved changes while keeping the rest intact. That’s when I decided to try out Git’s `cherry-pick` command—and it worked like a charm! It made managing my codebase much easier.

Here’s a simple walkthrough of how you can use it too:

## The Scenario

I had two branches in my Git repository:

- **Branch A**: The primary branch where ongoing development happens.
- **Branch B**: A feature branch where I accidentally pushed updates that should partially go into **Branch A**.

While it’s straightforward to merge changes from one branch into another, I only needed a subset of the commits from **Branch B** to be applied to **Branch A**. This is where Git’s `cherry-pick` command shines.

Go along with me and follow it step-by-step:

## 1. Switch to the Target Branch

First, check out the branch where you want to apply the commits (in my case, **Branch A**):

```bash
git checkout A
```

## 2. Find the Commits to Cherry-Pick

Use the `git log` command to list the commits in **Branch B** and identify the specific commit hashes you want to cherry-pick:

```bash
git log B
```

You should see output similar to this:

```bash
commit abc1234 (HEAD -> B)
Author: Your Name <you@example.com>
Date:   Mon Jan 1 12:00:00 2025 +0000

    Add feature X

commit def5678
Author: Your Name <you@example.com>
Date:   Sun Dec 31 12:00:00 2024 +0000

    Fix bug Y
```

Take note of the commit hash(es) you need. For example, let’s say you want to cherry-pick `abc1234` and `def5678`.

## 3. Cherry-Pick the Commit(s)

### Single Commit

To apply a single commit from **Branch B** onto **Branch A**, use:

```bash
git cherry-pick abc1234
```

### Multiple Commits

To apply multiple non-contiguous commits, list their hashes:

```bash
git cherry-pick abc1234 def5678
```

### Range of Commits

To cherry-pick a range of contiguous commits, use the `^..<` notation:

```bash
git cherry-pick def5678^..abc1234
```

This includes all commits from `def5678` to `abc1234`, inclusive.

## 4. Resolve Any Conflicts

If there are conflicts during the cherry-picking process, Git will pause and notify you. Resolve the conflicts in your files, then mark them as resolved:

```bash
git add <file>
```

Continue the cherry-pick process:

```bash
git cherry-pick --continue
```

To abort the cherry-pick if things go wrong:

```bash
git cherry-pick --abort
```

5. Verify the Result

Once the cherry-picking is complete, you can inspect your branch to ensure the changes were applied:

```bash
git log
```

You should see the cherry-picked commits in **Branch A**.

## When is cherry-picking useful?

Cherry-picking is perfect when you need specific commits from another branch without merging all its changes. This is especially helpful in scenarios like:

- Applying a bug fix from a feature branch to the main branch.
- Pulling specific updates without merging unrelated work.

## Bonus Tips

- Always double-check commit hashes before cherry-picking to avoid unexpected results.
- Use descriptive commit messages to make it easier to identify what each commit does
- If you find yourself cherry-picking often, consider rethinking your branch workflows to reduce the need for it.

That’s it! Now you know how to cherry-pick commits in Git. It’s a small but incredibly powerful tool to keep in your Git arsenal.