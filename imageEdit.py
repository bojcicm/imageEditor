import numpy as np
import cv2
#from matplotlib import pyplot as plt

# !!! BGR Image !!! 
image = cv2.imread('transfer.png')

#koeficijenti razina boje
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('bgr image',image)
cv2.imshow('gray image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()