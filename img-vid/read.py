import cv2 as cv
#accept filename or webcam index as argument
cap = cv.VideoCapture(0)
# output video 
fourcc = cv.VideoWriter_fourcc(*'XVID')
# cv.VideoWritter(output_filename,fourcc_code,captured_per_sec,output_video_size:tuple)
out = cv.VideoWriter("output.avi",fourcc,20.0,(640,480))
while(cap.isOpened()):
    #read method return true if frame is available
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
        # convert grey image 
        # cvtColor(source,convertion_type)
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("frame",gray)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# release cap variable
cap.release()
out.release()
cv.destroyAllWindows()