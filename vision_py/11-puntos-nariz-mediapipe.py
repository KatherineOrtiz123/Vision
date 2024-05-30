import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    # Leer frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Detectar cara
    results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]

        # Punta de nariz
        nose_point = face.landmark[4]
        nose_x = int(nose_point.x * frame.shape[1])
        nose_y = int(nose_point.y * frame.shape[0])

        # Círculo en nariz
        cv2.circle(frame, (nose_x, nose_y), 20, (0, 255, 0), -1)

    cv2.imshow('MediaPipe FaceMesh', frame)

    if cv2.waitKey(1) == 13:  # cierra la ventana con enter
        break

cap.release()
cv2.destroyAllWindows()
