import cv2 as cv
import cognitive_face as cf
import os
import matplotlib.pyplot as plt
import urllib
import numpy as np 



key = 'f2e4d43835444a9aad29cbd8a9387c06'

cf.Key.set(key)


real_url = 'C:/Users/prana/Documents/ComputerVision/Create-Face-Data-from-Images-master/faces/0_faces.png'

real_result = cf.face.detect(real_url)

real_img = real_result[0]['faceId']

test_url = 'C:/Users/prana/Documents/ComputerVision/Create-Face-Data-from-Images-master/faces/1_faces2.png'

test_result = cf.face.detect(test_url)

test_img  = test_result[0]['faceId']


r = cf.face.verify(test_img, real_img)

print(r)

