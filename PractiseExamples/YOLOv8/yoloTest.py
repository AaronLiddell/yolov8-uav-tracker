from ultralytics import YOLO
import cv2 as cv
import numpy as np


model = YOLO("yolov8n.pt")   #nano model, auto downloads 
#results = model("images/yoloTest.jpg", show=True, save=True)
#print(results[0].boxes)

def CaptureVideo():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Camera could not be opened")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Cant recieve frame (stream end?). Exiting....")
            break

        result = model(frame, save=False)
        annotated = result[0].plot()
        cv.imshow("frame", annotated)

        if cv.waitKey(1) == ord("q"): #waits for q pressed to end 
            break

    cap.release()
    cv.destroyAllWindows()

CaptureVideo()