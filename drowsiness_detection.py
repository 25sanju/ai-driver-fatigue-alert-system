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
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
)

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)
cap = cv2.VideoCapture(0)
# ---------------- VARIABLES ----------------
fatigue_score = 0
eye_closed_frames = 0
state = "NORMAL"
yawn_detected = False

# ---------------- CSV LOG ----------------
log_file = open("driver_drowsiness_log.csv", "w", newline="")
writer = csv.writer(log_file)
writer.writerow(["Time", "State", "Fatigue Score", "Yawning"])

print("🚗 Driver Drowsiness System Started")

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ---------------- FACE DETECTION ----------------
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes_detected = 0

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        eyes_detected = len(eyes)

    # ---------------- FACE MESH (YAWN DETECTION) ----------------
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    yawn_detected = False

    if results.multi_face_landmarks:
        for lm in results.multi_face_landmarks:
            upper_lip = lm.landmark[13]
            lower_lip = lm.landmark[14]

            mouth_gap = abs(upper_lip.y - lower_lip.y)

            if mouth_gap > 0.06:
                yawn_detected = True

    # ---------------- FATIGUE LOGIC (FIXED) ----------------
    if len(faces) > 0:

        if eyes_detected == 0:
            eye_closed_frames += 1
        else:
            eye_closed_frames = 0
            fatigue_score = max(0, fatigue_score - 1)

        if eye_closed_frames > 15:
            fatigue_score += 2

    else:
        eye_closed_frames = 0

    if yawn_detected:
        fatigue_score += 1
        cv2.putText(frame, "YAWNING DETECTED", (30, 250),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # ---------------- STATE MACHINE ----------------
    if fatigue_score < 15:
        new_state = "NORMAL"
        color = (0, 255, 0)

    elif fatigue_score < 30:
        new_state = "DROWSY"
        color = (0, 255, 255)

    else:
        new_state = "CRITICAL"
        color = (0, 0, 255)

    # ---------------- VOICE ALERT ----------------
    if new_state != state:
        state = new_state

        if state == "DROWSY":
            speak("You are feeling drowsy. Please stay alert.")

        elif state == "CRITICAL":
            speak("Warning. You are critically drowsy. Please take a break.")

    # ---------------- LOGGING ----------------
    writer.writerow([datetime.now(), state, fatigue_score, yawn_detected])

    # ---------------- UI ----------------
    cv2.putText(frame, f"STATUS: {state}", (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.putText(frame, f"FATIGUE SCORE: {fatigue_score}", (30, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.putText(frame, f"YAWN: {yawn_detected}", (30, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 255), 2)

    cv2.putText(frame, f"Faces: {len(faces)}", (30, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"Eyes: {eyes_detected}", (30, 240),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, f"Closed Frames: {eye_closed_frames}", (30, 280),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, "Press ESC to Exit", (30, 320),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    cv2.imshow("Driver Drowsiness Detection System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
log_file.close()
