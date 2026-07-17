import cv2 as cv
import numpy as np

def CaptureVideo():
    cap = cv.VideoCapture(0) #0 specifies which camera
    if not cap.isOpened():
        print("Camera could not be opened")
        exit()
    while True:
        #capture frame by frame
        ret, frame = cap.read()  
        #ret (bool) if frame was successfully grabbed. If false, could be end of vid.
        #frame is array of values in BGR form to create image of that frame

        #correctly read frame means ret is true
        if not ret:
            print("Cant recieve frame (stream end?). Exiting....")
            break

        #operations on frame come below
        gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        #display resulting frame
        cv.imshow("frame", gray)
        if cv.waitKey(1) == ord("q"): #waits for q pressed to end 
            break

    cap.release()

CaptureVideo()