import cv2
import numpy as np

img = cv2.imread('erosion.png')
img = cv2.GaussianBlur(img,(3,3),0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

showImage(img)
