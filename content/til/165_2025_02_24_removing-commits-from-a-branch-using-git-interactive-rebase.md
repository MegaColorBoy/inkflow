title: Removing Commits from a Branch Using Git Interactive Rebase
date: February 24th, 2025
slug: removing-commits-from-a-branch-using-git-interactive-rebase
category: Git + VCS
status: active

I'm working on a project that had approximately five minor incident fixes. However, I got approval from the client side to push only three of them. Luckily, my commits are atomic, so making this build was easier than I thought.

At this moment, I decided to clone the latest branch into a temporary branch and roll back two commits for today's deployment while keeping the latest branch intact with all the fixes.

To achieve this, I used **Git interactive rebase**, a powerful tool for modifying commit history.

## Why Use Interactive Rebase?

Interactive rebase allows you to modify commit history, including:

- Removing unwanted commits
- Reordering commits
- Squashing multiple commits into one
- Editing commit messages

## How I Did It?

Here’s the step-by-step process I followed:

### 1. Clone the Branch

Before making any changes, I cloned the branch to have a backup:

```sh
git checkout -b my-cloned-branch original-branch
```

### 2. Start Interactive Rebase

To remove specific commits, I ran:

```sh
git rebase -i HEAD~N
```

Where `N` is the number of commits I wanted to review. This opened an editor displaying the most recent commits.

### 3. Modify the Commit List

The interactive rebase interface showed something like this:

```sh
pick abc123 Commit message 1
pick def456 Commit message 2
pick ghi789 Commit message 3
```

To **remove** a commit, I replaced `pick` with `drop`.

To **edit** or **squash** commits, I could replace `pick` with commands like `edit` or `squash`.

After making my changes, I saved and closed the editor.

### 4. Handle Any Conflicts (If Needed)

If Git encountered conflicts, it prompted me to resolve them. I fixed the files and continued the rebase:

```sh
git rebase --continue
```

## Key Takeaways

- Interactive rebase is powerful for cleaning up commit history.
- Always clone or create a backup branch before rebasing.
- If working with a team, communicate before modifying shared branches.

This was a great learning experience, and now I feel more confident managing Git history efficiently!

Hope you found this tip useful!
