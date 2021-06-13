# Import cv2
import cv2 as cv

# Read Image
# img = cv.imread("C:\\Users\\B.Manoj Kumar\\Downloads\\cat.jpg")

# cv.imshow("Cat", img)

# cv.waitKey(0)

# Read Videos
capture = cv.VideoCapture("C:\\Users\\B.Manoj Kumar\\Downloads\\video.mp4")

while True:
    isTrue, frame = capture.read()

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows() 