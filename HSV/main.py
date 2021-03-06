import cv2 
import numpy as np



def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Tracking')
# track ber for lower value
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
# upper value 
cv2.createTrackbar("UH","Tracking",0,255,nothing)
cv2.createTrackbar("US","Tracking",0,255,nothing)
cv2.createTrackbar("UV","Tracking",0,255,nothing)



while True:
    # frame = cv2.imread('../src/ball.jpg')
    _,frame = cap.read()
    #convert color to hsv color space
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #threshold color for blue color values
    #define lower range of blue values color
    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")
    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    key = cv2.waitKey(1)
    
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()