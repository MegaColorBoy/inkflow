title: Download a webpage along with it's assets using wget
date: July 17th, 2022
slug: download-a-webpage-along-with-its-assets-using-wget
category: wget + Linux
status: active

I wanted to download a webpage along with it's assets and scripts, I tried using Chrome's **Save as...** option but it wasn't working as expected.

I did a little googling and thought of using `wget` to do the job and it worked. Here's the command I used:

```bash
wget -p -k -H --nd https://www.example.com
```

Let's see what do those flags mean:

- `-p`: Downloads all the necessary files to properly display the downloaded HTML page.
- `-k`: After the download is complete, it converts the links in the document to make them suitable for local viewing.
- `-H`: This would download files that spans different hosts.
- `--nd`: While retrieving files recursively, it will not create a hierarchy of directories and downloads the files into a single directory instead.

If you open `index.html` directly on the browser, the assets might be broken as the `-k` flag doesn't seem to make the assets relative to the root directory. In order to view it, you can view it on a localhost server like WAMP, XAMPP or if you are using Python, you can type `python -m http.server` and view your downloaded file.

Might be a bit messy but gets the job done.