import cv2 as cv

#read image by imread(filename,flug) # FLUG CANBE 1 read image in color mood // 0 read image in grayscale // -1 read image as its in alpha channel 
# if specified image is not available than imread return none
#otherwise it returns an np matrix
img=cv.imread("image/me.jpg",-1)
# print(img)
#show image using imshow(window_name,img_pointer)
cv.imshow("image",img)
# image disappear open and disappear
#to show the image for specified sec use waitKey method
k=cv.waitKey(0)
# in 64bit machine we should use like
#  waitKey(0) & 0xFF
if k==27:
#destroy all window that were created
    cv.destroyAllWindows()
elif k  == ord('s'):
    cv.imwrite("image/copy_me.png",img)
    cv.destroyAllWindows()
