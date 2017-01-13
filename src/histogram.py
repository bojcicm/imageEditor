'''Histogram stretching and equalization.'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

def im2double(input_img):
    ''' Divide all values by the largest possible value in the datatype '''
    info = np.iinfo(input_img.dtype)
    return input_img.astype(np.float) / info.max

def double2im(input_img):
    ''' Revert to uint8 from double '''
    return (255 * np.array(input_img)).astype(np.uint8)


def stretch(input_array, array_min, array_max):
    ''' apply stretch to every element of array '''
    iterator = np.nditer([input_array, None])
    for x_val, y_val in iterator:
        y_val[...] = ((x_val - array_min) * (1 / (array_max - array_min)))
    return iterator.operands[1]


def hist_stretch(ld_img):
    """Stretch histogram of image - lighter."""
    grayscale_img = cv2.cvtColor(ld_img, cv2.COLOR_BGR2GRAY)
    double_img = im2double(grayscale_img)
    arr_min = np.amin(double_img)
    arr_max = np.amax(double_img)
    out_img = stretch(double_img, arr_min, arr_max)
    return double2im(out_img)


def hist_equ(xarg):
    """Equalize histogram of image - darker."""
    return cv2.equalizeHist(xarg)

#code for execute

IMG_READ = cv2.imread('lena-color.jpg')
IMG_GRAY = cv2.cvtColor(IMG_READ, cv2.COLOR_BGR2GRAY)
IMG_HIST = hist_stretch(IMG_READ)
IMG_EQU = cv2.equalizeHist(IMG_GRAY)

plt.figure(1)
plt.subplot(311)
plt.hist(IMG_GRAY.flatten(), 256, [0,256], color = 'r')
plt.xlim([0,256])

plt.figure(1)
plt.subplot(312)
plt.hist(IMG_HIST.flatten(), 256, [0,256], color = 'g')
plt.xlim([0,256])

plt.figure(1)
plt.subplot(313)
plt.hist(IMG_EQU.flatten(), 256, [0,256], color = 'g')
plt.xlim([0,256])


cv2.imshow('images1', np.hstack((IMG_GRAY, IMG_HIST, cv2.equalizeHist(IMG_GRAY))))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
