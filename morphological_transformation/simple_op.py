import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("./../src/ball.jpg",cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# to remove the black mark in mask image shape
kernel = np.ones((5,2),np.uint8)
dilation  = cv2.dilate(mask,kernel,iterations=4)
erosion = cv2.erode(mask,kernel,iterations=5)
# opening erosion than dilation
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
#closing dilation than erosion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
titles = ['images',"mask",'dilation','erosion','opening','closing']
images=[img,mask,dilation,erosion,opening,closing]


for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()