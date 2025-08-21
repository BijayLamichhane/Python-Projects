import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import time

# --- Helper to open first working camera ---
def open_camera(max_index=3, retries=5, delay=2):
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ Camera found at index {i}")
            return cap
        cap.release()
    print("❌ No working camera found")
    return None

cap = open_camera()
if cap is None:
    exit()

# --- Load known faces ---
your_image = face_recognition.load_image_file("faces/1.jpg")
encoding = face_recognition.face_encodings(your_image)[0]

known_face_encodings = [encoding]
known_face_names = ["your_name"]
students = known_face_names.copy()

# --- Prepare CSV ---
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])  # header

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("⚠️ Failed to grab frame. Retrying...")
        time.sleep(0.5)
        continue

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            current_time = datetime.now().strftime("%H:%M:%S")
            if name in students:
                lnwriter.writerow([name, current_time])
                students.remove(name)
                print(f"✅ Marked attendance: {name} at {current_time}")

            # Add the text if the person is present
            if name in known_face_names:
              font = cv2.FONT_HERSHEY_SIMPLEX
              bottomLeftCornerOfText = (10, 100)
              fontScale = 1.5
              fontColor = (255, 0, 0)
              thickness = 3
              lineType = 2
              cv2.putText (frame, name + "Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

              if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
f.close()
cv2.destroyAllWindows()
