import cv2 as cv 

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

numberFaces = 0

while(True):

	ret, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = face_cascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	numberFaces = len(faces)

	print("There are this many people here: ", numberFaces)

	for (x, y, w, h) in faces:
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


	cv.imshow('frame', frame)

	if(cv.waitKey(1) & 0xFF == ord('q')):
		break





