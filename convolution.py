''' Apply convolution/correlation filter to image '''

import argparse
import cv2
import numpy as np

FILTERS = {
    'low-pass' : np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float32),
    'gauss' : np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32),
    'low-seven' : np.ones((7, 7), np.float32),
    'laplace' : np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
}

def apply_filter(filter_id, image):
    ''' Apply filter depending on ID sent '''
    return {
        'low-pass' : run_filter(image, 'low-pass', 9),
        'gauss' : run_filter(image, 'gauss', 16),
        'low-seven' : run_filter(image, 'low-seven', 49),
        'laplace' : run_filter(image, 'laplace', 1)
    }.get(filter_id, image)

def run_filter(image, sel_filter='low-pass', coef=1):
    ''' Apply filter to image '''
    filt_array = FILTERS[sel_filter] / coef
    return cv2.filter2D(image, -1, filt_array)


ARG_PARS = argparse.ArgumentParser()
ARG_PARS.add_argument("-f", "--filter", required=True,
                      help="filter to apply to image")
SELECTED_FILTER = vars(ARG_PARS.parse_args())["filter"]

IMG_READ = cv2.imread('lena-color.jpg')
ADJUSTED = apply_filter(SELECTED_FILTER, IMG_READ)
cv2.putText(ADJUSTED, "filter:{}".format(SELECTED_FILTER), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (125, 125, 125), 2)
cv2.imshow("Images", np.hstack([IMG_READ, ADJUSTED]))
cv2.waitKey(0)
