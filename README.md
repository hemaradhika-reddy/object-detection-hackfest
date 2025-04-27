
## Overview
This project is a web application for object detection, developed for the **AIWS Hackfest**. It uses the **YOLOv5** model to detect objects in a static image, displaying results in a user-friendly webpage.  

The app is built with a **Flask** backend, **Bootstrap** frontend, and **PyTorch** for AI inference, showcasing a full-stack solution with local AI processing.  

Designed to be scalable to real-time webcam detection, this submission focuses on simplicity and reliability to meet the hackathon's 6-hour timeline.

## AI Tools and Libraries
- **YOLOv5**: Pre-trained model for object detection, ensuring accurate and efficient inference.
- **Flask**: Lightweight web framework for serving the application.
- **PyTorch**: Deep learning framework for running YOLOv5.
- **OpenCV**: Image processing for handling input images.
- **Bootstrap**: Frontend framework for responsive and styled UI.

## Features
- Detects objects in a static image (e.g., "person" with confidence scores) using YOLOv5.
- Displays results in a clean, Bootstrap-styled webpage.
- Lightweight and local, with no cloud dependencies.
- Scalable architecture for potential real-time webcam integration.
