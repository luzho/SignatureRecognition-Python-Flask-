import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

#Show image
def showImage(name):
	cv2.imshow('image',name)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#Convert file to whatever type to another type, preferably images
def convert(filein, fileout):
	os.system('convert '+filein+ ' ' +fileout)
	img = cv2.imread(fileout)
	img = cv2.resize(img,(816,1056),interpolation = cv2.INTER_LINEAR)
	cv2.imwrite(fileout,img)

def removeBackground(image):
	tmp = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	ret,alpha = cv2.threshold(tmp,160,255,cv2.THRESH_BINARY_INV)
	b, g , r = cv2.split()
	dst = cv2.merge ((b,g,r,alpha))
	return dst

#Get 2 signatures from PDF file
def getSignatures(filename):

	#Load file
	img = cv2.imread(filename)
	img = cv2.resize(img,(768,1024), interpolation = cv2.INTER_LINEAR)
	
	#Apply Filters 
	img = cv2.GaussianBlur(img,(3,3),0) 
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	mean = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,75,10) #11,2
	ret,thresh = cv2.threshold(mean,127,255,cv2.THRESH_BINARY_INV)
	kernel = np.ones((4,4),np.uint8)
	erosion = cv2.erode(thresh,kernel,iterations = 1) 
	
	#Get all contours of the image
	image, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

	#Ordered contours by Area... From the highest to the lowest area 
	contoursSorted = sorted(contours, key=cv2.contourArea, reverse=True)

	#First contour with higher area
	cnt = contoursSorted[0]
	x,y,w,h = cv2.boundingRect(cnt)

	#Second contour with higher area
	cnt2 = contoursSorted[1]
	xn,yn,wn,hn = cv2.boundingRect(cnt2)

	#Get 2 image with higher area
	img = cv2.imread("temp.jpg")
	crop_img = img[y+12: y+(h+3), x+12:x+(w+5)] # Crop from x, y, w, h -> 100, 200, 300, 400
	crop_img1 = img[yn+25: yn+(hn+10), xn+12:xn+(wn+5)]



	return (removeBackground(crop_img),removeBackground(crop_img1))
