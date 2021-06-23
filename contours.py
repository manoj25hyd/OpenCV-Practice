import cv2 as cv

img = cv.imread("C:\\Users\\B.Manoj Kumar\\Downloads\\jon.jpg")
#cv.imshow("Jon Snow", img)

# Scaling
def rescale(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

new_img = rescale(frame = img, scale = 0.5)
cv.imshow("Scaled Image", new_img)

gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

canny = cv.Canny(new_img, 125, 175)
cv.imshow("Canny", canny)

cv.waitKey(0)