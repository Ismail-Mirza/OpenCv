import cv2
import numpy as np
import math
import time
def fx(x):
    return abs((100-x**2)**0.5)
def fx2(x):
    return x**2
w =  1000
h =  1000
image = np.zeros((w,h,3),np.uint8)
heart_w = 100
heart_h = 100
first_x = 0
last_x = 0
first_y = 0
last_y = 0
x_cor = np.linspace(-2,2,1000)
while True:
    key = cv2.waitKey(0) & 0xFF
    
    for i in x_cor:
        
        y1 =math.floor(fx(i))
        x1 =math.floor(abs(i)*100)
        y2 =math.floor(fx(i+1))
        x2 = math.floor(abs(i+1)*100)
        print(x1,y1)
        image = cv2.line(image,(x1,y1),(x2,y2),(0,0,255),5)
    
    # last_x = x2
    # last_y = math.floor(fx(x_cor[0])*heart_h)
    # first_x = math.floor(abs(x_cor[0])*heart_w)+heart_w
    # for i in range(len(x_cor)-2):
    #     y1 =200- math.floor(fx( i)*heart_h)
    #     x1 = math.floor(abs( i)*heart_w)+last_x
    #     y2 =200- math.floor(fx(x_cor[i+1])*heart_h)
    #     x2 = math.floor(abs(x_cor[i+1])*heart_w)+last_x
    #     image = cv2.line(image,(x1,y1),(x2,y2),(0,0,255),5)
    # for i in range(len(x_cor)-2):
    #     y1 = last_y+math.floor(fx2( i)*heart_h)
    #     x1 = math.floor(abs( i)*heart_w)+first_x
    #     y2 = last_y+math.floor(fx2(x_cor[i+1])*heart_h)
    #     x2 = math.floor(abs(x_cor[i+1])*heart_w)+first_x
    #     image = cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
        
    if key == 27:
        break 
    cv2.imshow("image", image)
cv2.destroyAllWindows()