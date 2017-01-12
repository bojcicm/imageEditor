''' open, close image '''

import argparse
import numpy as np
import cv2

morph_type = 0
morph_elem = 2
morph_size = 3
morph_iter = 1

M_TYPES = {
    0 : cv2.MORPH_OPEN,
    1 : cv2.MORPH_CLOSE,
    2 : 'erode',
    3 : 'dilate',
}
M_ELEMS = {
    0 : cv2.MORPH_RECT,
    1 : cv2.MORPH_CROSS,
    2 : cv2.MORPH_ELLIPSE
}

def start_morph():
    kernel = cv2.getStructuringElement(
        M_ELEMS[morph_elem],
        (morph_size, morph_size))
    if morph_type < 2:
        dst = cv2.morphologyEx(
            IMG_READ,
            M_TYPES[morph_type],
            kernel,
            iterations=morph_iter)
    elif morph_type == 2:
        dst = cv2.erode(
            IMG_READ,
            kernel,
            iterations=morph_iter)
    elif morph_type == 3:
        dst = cv2.dilate(
            IMG_READ,
            kernel,
            iterations=morph_iter)
    cv2.imshow('morph', dst)


#end of main

def update_type(new_val):
    global morph_type
    morph_type = new_val
    start_morph()

def update_elem(new_val):
    global morph_elem
    morph_elem = new_val
    start_morph()

def update_size(new_val):
    global morph_size
    if new_val < 3:
        morph_size = 3
    else:
        morph_size = new_val
    start_morph()

def update_iter(new_val):
    global morph_iter
    if new_val < 1:
        morph_iter = 1
    else:
        morph_iter = new_val
    start_morph()

#set up commands

def set_window():
    cv2.namedWindow('morph', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('operation', 'morph', morph_type, 3, update_type)

    cv2.createTrackbar('element', 'morph', morph_elem, 2, update_elem)

    cv2.createTrackbar('size', 'morph', morph_size, 100, update_size)

    cv2.createTrackbar('iterations', 'morph', morph_iter, 100, update_iter)


def run_prog():
    set_window()
    start_morph()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ARG_PARS = argparse.ArgumentParser()
ARG_PARS.add_argument("-i", "--image", required=False,
                      help='''Full path to image''')
IMG = vars(ARG_PARS.parse_args())["image"]
if IMG:
    IMG_READ = cv2.imread(IMG)
else:
    IMG_READ = cv2.imread('lena-color.jpg')

run_prog()
