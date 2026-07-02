title: Playing around with ImageMagick
date: January 15th, 2023
slug: playing-around-with-imagemagick
category: Image Manipulation
status: active

ImageMagick is not a new tool for me but I haven't really talked about how it comes in handy whenever I wanted to resize and/or compress images efficiently using the terminal instead of using some image conversion service found for free online.

To get started, make sure you install ImageMagick on your machine. This is the command I use for Fedora Linux:

```bash
sudo dnf install ImageMagick
```

For example, if you wanted to compress an image's quality to 80%, here's you can do it:
```bash
convert -quality 80% src.png dest.png
```

Great! What if you want to do it for hundreds of images in a directory, then you can easily do something like this:

```bash
find . -type f -name '*.png' -exec bash -c 'convert -quality 80% "$1" "${1%}_compressed.png" ' bash  {} \;
```

You can do the same to resize the images while keeping original aspect ratio intact:


```bash
convert -resize 450x450 src.png dest.png
```

And similar to the one above, you can do the same for multiple images like so:

```bash
find . -type f -name '*.png' -exec bash -c 'convert -resize 450x450 "$1" "${1%}_resized.png" ' bash  {} \;
```

I have just scraped the surface of this image manipulation tool and if you are interested to know more, read the official [manpage](https://linux.die.net/man/1/imagemagick) on how to use it.

Hope you found this tip useful!
