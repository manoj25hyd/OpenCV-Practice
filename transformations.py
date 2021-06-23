import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\\B.Manoj Kumar\\Downloads\\jon.jpg")
# blank = np.zeros((200, 500, 3), dtype = 'uint8')  # (Height, Width, Number of channels)
#cv.imshow("Jon Snow", img)

# Rescaling
def rescaleframe(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

new_img = rescaleframe(frame = img, scale = 0.5)

cv.imshow("Jon Snow", new_img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])  

    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up

translated = translate(img = new_img, x = 40, y = 50)
translated_negative = translate(new_img, x = -30, y = -50)

# cv.imshow("Translated Image", translated)

# Rotation
def rotate(img, angle, rotation_point = None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated = rotate(img = new_img, angle = 23) # Negative sign for clock-wise

cv.imshow("Rotated Image", rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# Flipping
# flipcode = 0 --> Flip Vertically
# flipcode = 1 --> Flip Horizontally
# flipcode = -1 --> Flip both Horizontally and Vertically
flip = cv.flip(new_img, flipCode = 1)
cv.imshow("Flip", flip)

# Cropping
cropped = new_img[200 : 400, 300 : 400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)