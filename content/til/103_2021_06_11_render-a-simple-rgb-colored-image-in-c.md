title: Render a simple RGB colored image in C++
date: June 11th, 2021
slug: render-a-simple-rgb-colored-image-in-c
category: Graphics
status: active

<img src="../../../static/til_images/rgb-colored-spectrum.png" style="width: 500px; height: 300px;" />

Recently, I started reading a book called [The Graphics Codex](https://graphicscodex.courses.nvidia.com/app.html), it's an amazing book about Computer Graphics covering a lot of content and I find it quite resourceful. I wanted to build my own toy raytracer for the sake of exploring, so that's why I started to refresh my graphics coding knowledge a bit.

Just like any graphics renderer, in order to view your image. you must be able to write your image to a file, right?

Below, I wrote a really simple code to generate the entire RGB colored spectrum from top to bottom:

```cpp
#include <iostream>
using namespace std;

int main() {
    const int width = 800;
    const int height = 800;

    std::cout << "P3\n" << width << " " << height << "\n255\n";

    for(int j=height-1; j>=0; j--) {
        for(int i=0; i<width; i++) {
            auto r = double(i) / (width-1);
            auto g = double(j) / (height-1);
            auto b = 0.25;

            int ir = static_cast<int>(255.999 * r);
            int ig = static_cast<int>(255.999 * g);
            int ib = static_cast<int>(255.999 * b);

            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}
```

You can generate it by simply creating an executable like this:
```bash
g++ -o pixels pixels.cpp
```

Now, when you execute it by typing `./pixels`, you'll get a list of numbers that's pretty much a combination and permutation of RGB color values.

Lastly, to generate a colored image, like the one above, just redirect the output to an image format, in this example, I used PPM image format:

```bash
./pixels > image.ppm && xdg-open image.ppm
```

And that's it, you have generated your own colored image! &#x1F601;

Hope you found this useful!
