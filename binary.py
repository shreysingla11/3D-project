import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(True):
	_, frame=cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('capture.png',frame)
		break

cap.release()
cv2.destroyAllWindows()

def nothing(x):
	print(x)

img=cv2.imread('capture.png',0)

cv2.namedWindow('image')
cv2.createTrackbar('brightness','image',0,255,nothing)

while(True):
	cv2.imshow('image',img)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
	p=cv2.getTrackbarPos('brightness','image')

	_, th1=cv2.threshold(img,p,255,cv2.THRESH_BINARY)
	cv2.imshow('output',th1)

cv2.destroyAllWindows()


