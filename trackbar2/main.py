import numpy as np
import cv2 as cv


def nothing(x):
    print(x)



cv.namedWindow('image')
cv.createTrackbar('CP', 'image', 0,400, nothing)
# use switch using trackbar
button = 'color/gray'
cv.createTrackbar(button, 'image', 0, 1, nothing)



# b,g,r = cv.split(img)
# img = cv.merge([0.299*r,0.587*g,0.114*b])


while True:
    img = cv.imread('../src/messi.jpg')
    img = cv.resize(img,(500,500))
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,4,(0,0,255))
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    s = cv.getTrackbarPos(button, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img=cv.imshow('image', img)
cv.destroyAllWindows()
