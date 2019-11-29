import numpy as np
import sys


# This function expects an array of 3 values (RGB) in the range [0,1], and returns an array of three values:
# the first, Y, in range [0,1], the second, U, in range [-0.436,0.436], and the third, V, in range [-0.615,0.615].
def rgb_to_yuv(RGB):
    rgb2yuv = np.array([[0.2126, 0.7152, 0.0722],
                        [-0.09991, -0.33609, 0.436],
                        [0.615, -0.55861, -0.05639]])
    return np.dot(rgb2yuv, RGB)


# This function expects an array of 3 values (YUV) the first, Y, in range [0,1]], the second, U,
# in range [-0.436,0.436], and the third, V, in range [-0.615,0.615].
def yuv_to_rgb(YUV):
    yuv2rgb = np.array([[1, 0, 1.28033],
                        [1, -0.21482, -0.38059],
                        [1, 2.12798, 0]])
    return np.dot(yuv2rgb, YUV)


def print_error():
    print("Error in the input. There should be 4 arguments. \n"
          "First: rgb2yuv or yuv2rgb. \n"
          "Second: the three corresponding values \n"
          "Example: rgb2yuv 200 100 125")


if len(sys.argv) < 4:
    print_error()
    sys.exit(0)
else:
    if sys.argv[1] == "rgb2yuv":
        # Check the three values are in the accepted range
        if 0 <= int(sys.argv[2]) < 256 and 0 <= int(sys.argv[3]) < 256 and 0 <= int(sys.argv[4]) < 256:
            RGB = [int(sys.argv[2])/255, int(sys.argv[3])/255, int(sys.argv[4])/255]
            yuv = rgb_to_yuv(RGB)

            print("The Y value is: {:.2f} \n"
                  "The U value is: {:.2f} \n"
                  "The V value is: {:.2f}".format(yuv[0], yuv[1], yuv[2]))
        else:
            print_error()

    elif sys.argv[1] == "yuv2rgb":
        # Check the three values are in the accepted range
        if 0 < float(sys.argv[2]) <= 1 and -0.436 <= float(sys.argv[3]) <= 0.436 \
                and -0.615 <= float(sys.argv[4]) <= 0.615:
            YUV = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
            rgb = yuv_to_rgb(YUV)

            print("The R value is: {:.2f} \n"
                  "The G value is: {:.2f} \n"
                  "The B value is: {:.2f}".format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))
        else:
            print_error()
    else:
        print_error()
