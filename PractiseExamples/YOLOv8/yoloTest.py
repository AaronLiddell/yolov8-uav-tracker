from ultralytics import YOLO
import cv2 as cv
import numpy as np


model = YOLO("PractiseExamples/YOLOv8/yolov8n.pt")   #nano model, auto downloads 
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

        results = model(frame, save=False)
        boxes = results[0].boxes

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0]) #gives top left and bottom right corners of bounding boxes and turns from tensor to integer
            conf = float(box.conf[0]) #pulls confidence score of a box. converts to float
            cls = int(box.cls[0]) #pulls out class number and converts to interger
            label = model.names[cls] #gets the label from the class number

            vertRectangle(frame,x1,y1,x2,y2)

            cv.putText(frame, f"{label} {conf:.2f}", (x1,y1), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        cv.imshow("frame", frame)

        if cv.waitKey(1) == ord("q"): #waits for q pressed to end 
            break

    cap.release()
    cv.destroyAllWindows()

def vertRectangle(frame,x1,y1,x2,y2):
    cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
    

CaptureVideo()