title: How to use GitHub Personal Access Token to authenticate your git commits?
date: August 13th, 2021
slug: how-to-use-github-personal-access-token-to-authenticate-your-git-commits
category: Git
status: active

On November 2020, GitHub had announced that they would no longer accept basic username/password to authenticate git commits and it would be deprecated by Mid 2021.

Instead, they recommend you to authenticate your git commits using a Personal Access Token from your GitHub account.

## Generate a personal access token

1. Unset your credentials from your remote repository: `git config --local --unset credential.helper`
2. Login to your GitHub account and go to *Settings* 
3. Then navigate to *Developer Settings -> Personal Access Tokens*
4. Click on *Generate new token*
5. Give a name to your Personal Access Token and the necessary permissions required.
6. Once done, hit on *Generate token*
7. The token will be shown once, so make sure to copy it and store it somewhere that you can remember.

## Update your remote repository
Once you've generated a token, you just have to update your remote repository by following the below steps:

### 1. Update remote repository URL
```bash
git remote set-url origin https://&lt;your_access_token&gt;@github.com/&lt;your_git_repo_url&gt;
```

### 2. Just git pull once
Now, just perform `git pull` operation once and you should be good:
```bash
git pull https://&lt;your_access_token&gt;@github.com/&lt;your_git_repo_url&gt;
```

Hope this helps you out!