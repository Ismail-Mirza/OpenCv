import numpy as np
import cv2
img = cv2.imread('../src/messi.jpg')
img2 = cv2.imread('../src/building.jpg')
# print img.shape get the shape of the image

print(img.shape)
# print size of image
print(img.size)
# image datatype
print(img.dtype)
# split image into into bgr format
b,g,r = cv2.split(img)
# merge b,g,r into image by merge method

new_img = cv2.merge([b,g,r])
new_img = cv2.resize(new_img,(600,300))
new_img2 = cv2.resize(img2,(600,300))
ball = new_img[280:340,330:390]
new_img[50:70,100:160] = ball
# add two image 
dst = cv2.add(new_img,new_img2)
#add two image by saturation 
dst2 = cv2.addWeighted(new_img,.9,new_img2,.1,10)
cv2.imshow("image",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
