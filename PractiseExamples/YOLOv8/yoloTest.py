from ultralytics import YOLO

model = YOLO("yolov8n.pt")   #nano model, auto downloads 
results = model("path/to/image.jpg", show=True, save=True)