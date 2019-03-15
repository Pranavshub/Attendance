import cv2 as cv
import os

cap = cv.VideoCapture(0)

while(True):

	ret, frame = cap.read()


	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		path = 'C:/Users/prana/Documents/ComputerVision/Create-Face-Data-from-Images-master/images'
		cv.imwrite(os.path.join(path, 'faces2.png'), frame)
		break

cap.release()