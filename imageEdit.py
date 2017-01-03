import numpy as np
import cv2
from matplotlib import pyplot as plt

# !!! BGR Image !!!
IMG_READ = cv2.imread('transfer.png')

#koeficijenti razina boje
IMG_GRAY = cv2.cvtColor(IMG_READ, cv2.COLOR_BGR2GRAY)

HIST = cv2.calcHist([IMG_READ], [0], None, [256], [0, 256])

plt.hist(IMG_GRAY.ravel(), 256, [0, 256], cumulative=True)
cv2.imshow('bgr image', IMG_READ)
cv2.imshow('gray image', IMG_GRAY)
plt.show()


cv2.imshow('bgr image', IMG_READ)
cv2.imshow('gray image', IMG_GRAY)
cv2.waitKey(0)
cv2.destroyAllWindows()
