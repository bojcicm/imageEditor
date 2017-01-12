''' Load 2 images and combine them using opacity '''

import argparse
import numpy as np
import cv2

fil_val = 1

def update_opacity(new_val):
    global fil_val
    if new_val < 1:
        fil_val = 1
    else:
        fil_val = new_val
    alpha = 1.0 - (float(fil_val) / 100.0)
    alpha2 = 1 - alpha
    new_img = cv2.addWeighted(IMG_READ, alpha, IMG_READ2, alpha2, 0)
    cv2.imshow('opacity', np.hstack([IMG_READ, IMG_READ2, new_img]))

def run_prog():
    cv2.namedWindow('opacity', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('opacity', 'opacity', fil_val, 100, update_opacity)
    update_opacity(fil_val)
    cv2.waitKey(0)

ARG_PARS = argparse.ArgumentParser()
ARG_PARS.add_argument("-i1", "--image1", required=False,
                      help='''Full path to image1''')
ARG_PARS.add_argument("-i2", "--image2", required=False,
                      help='''Full path to image2''')
IMG = vars(ARG_PARS.parse_args())["image1"]
if IMG:
    IMG_READ = cv2.imread(IMG)
else:
    IMG_READ = cv2.imread('lena-color.jpg')
IMG = None
IMG = vars(ARG_PARS.parse_args())["image2"]
if IMG:
    IMG_READ2 = cv2.imread(IMG)
else:
    IMG_READ2 = cv2.imread('lena-color2.jpg')

run_prog()