import cv2
import numpy as np
# img 1
img1 = np.zeros((339,500,3),np.uint8)
cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)

img2 = cv2.imread("../src/image_1.jpg")
img1 = cv2.resize(img1,(600,300))
img2 = cv2.resize(img2,(600,300))
# bitAnd = cv2.bitwise_and(img2,img1)
# bitAnd = cv2.bitwise_or(img2,img1)
# bitAnd = cv2.bitwise_xor(img2,img1)
bitNot = cv2.bitwise_not(img1)
cv2.imshow("image2",img2)
cv2.imshow("image1",img1)
cv2.imshow("bitand",bitNot)
cv2.waitKey(0)
cv2.destroyAllWindows()