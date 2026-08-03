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

        hsv_unnorm = np.array([200, 100, 93])
        hsv_norm = (hsv_unnorm[0]/360 * 179), (hsv_unnorm[1]/100 * 255), (hsv_unnorm[2]/100 * 255)

        dark_col = hsv_norm - np.array((10, 99, 80))
        bright_col = hsv_norm + np.array((10, 99, 80))

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

    if not contours:
        return
    
    largest = max(contours, key=cv.contourArea)
    if cv.contourArea(largest) > 500:
        cv.drawContours(res, [largest], -1, (0,255,0), 3)

    #Rotating bounding box
    rect = cv.minAreaRect(largest)
    #find min area rectangle that encloses all points in the contour
    #returns (centre coords, (width,height), angle of rotation)

    box = cv.boxPoints(rect) #returns four corners of the rectangle
    box = np.int32(box) #coords must be integers to draw onto an image
    cv.putText(res, "Bounding box", (int(rect[0][0]), int(rect[0][1])), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2, cv.LINE_AA)
    cv.drawContours(res, [box], 0, (0,0,255), 2)

CaptureVideo()