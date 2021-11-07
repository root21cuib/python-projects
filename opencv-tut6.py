import numpy as np
import cv2

1
img = cv2.imread('/home/chris/Documents/python-projects/cipherpic1.png', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.2, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (250, 0, 0), -1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()