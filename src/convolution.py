''' Apply convolution/correlation filter to image '''

import argparse
import cv2
import numpy as np

FILTERS = {
    'low-pass' : np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float32),
    'gauss' : np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32),
    'low-seven' : np.ones((7, 7), np.float32),
    'laplace' : np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32),
    'sharpening' : np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
}
fil_val = 1

def apply_filter(filter_id, image):
    ''' Apply filter depending on ID sent '''
    return {
        'low-pass' : run_filter(image, 'low-pass'),
        'gauss' : run_filter(image, 'gauss'),
        'low-seven' : run_filter(image, 'low-seven'),
        'laplace' : run_filter(image, 'laplace'),
        'sharpening' : run_filter(image, 'sharpening')
    }.get(filter_id, image)

def run_filter(image, sel_filter='low-pass'):
    ''' Apply filter to image '''
    if sel_filter == 'laplace':
        filt_array = FILTERS[sel_filter] * fil_val
    elif sel_filter == 'low-pass':
        filt_array = np.ones((fil_val, fil_val), np.float32) / (fil_val*fil_val)
    elif sel_filter == 'sharpening':
        filt_array = FILTERS[sel_filter] * fil_val
    else:
        filt_array = FILTERS[sel_filter] / fil_val
    return cv2.filter2D(image, -1, filt_array)

def update_filter(new_val):
    global fil_val, ADJUSTED
    if new_val < 1:
        fil_val = 1
    else:
        fil_val = new_val
    ADJUSTED = apply_filter(SELECTED_FILTER, IMG_READ)
    cv2.putText(ADJUSTED, "filter:{}".format(SELECTED_FILTER), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (125, 125, 125), 2)
    cv2.imshow(SELECTED_FILTER, np.hstack([IMG_READ, ADJUSTED]))


def run_prog():
    cv2.namedWindow(SELECTED_FILTER, cv2.WINDOW_NORMAL)
    cv2.createTrackbar('filter intensity', SELECTED_FILTER, fil_val, 100, update_filter)
    update_filter(0)
    cv2.waitKey(0)


ARG_PARS = argparse.ArgumentParser()
ARG_PARS.add_argument("-f", "--filter", required=True,
                      help='''
                      filter to apply to image. 
                      filters : low-pass, gauss, low-seven, laplace, sharpening
                      ''')
SELECTED_FILTER = vars(ARG_PARS.parse_args())["filter"]
IMG_READ = cv2.imread('lena-color.jpg')
ADJUSTED = apply_filter(SELECTED_FILTER, IMG_READ)
run_prog()
