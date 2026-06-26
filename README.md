# Driver Drowsiness Detection System

A **real-time Driver Drowsiness Detection System** developed using **Python, OpenCV, and MediaPipe**. The system continuously monitors the driver's face through a webcam and detects signs of fatigue by analyzing **eye closure** and **yawning**. Based on the driver's fatigue level, it provides **real-time voice alerts**, displays the driver's status, and stores all detection events in a CSV log file.

---

# Motivation

Driver fatigue is one of the major causes of road accidents worldwide. Long driving hours often reduce a driver's alertness, increasing the risk of collisions. The objective of this project is to build an intelligent computer vision system that can monitor the driver's facial features in real time, detect drowsiness at an early stage, and alert the driver before a dangerous situation occurs.

---

# Built With

* **Python** – Core programming language.
* **OpenCV** – Real-time image processing and face/eye detection.
* **MediaPipe Face Mesh** – Facial landmark detection for yawning detection.
* **Haar Cascade Classifiers** – Face and eye detection.
* **CSV Module** – Stores driver activity logs.
* **PowerShell Speech Synthesizer** – Generates voice alerts.
* **Datetime Module** – Records timestamps for every event.

---

# Getting Started

These instructions will help you run the project on your local machine.

## Prerequisites

* Python 3.10 or later
* Webcam
* Visual Studio Code or any Python IDE

---

# Installation

Clone the repository.

```bash
git clone https://github.com/your-username/Driver-Drowsiness-Detection-System.git
```

Move into the project folder.

```bash
cd Driver-Drowsiness-Detection-System
```

Install the required libraries.

```bash
pip install opencv-python mediapipe
```

---

# Running the Application

Run the Python file.

```bash
python driver_drowsiness.py
```

The webcam will open and begin monitoring the driver's face.

Press **ESC** to close the application.

---

# Algorithm

1. Capture live video frames using the webcam.
2. Detect the driver's face using OpenCV Haar Cascade.
3. Detect the driver's eyes using the Eye Cascade classifier.
4. Count consecutive frames where eyes remain closed.
5. Detect yawning using MediaPipe Face Mesh by measuring the distance between the upper and lower lips.
6. Calculate the fatigue score based on:

   * Eye closure duration
   * Number of yawns detected
7. Classify the driver's condition into:

   * Normal
   * Drowsy
   * Critical
8. Generate voice alerts whenever the driver becomes drowsy or critically drowsy.
9. Store every detection event in a CSV file with timestamp, driver state, fatigue score, and yawning status.
10. Continue monitoring until the user presses the ESC key.

---

# Features

* Real-time face detection
* Eye detection
* Yawning detection
* Fatigue score calculation
* Voice alert system
* Driver status monitoring
* CSV logging
* Live webcam interface
* Easy to use
* Lightweight and fast

---

# Driver Status Levels

| Fatigue Score | Status      |
| ------------- | ----------- |
| Less than 15  | 🟢 Normal   |
| 15 - 29       | 🟡 Drowsy   |
| 30 and Above  | 🔴 Critical |

---

# Output

The application displays:

* Driver Status
* Fatigue Score
* Yawning Detection
* Number of Faces Detected
* Number of Eyes Detected
* Closed Eye Frames
* Voice Alerts

The system also creates a CSV log file containing:

* Time
* Driver Status
* Fatigue Score
* Yawning Detection

---

# Testing and Results

The system was tested under different real-world conditions.

## Test Case 1: Normal Lighting

**Result:** Face and eyes were detected successfully, and fatigue monitoring worked accurately.

(Add Screenshot Here)

---

## Test Case 2: Driver Yawning

**Result:** The system successfully detected yawning using MediaPipe Face Mesh and increased the fatigue score.

(Add Screenshot Here)

---

## Test Case 3: Driver Closing Eyes

**Result:** Continuous eye closure increased the fatigue score, and the system generated a voice warning.

(Add Screenshot Here)

---

## Test Case 4: Drowsy Driver

**Result:** When the fatigue score crossed the threshold, the system changed the driver's status from **Normal** to **Drowsy** and produced an alert.

(Add Screenshot Here)

---

## Test Case 5: Critical Driver State

**Result:** When the fatigue score exceeded the critical threshold, the system displayed **Critical** status and generated a stronger voice alert recommending the driver take a break.

(Add Screenshot Here)

---

## Test Case 6: CSV Log Generation

**Result:** Every detection event was successfully stored in a CSV file with timestamp, driver status, fatigue score, and yawning information.

(Add Screenshot Here)

---

# Project Structure

```
Driver-Drowsiness-Detection-System/

│── driver_drowsiness.py
│── driver_drowsiness_log.csv
│── README.md
```

---

# Future Scope

* Mobile application support
* GPS-based emergency alerts
* SMS notifications to emergency contacts
* Deep Learning based eye aspect ratio (EAR) detection
* Night vision camera support
* Cloud dashboard for fatigue monitoring
* Driver identity recognition using Face Recognition

---

# References

1. OpenCV Documentation

https://docs.opencv.org/

2. MediaPipe Face Mesh

https://developers.google.com/mediapipe

3. Python Documentation

https://docs.python.org/3/

---

# Author

**Sanjana Palle**

**B.Tech - Infomation Technology**

**Skills:** Python | Computer Vision | OpenCV | MediaPipe | Machine Learning

**GitHub:** https://github.com/your-sanjana

**LinkedIn:** https://linkedin.com/in/sanjana
