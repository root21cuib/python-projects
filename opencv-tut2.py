import cv2
import random
cap = cv2.imread('/home/chris/Documents/python-projects/cipherpic1.png', 1)
#standard is RGB but opencv uses BGR

'''for i  in range(100):
    for j in range(cap.shape[1]):
        cap[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
'''

#copy part of the image and paste it  to another part
tag = cap[500:700, 600:900]
cap[100:300, 650:950] = tag


cv2.imshow('image', cap)
cv2.waitKey(0)
cv2.destroyAllWindows()