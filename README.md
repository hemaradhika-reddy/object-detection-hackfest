Object Detection Hackfest
Overview
This project is a web application for object detection, developed for the AIWS Hackfest. It uses the YOLOv5 model to detect objects in a static image, displaying results in a user-friendly webpage. The app is built with a Flask backend, Bootstrap frontend, and PyTorch for AI inference, showcasing a full-stack solution with local AI processing. Designed to be scalable to real-time webcam detection, this submission focuses on simplicity and reliability to meet the hackathon's 6-hour timeline.
AI Tools and Libraries

YOLOv5: Pre-trained model for object detection, ensuring accurate and efficient inference.
Flask: Lightweight web framework for serving the application.
PyTorch: Deep learning framework for running YOLOv5.
OpenCV: Image processing for handling input images.
Bootstrap: Frontend framework for responsive and styled UI.

Features

Detects objects in a static image (e.g., "person" with confidence scores) using YOLOv5.
Displays results in a clean, Bootstrap-styled webpage.
Lightweight and local, with no cloud dependencies.
Scalable architecture for potential real-time webcam integration.

Setup Instructions
Follow these steps to run the project locally:

Clone the Repository:
git clone <repo-link>
cd object-detection-hackfest


Create and Activate Virtual Environment:
python3 -m venv venv
source venv/bin/activate


Install Dependencies:
pip install -r requirements.txt
pip install -r yolov5/requirements.txt


For M1/M2 Macs:pip install torch==2.0.1 torchvision==0.15.2 --extra-index-url https://download.pytorch.org/whl/cpu




Download YOLOv5 Model:
wget https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt -O yolov5/yolov5s.pt


Add Test Image:
wget https://ultralytics.com/images/zidane.jpg -O test.jpg


Run the Application:
python3 app.py


Access the App:

Open http://localhost:5000 in a web browser (e.g., Chrome or Firefox).



Expected Output

Terminal (on running app.py):
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)


Webpage (http://localhost:5000):
Object Detection
Detected Objects
person (87.43%)
person (67.54%)


Displays detected objects from test.jpg in a clean, Bootstrap-styled UI.



Demo
[Insert link to demo video here after uploading]

The demo video showcases the webpage output, demonstrating YOLOv5 object detection on a static image.

Repository Structure
object-detection-hackfest/
├── static/
│   ├── styles.css        # Custom CSS for webpage styling
├── templates/
│   ├── index.html        # HTML template for displaying results
├── yolov5/
│   ├── requirements.txt  # YOLOv5 dependencies
├── app.py                # Flask backend with YOLOv5 inference
├── requirements.txt      # Project dependencies
├── test.jpg              # Sample image for detection
├── README.md             # Project documentation
├── .gitignore            # Excludes venv, yolov5s.pt, etc.

Notes

The project uses a static image (test.jpg) for simplicity and reliability, avoiding webcam-related errors.
The .gitignore excludes large files like yolov5s.pt and test.jpg, which are downloaded during setup.
Built in ~6 hours, the app demonstrates a scalable, AI-driven solution with potential for real-time extensions.

