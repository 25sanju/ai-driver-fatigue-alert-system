import cv2
import time
import os
import csv
from datetime import datetime
import mediapipe as mp

# ---------------- VOICE FUNCTION ----------------
def speak(text):
    os.system(
        'PowerShell -Command "Add-Type –AssemblyName System.Speech;'
        '$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;'
        f'$speak.Speak(\'{text}\');"'
    )

# ---------------- SETUP ----------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

# ---------------- VARIABLES ----------------
fatigue_score = 0
eye_closed_time = 0
state = "NORMAL"

# ---------------- LOG FILE ----------------
log_file = open("driver_drowsiness_log.csv", "w", newline="")
writer = csv.writer(log_file)
writer.writerow(["Time", "State", "Fatigue Score"])

print("🚗 Driver Drowsiness System Started")

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ---------------- FACE + EYES ----------------
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes_detected = 0

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        eyes_detected = len(eyes)

    # ---------------- FATIGUE LOGIC ----------------
    if eyes_detected == 0:
        eye_closed_time += 1
        fatigue_score += 1
    else:
        eye_closed_time = 0
        fatigue_score = max(0, fatigue_score - 1)

    # ---------------- STATE ----------------
    if fatigue_score < 10:
        new_state = "NORMAL"
        color = (0, 255, 0)

    elif fatigue_score < 20:
        new_state = "DROWSY"
        color = (0, 255, 255)

    else:
        new_state = "CRITICAL"
        color = (0, 0, 255)

    # ---------------- VOICE ALERT ----------------
    if new_state != state:
        if new_state == "DROWSY":
            speak("You are feeling drowsy. Please stay alert.")
        elif new_state == "CRITICAL":
            speak("Warning. You are critically drowsy. Please take a break.")
        state = new_state

    # ---------------- LOGGING ----------------
    writer.writerow([datetime.now(), state, fatigue_score])

    # ---------------- UI ----------------
    cv2.putText(frame, f"STATUS: {state}", (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.putText(frame, f"FATIGUE SCORE: {fatigue_score}", (30, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.putText(frame, "Press ESC to Exit", (30, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    cv2.imshow("Driver Drowsiness Detection System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
log_file.close()