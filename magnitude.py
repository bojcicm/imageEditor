''' get image gradient magnitude and orientation '''

import argparse
import cv2
import numpy as np


def getGradientMagnitude(im):
    "Get magnitude of gradient for given image"
    ddepth = cv2.CV_32F
    dx = cv2.Sobel(im, ddepth, 1, 0)
    dy = cv2.Sobel(im, ddepth, 0, 1)
    dxabs = cv2.convertScaleAbs(dx)
    dyabs = cv2.convertScaleAbs(dy)
    mag = cv2.addWeighted(dxabs, 0.5, dyabs, 0.5, 0)
    return mag

ARG_PARS = argparse.ArgumentParser()
ARG_PARS.add_argument("-i", "--image", required=False,
                      help='''Full path to image''')
IMG = vars(ARG_PARS.parse_args())["image"]

if IMG:
    IMG_READ = cv2.imread(IMG)
else:
    IMG_READ = cv2.imread('lena-color.jpg')

MAG = getGradientMagnitude(IMG_READ)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', np.hstack([IMG_READ, MAG]))
cv2.waitKey(0)
cv2.destroyAllWindows()
