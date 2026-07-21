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
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        dark_col = np.array([83, 50, 50])
        bright_col = np.array([103, 255, 255])

        mask = cv.inRange(hsv, dark_col, bright_col)
        mask = erodeNoise(mask) #shrinks small patches of white noise

        res = cv.bitwise_and(frame, frame, mask = mask)


        #display resulting frame
        cv.imshow("frame", frame)
        cv.imshow("mask", mask)
        cv.imshow("res", res)
        if cv.waitKey(1) == ord("q"): #waits for q pressed to end 
            break

    cap.release()

def erodeNoise(mask):
    kernel = np.ones((5,5), np.uint8)
    erosion = cv.erode(mask, kernel, iterations=1)

    return erosion

CaptureVideo()