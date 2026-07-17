import cv2 as cv
import numpy as np

print("OpenCV", cv.__version__)
img = np.zeros((120, 400, 3), dtype=np.uint8)  #creates blank numpy array: 120p tall, 400p wide, 3 channels(BGR). dtype each pixel val is 0-255
cv.putText(img, "OpenCV OK", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)  
#(10,80) is bottom left corner (x,y) of where text starts
#2 is font scaler
#3 is line thickness

cv.imshow("hello", img) #opens window titled "hello" to display image
cv.waitKey(0) #pauses execution until key pressed (0 meaning indefinitely)
#cv.imwrite("Hello.png", img) #would save image as img to current directory