import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:

    # Leer frame
    ret, frame = cap.read()

    # Detectar cara
    results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Obtener coordenadas de ojos
    l_eye_x = 0
    l_eye_y = 0
    r_eye_x = 0
    r_eye_y = 0

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]

        # Ojo izquierdo
        l_eye = face.landmark[33]
        l_eye_x = int(l_eye.x * frame.shape[1])
        l_eye_y = int(l_eye.y * frame.shape[0])

        # Ojo derecho
        r_eye = face.landmark[263]
        r_eye_x = int(r_eye.x * frame.shape[1])
        r_eye_y = int(r_eye.y * frame.shape[0])

    # Dibujar círculos
    cv2.circle(frame, (l_eye_x, l_eye_y), 20, (0, 255, 255), 5)
    cv2.circle(frame, (r_eye_x, r_eye_y), 20, (0, 0, 255), 5)

    cv2.imshow('MediaPipe FaceMesh', frame)

    if cv2.waitKey(1) == 13:  # cierra la ventana con enter
        break

cap.release()
cv2.destroyAllWindows()
