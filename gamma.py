''' Gamma correction of immage from 0 to 3 '''

import cv2
import numpy as np

def adjust_gamma(image, gamma=1.0):
    ''' Create gamma value lookup table and apply to image'''
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def run_gamma():
    ''' run gamma '''
    img_read = cv2.imread('lena-color.jpg')
    for gamma_val in np.arange(0.0, 3.5, 0.5):
        if gamma_val == 1:
            continue
        gamma_val = gamma_val if gamma_val > 0 else 0.1
        adjusted = adjust_gamma(img_read, gamma=gamma_val)
        cv2.putText(adjusted, "g={}".format(gamma_val), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv2.imshow("Images", np.hstack([img_read, adjusted]))
        cv2.waitKey(0)

run_gamma()
