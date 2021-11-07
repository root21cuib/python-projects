#import numpy as np
#import sys
#import numpy as np

'''cap = cv2.VideoCapture("virus.mp4")
cv2.namedWindow('Frame',cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:
       break
cap.release()
cv2.destroyAllWindows()
'''


#-1, cv2.IMREAD_COLOR : loads a color image. Any transparancy of image is ignored
#0,  cv2.IMREAD_GRAYSCALE : loads image in grayscale mode
#1,  cv2.IMREAD_UNCHANGED : loads imagr as such including alpha channel
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)


import cv2
img = cv2.imread('/home/chris/Documents/python-projects/cipherpic1.png', 1)
print(type(img))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_img.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
