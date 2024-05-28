import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 1)
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, frame)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()