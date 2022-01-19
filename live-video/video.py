    """
     Add Date Time to Live Video
    
    """

import cv2
import datetime
cap = cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1000)
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text= f'Width: {cap.get(3)} Height:{cap.get(4)}'
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame,date,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()