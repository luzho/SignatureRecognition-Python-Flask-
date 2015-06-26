import cv2
import numpy as np
from matplotlib import pyplot as plt

def showImage(name):
	cv2.imshow('image',name)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#Invert->threshold(Mean)

#Load image
img = cv2.imread('planilla.jpg')
img = cv2.resize(img,(768,1024), interpolation = cv2.INTER_CUBIC)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
showImage(mean)
ret,thresh5 = cv2.threshold(mean,127,255,cv2.THRESH_BINARY_INV)
showImage(thresh5)
cv2.imwrite('im1.png',thresh5)


mean = cv2.adaptiveThreshold(gray_image, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
ret,thresh5 = cv2.threshold(mean,127,255,cv2.THRESH_BINARY_INV)
showImage(thresh5)

cv2.imwrite('im2.png',thresh5)




"""
# skeletonize the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
skeleton = imutils.skeletonize(gray, size=(4, 4))
showImage(skeleton)

#erode
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
showImage(erosion)
"""




