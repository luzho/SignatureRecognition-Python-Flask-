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
img = cv2.resize(img,(768,1024), interpolation = cv2.INTER_LINEAR)
img = cv2.GaussianBlur(img,(3,3),0)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,75,10) #11,2
showImage(mean)
ret,thresh = cv2.threshold(mean,127,255,cv2.THRESH_BINARY_INV)
showImage(thresh)

kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(thresh,kernel,iterations = 1)
showImage(erosion)
cv2.imwrite('erosion.png',erosion)

image, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
indexMax = 0
x,y,w,h = cv2.boundingRect(contours[0])
maxArea = w*h

for i in range(0,len(contours)):
	cnt = contours[i]
	x,y,w,h = cv2.boundingRect(cnt)
	if maxArea < w*h:
		maxArea=w*h
		indexMax = i

cnt = contours[indexMax]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(erosion,(x,y),(x+w,y+h),(129,0,0),3)

showImage(erosion)
cv2.imwrite('erosion.png',erosion)


"""
#cv2.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]])
lines = cv2.HoughLinesP(erosion,1, np.pi/180, 2, 20, 50);
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

showImage(img)

cv2.imwrite('im1.png',thresh)

_,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print M
"""


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




