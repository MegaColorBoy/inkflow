title: Resize images from a file list using ImageMagick
date: January 2nd, 2026
slug: resize-images-from-a-file-list-using-imagemagick
category: Image Manipulation + Linux
status: active

Today, a colleague of mine uploaded a large number of images, only to realise later that they were all uncompressed and the site was loading noticeably slower. 

His first thought was to compress them and re-upload everything again—but why do something redundant when you can handle it easily from the terminal using ImageMagick?

Previously, I’ve written about how ImageMagick makes it easy to [resize images](https://www.megacolorboy.com/til/posts/playing-around-with-imagemagick/) in bulk. However, sometimes you don’t want to touch every image in a directory.

In cases like this, if you already know which images need resizing, you can list their filenames in a text file and let ImageMagick process only those.

Assume a `files.txt` like this:

```bash
image1.jpg
photo_02.png
banner.jpeg
```

You can then resize just those images while keeping the original aspect ratio intact and avoiding upscaling:

```bash
while IFS= read -r file; do
  [ -f "$file" ] && mogrify -resize 500x600\> "$file"
done < files.txt
```

This works well when cleaning up large media folders or fixing legacy content where only a subset of images needs adjustment.

Hope you found this tip useful!