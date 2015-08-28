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
def convert(fileIn, fileOut):
	os.system('convert '+fileIn+ ' ' +fileOut)
	img = cv2.imread(fileOut)
	img = cv2.resize(img,(816,1056),interpolation = cv2.INTER_LINEAR)
	cv2.imwrite(fileOut,img)

def removeBackground(image):
	tmp = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	alpha = cv2.adaptiveThreshold(tmp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
	#ret,alpha = cv2.threshold(tmp,200,255,cv2.THRESH_BINARY_INV)
	b, g , r = cv2.split(image)
	b = cv2.adaptiveThreshold(b, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	g = cv2.adaptiveThreshold(g, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	r = cv2.adaptiveThreshold(r, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	dst = cv2.merge ((b,g,r,alpha))
	blur = cv2.GaussianBlur(dst,(1,1),0)
	return blur

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
	crop_img = img[y+8: y+(h-8), x+8:x+(w-8)]

	#Second contour with higher area
	cnt2 = contoursSorted[1]
	xn,yn,wn,hn = cv2.boundingRect(cnt2)
	crop_img1 = img[yn+8: yn+(hn-8), xn+8:xn+(wn-8)]

	return (removeBackground(crop_img),removeBackground(crop_img1))

#sig1,sig2=getSignatures("doc.jpg")
#cv2.imwrite("1.png",sig1)
#cv2.imwrite("2.png",sig2)

