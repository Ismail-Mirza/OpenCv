import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("./../src/messi.jpg",-1)

cv.imshow("Image",img)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
# hide x and coordinates of matplotlib axis 
plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()