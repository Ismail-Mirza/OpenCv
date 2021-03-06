"""
    Cv Event 

"""
import numpy as np 
import cv2
# show all events
events = [i for i in dir(cv2) if 'EVENT' in i]

# print(events)


def callback_function(event,x,y,flags,params) -> None:
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY= f'{x} ,  {y}'
        
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        cv2.imshow('images',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR= f'{blue},{green},{red}'
        
        cv2.putText(img,strBGR,(x,y),font,1,(255,255,0),2)
        cv2.imshow('images',img)
# def drawCircles(event,x,y,flags,params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),3,(0,0,255),-1)
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img,points[-1],points[-2],(255,0,0),5)
#         cv2.imshow('images',img)
def drawCircles(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('images',img)
def drawColorCircles(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage = np.zeros((512,512,3),np.uint8)
        mycolorImage[:] = [blue,green,red]
        cv2.imshow('color',mycolorImage)
        
# img = cv2.imread('me.jpg')
img = np.zeros((512,512,3))
cv2.imshow('images',img)
# call callback_function
points= []
cv2.setMouseCallback('images',drawColorCircles)
cv2.waitKey(0)
cv2.destroyAllWindows()