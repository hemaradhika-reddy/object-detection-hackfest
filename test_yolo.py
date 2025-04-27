import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/yolov5s.pt')
img = cv2.imread('test.jpg')
results = model(img)
print(results.pandas().xyxy[0])
