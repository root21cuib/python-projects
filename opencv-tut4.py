import numpy as np
import cv2

#cap = cv2.VideoCapture(0)

img = cv2.imread('/home/chris/Documents/python-projects/cipherpic1.png', 1)
#cv2.imshow('frame', img)

cv2.line(img,(0,0), (511,511), (255,0,0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()