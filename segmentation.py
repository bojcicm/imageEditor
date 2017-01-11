''' Select values, segment image '''

import cv2
import numpy as np

IMG_READ = cv2.imread('lena-color.jpg')
IMG_GRAY = cv2.cvtColor(IMG_READ, cv2.COLOR_BGR2GRAY)
low_tresh = 0
high_tresh = 255
hist_height = 255
hist_width = 256
nbins = 32
bin_width = hist_width/nbins

def threshold(pixel_val):
    ''' apply threshold to pixel value '''
    if pixel_val > high_tresh:
        return 255
    elif pixel_val < low_tresh:
        return 0
    else:
        return pixel_val


def run_treshold():

    table = np.array([threshold(i) for i in np.arange(0, 256)]).astype("uint8")
    dst = cv2.LUT(IMG_GRAY, table)

    #res, dst = cv2.adaptiveThreshold(IMG_GRAY, low_tresh, high_tresh, cv2.THRESH_BINARY)

    cv2.imshow('image', dst)
    run_histogram(dst)

def run_histogram(new_image):
    ''' render histogram '''
    h = np.zeros((hist_height, hist_width))
    #Create array for the bins
    bins = np.arange(nbins, dtype=np.int32).reshape(nbins, 1)
    #Calculate and normalise the histogram
    hist_item = cv2.calcHist([new_image], [0], None, [nbins], [0, 256])
    cv2.normalize(hist_item, hist_item, hist_height, cv2.NORM_MINMAX)
    hist = np.int32(np.around(hist_item))
    pts = np.column_stack((bins, hist))
    #Loop through each bin and plot the rectangle in white
    for x, y in enumerate(hist):
        cv2.rectangle(h, (x*bin_width, y), (x*bin_width + bin_width-1, hist_height), (255), -1)
    #Flip upside down
    h=np.flipud(h)
    #Show the histogram
    cv2.imshow('colorhist',h)

def update_low_tresh(low_tresh_new_val):
    global low_tresh
    low_tresh = low_tresh_new_val
    run_treshold()

def update_high_tresh(high_tresh_new_val):
    global high_tresh
    high_tresh = high_tresh_new_val
    run_treshold()

def run_prog():
    ''' run treshold program '''
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('low', 'image', low_tresh, 255, update_low_tresh)
    cv2.createTrackbar('high', 'image', high_tresh, 255, update_high_tresh)
    run_treshold()
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

run_prog()