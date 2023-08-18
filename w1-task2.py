import cv2 as cv

capture = cv.VideoCapture("gandalfLaugh.mp4")

while True:
    
    retval, frame = capture.read()

    if not retval:
        break

    cv.imshow("Display name", frame)

    if cv.waitKey(17) == ord(' '): # close if spacebar is pressed
        break

capture.release()
cv.destroyAllWindows()