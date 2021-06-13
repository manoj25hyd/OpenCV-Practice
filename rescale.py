# Import Library
import cv2 as cv

# Read Image
# img = cv.imread("C:\\Users\\B.Manoj Kumar\\Downloads\\cat.jpg")

# # Display image
# cv.imshow("Cat", img)

# # Define a function to rescale a image
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # For Live Video
    capture.set(3, width)
    capture.set(4, height)    

# # Take resized image in a variable
# img2 = rescaleFrame(frame = img, scale = 0.5)

# # Display Scaled image
# cv.imshow("Cat_Small", img2)

# cv.waitKey(0)

# Read Video
capture = cv.VideoCapture(0)
# changeRes(45,56)

while True:
    isTrue, frame = capture.read()

    rescaled_frame =  rescaleFrame(frame = frame, scale = 0.2)

    cv.imshow("Scaled_Video", rescaled_frame)
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break


capture.release()

cv.destroyAllWindows()