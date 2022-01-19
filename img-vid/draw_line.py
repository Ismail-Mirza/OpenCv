import cv2 as cv
import numpy as np
# create black image with zeros 
# zeros([img_width, img_height,3],datatype)
# img = np.zeros([512,512,3],np.uint8)
img = cv.imread("image/me.jpg",1)
#draw line in img
# line(img_to_draw,start_cor,end_cor,rgb_color,thickness)
# img = cv.line(img,(0,0),(255,255),(255,0,0),5)
# img = cv.arrowedLine(img,(0,0),(255,255),(255,0,0),5)
img= cv.rectangle(img,(0,0),(255,255),(255,74,70),5)
# circle(img,center_cor,radius,color,thickness)
#write text in the Image
font=cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img,"OpenCv",(10,500),font,4,(0,255,255),10,cv.LINE_AA)
cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()