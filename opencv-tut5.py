import cv2
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([80, 50, 50])
    upper_blue = np.array([130, 200, 200])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)


    '''BGR_color = np.array([[[255, 0, 0]]])
    x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
    x[0][0]  to display just one pixel'''


    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
