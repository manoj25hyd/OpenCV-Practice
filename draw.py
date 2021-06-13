import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0, 255, 0    # RGB
# cv.imshow("Green", blank)

# 2. Draw a Rectangle
#cv.rectangle(blank, (0,0), (250,500), (0,0,255), thickness = 2)
# cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0,0,255), thickness = -1)
# cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 100, (0,0,255), thickness = -1)
#cv.imshow("Circle", blank)

# Draw a Line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness = 2)
# cv.imshow("Line", blank)

# Write text
cv.putText(blank, "Hello,\n Iam Manoj", (222,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=3)
cv.imshow("Text", blank)

cv.waitKey(0)