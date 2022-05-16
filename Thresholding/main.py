import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread("./../src/gradient.png",0)
_,threshold1 = cv.threshold(img,50,255,cv.THRESH_BINARY)
_,threshold2 = cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
_,threshold3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,threshold4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)

# cv.imshow("Image",img)
# cv.imshow("Thresholded1",threshold1)
# cv.imshow("Thresholded2",threshold2)
# cv.imshow("Thresholded3",threshold3)
# cv.imshow("Thresholded4",threshold4)
titles = ['Original Image','Binary','Binary Inv','Binary Trunc','To Zero']
images = [img,threshold1,threshold2,threshold3,threshold4]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()