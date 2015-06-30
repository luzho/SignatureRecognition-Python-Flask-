import cv2
import numpy as np
from matplotlib import pyplot as plt


im = cv2.imread('erosion.png')
img = cv2.GaussianBlur(img,(5,5),0)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#im = cv2.drawContours(im, contours, -1, (0,255,0), 3)

indexMax = 0
x,y,w,h = cv2.boundingRect(contours[0])
maxArea = w-x*h-y


for i in range(0,len(contours)):
	cnt = contours[i]
	x,y,w,h = cv2.boundingRect(cnt)
	print x,y,w,h
	img = cv2.rectangle(im,(x,y),(x+w,y+h),(129,0,0),3)
#im = cv2.drawContours(im, approx, -1, (0,255,0), 3)

showImage(im)

area = cv2.contourArea(cnt)
print area

