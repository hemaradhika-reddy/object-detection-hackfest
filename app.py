from flask import Flask, render_template
import torch
import cv2

app = Flask(__name__)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/yolov5s.pt')

@app.route('/')
def index():
    img = cv2.imread('test.jpg')
    results = model(img)
    detections = results.pandas().xyxy[0]
    objects = detections[['name', 'confidence']].to_dict('records')
    objects = [{'Name': obj['name'], 'Confidence': obj['confidence'] * 100} for obj in objects]
    return render_template('index.html', objects=objects)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

