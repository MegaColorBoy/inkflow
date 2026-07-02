title: Fetch selected files from your remote repository
date: April 10th, 2021
slug: fetch-selected-files-from-your-remote-repository
category: Git
status: active

Wanted to fetch a specific file from your Git repository except that the repository doesn't exist in your local machine?

Try this out:

```bash
git init
git remote add origin &lt;your_repo_link&gt;.git
git fetch
git checkout &lt;your_branch_name&gt; -- &lt;/path/to/file&gt;
```

After executing these commands, you should be able to see the selected directory/file in your project directory.

Hope you found this useful!