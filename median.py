''' run treshold program '''

import cv2


low_bl = 3
IMG_READ = cv2.imread('lena-color.jpg')
median = IMG_READ

def update_median(new_val):
    ''' update value '''
    global low_bl
    low_bl = new_val
    render_view()

def render_view():
    global low_bl, median
    if low_bl < 3:
        median = IMG_READ
    if low_bl % 2 == 1:
        median = cv2.medianBlur(IMG_READ, low_bl)
    cv2.imshow('image', median)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('median', 'image', low_bl, 100, update_median)
render_view()
cv2.waitKey(0)
