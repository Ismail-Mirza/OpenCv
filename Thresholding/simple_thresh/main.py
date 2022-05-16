import cv2 as cv
import numpy as np
img = cv.imread('../../src/birth.png',0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
# adaptiveThreshold
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Image",img)
# cv.imshow("Thresh",th1)
cv.imshow("Thresh mean c",th2)
cv.imshow("Thresh gaussian c",th3)
cv.waitKey(0)
cv.destroyAllWindows()
