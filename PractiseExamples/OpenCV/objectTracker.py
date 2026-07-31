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

        hsv_unnorm = np.array([200, 11, 78])
        hsv_norm = (hsv_unnorm[0]/360 * 179), (hsv_unnorm[1]/100 * 255), (hsv_unnorm[2]/100 * 255)

        dark_col = hsv_norm - np.array((10, 100, 100))
        bright_col = hsv_norm + np.array((10, 100, 100))

        mask = cv.inRange(hsv, dark_col, bright_col)
        mask = erodeNoise(mask) #shrinks small patches of white noise

        res = cv.bitwise_and(frame, frame, mask = mask)
        
        contouring(mask, res)



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

def contouring(mask, res):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    largest = max(contours, key=cv.contourArea)
    if cv.contourArea(largest) > 500:
        cv.drawContours(res, [largest], -1, (0,255,0), 3)


CaptureVideo()