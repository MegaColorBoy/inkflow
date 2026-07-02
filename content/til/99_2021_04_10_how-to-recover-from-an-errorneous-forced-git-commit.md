title: How to recover from an errorneous forced git commit?
date: April 10th, 2021
slug: how-to-recover-from-an-errorneous-forced-git-commit
category: Git
status: active

If you're the type of person who types `git push -f origin master`, please don't do that as it might overwrite your entire branch. I'm saying this because I did this once and I thought I lost all the files.

Luckily, I was a bit relieved as `git` is a VCS (Version Control Software), which means the files are most likely not **deleted**. This is when I came across `git reflog` command.

According to the [Git manual](https://git-scm.com/docs/git-reflog), this is what it does:

> Reference logs, or "reflogs", record when the tips of branches and other references were updated in the local repository.

This is a life-saver especially if you wanted to return back to the previous point in time. Here's how I recovered my files back again:

1. Type `git reflog show remotes/origin/master`
2. Find and make note of the previous commit hash.
3. Create a new branch with using the previous commit hash like this: `git branch <new_branch_name> <previous_commit_hash>`
4. Then finally, push the files to the new branch: `git add . && git commit -m "pushing recovered files" && git push origin <new_branch_name>`
4. Checkout to the newly created branch: `git checkout <new_branch_name>`
5. Delete the corrupted branch and replace it with the newly created branch that contains your restored files.

If I didn't discover this, I don't really know what I would have done to recover those files.

## References

- [Git reflog documentation](https://git-scm.com/docs/git-reflog)
- [How can I recover from an erronous git push -f origin master?](https://stackoverflow.com/questions/3973994/how-can-i-recover-from-an-erronous-git-push-f-origin-master)

Hope this helps you out!