import cv2 as cv
import cognitive_face as cf
import os
import matplotlib.pyplot as plt
import urllib
import numpy as np 

directory = os.path.dirname(__file__)
base_dir = os.path.dirname(os.path.abspath(__file__))

key = 'f2e4d43835444a9aad29cbd8a9387c06'

cf.Key.set(key)

for file in os.listdir(directory + "images"):

	file_name, file_extension = os.path.splitext(file)

	pic_url = base_dir + "\\images\\" + file_name + file_extension # gets the url of the image that the webcam obtained
	print(pic_url)

	pic_result = cf.face.detect(pic_url) # gets the face from the image that it obtained

	pic_img = pic_result[0]['faceId'] # seperates the image from the rest of the date returned by the function 

	for face in os.listdir(directory + "faces"):
		face_name, face_extension = os.path.splitext(face)

		face_url = base_dir + "\\faces\\" + face_name + face_extension # gets the url of the image from the database
		print(face_url)

		face_result = cf.face.detect(face_url) # gets the face from the image that it obtained

		face_img = face_result[0]['faceId'] # seperates the image from the rest of the date returned by the function 

		result, confidence = cf.face.verify(pic_img, face_img)

		if(result):
			print(face_name + " is here")

'''
real_url = 'C:/Users/prana/Documents/ComputerVision/Attendance/images/charles.jpg'

real_result = cf.face.detect(real_url)

real_img = real_result[0]['faceId']

test_url = 'C:/Users/prana/Documents/ComputerVision/Attendance/faces/Charles_Shaffer.jpg'

test_result = cf.face.detect(test_url)

test_img  = test_result[0]['faceId']


r = cf.face.verify(test_img, real_img)

print(r)
'''