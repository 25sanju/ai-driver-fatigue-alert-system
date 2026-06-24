# AI Driver Drowsiness Detection System

## Overview
Drowsiness detection is a safety system designed to prevent road accidents caused by driver fatigue. This project uses computer vision to detect drowsiness in real time from a webcam feed and provides alerts using voice and visual warnings.

## Motivation
Driver fatigue is one of the major causes of road accidents worldwide. This system helps in detecting early signs of drowsiness and improving road safety using AI-based monitoring.

## Built With
• Python  
• OpenCV (Computer Vision)  
• MediaPipe Face Mesh  
• NumPy  
• CSV Module  
• PowerShell Speech Engine  

## Features
• Real-time face detection  
• Eye closure detection using Haar cascade  
• Yawning detection using MediaPipe  
• Fatigue scoring system  
• State classification (NORMAL / DROWSY / CRITICAL)  
• Voice alert system  
• Live webcam processing  
• CSV logging  

## Working Principle
1. Capture webcam video  
2. Detect face using OpenCV  
3. Detect eyes using Haar cascade  
4. Detect mouth movement using MediaPipe  
5. Calculate fatigue score  
6. Trigger alerts based on thresholds  

## System States
| State | Description | Action |
|------|------------|--------|
| NORMAL | Driver is alert | No alert |
| DROWSY | Early fatigue detected | Voice warning |
| CRITICAL | High fatigue risk | Strong alert |

## Testing Scenarios
• Normal lighting conditions → stable detection  
• Different face positions → works correctly  
• Wearing glasses → eye detection works  
• Yawning → detected using landmarks  
• Limitation → low light reduces accuracy  

## Future Improvements
• Deep learning-based detection  
• Mobile application integration  
• Night vision support  
• Vehicle safety automation system  

## How to Run
```bash
pip install -r requirements.txt
python drowsiness.py

## Author
Sanjana
AI Driver Drowsiness Detection System
Domain: Computer Vision and Artificial Intelligence



