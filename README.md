# Lab 1
This is the first lab from the sibject of Audio and video encoding systems. The main goal is to get used to using python and ffmpeg.

## Exercise 1
This first exercise consists on writing a python script capable of translating 3 RGB values into YUV values and
vice versa. The transformation used in this part is the one defined in the [HDTV BT.709 standard.](https://en.wikipedia.org/wiki/YUV#HDTV_with_BT.709)

### Execution
In order to run this exercise, the user must pass 4 arguments: the mode (from what to what to translate the values), and the 3 corresponding input values.

Some examples:

To transform from RGB to YUV colorspace, e.g a purple, RGB (150, 50, 200), use the following command:
`python3 app/rgb_yuv.py rgb2yuv 150 50 200`

To do the inverse transformation: from yuv to rgb, e.g. a green, YUV (0.73, -0.25, -0.26), us the following command:
`python3 app/rgb_yuv.py yuv2rgb 0.73 -0.25 -0.26`

## Exercise 2
The aim of this exercise is to use ffmpeg to resize an image into a lower quality. In this case we have used the Lenna image.

In our case, the original image is 521x512 pixels, so if we want to resize it, for example to 128x128 we just need to 
run a simple line in the terminal: 
`ffmpeg -i examples/lenna.png -vf scale=128:128 examples/lenna128.png`

Regarding the results it is easy to see that if we put both images at the same size, the one with the lowest resolution 
looks much more blurry, whereas the original keeps its sharpness.

Original image: 

![](/examples/lenna.png)

Resized image: 

![](/examples/lenna128.png =512x512)

## Exercise 3a
This exercises consists on creating a script that reads a matrix, or an image, in a serpentine way.

This code can be run in two ways: with a simple hardcoded matrix, or by specifying an image file location.

For the first way write in the command line: `python3 app/serpentine.py`

For the other mode, for example using the lenna image from the previous exercise, just execute: 
`python3 app/serpentine.py examples/lenna.png`

## Exercise 3b
In this exercise we need to use ffmpeg in order to transform an image top b/w.

For example, to transform the lenna image to b/w it can be done by running in the terminal: 
`ffmpeg -i examples/lenna.png -vf hue=s=0 -c:a copy examples/lennabw.png`

Furthermore, we can also specify the level of compression at which we want to perform the operation. By default it is 
set to 100, which is maximum compression, thus minimum file size. To run the b/w transformation with a custom compression
value, e.g 0, we can run: `ffmpeg -i examples/lenna.png -vf hue=s=0 -compression_level 0 -c:a copy examples/lennabw0.png`

Regarding the results, we can see that there is no noticeable difference, which makes sense as it is a lossless compression.

Black and white photo with maximum compression (default): 

Black and white photo with minimum compression:

## Exercise 4
This last exercise aims to create a script capable of applying run-length encoding to a given sequence. For the sake
of simplicity of the execution I've used a sequence of letters. The code can also accept sequences of numbers.

To run the code use: `python3 app/ex4.py` or if you want to specify a sequence, e.g. aaaeeeeeiii use: `python3 app/ex4.py aaaeeeeeiii` 
