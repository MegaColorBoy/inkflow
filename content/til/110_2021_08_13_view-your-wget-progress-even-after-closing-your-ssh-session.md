title: View your wget progress even after closing your SSH session
date: August 13th, 2021
slug: view-your-wget-progress-even-after-closing-your-ssh-session
category: DevOps + wget
status: active

Few days back, I ran a `wget` command to download a file and accidentally closed the SSH client.

I logged in again and checked the list of active processes and thankfully, the `wget` process was still running except that I wasn't able to know the current progress of it.

So, I did a little research and found a way to view the progress, so I tried the following command:
```bash
tail -f wget_log
```

And, I was able to view it's current download progress again.

Hope this helps you out!