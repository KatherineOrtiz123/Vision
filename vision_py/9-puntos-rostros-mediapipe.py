import cv2
import mediapipe as mp

# Inicializar la clase FaceMesh de MediaPipe
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Inicializar la webcam (puedes cambiar el número según tu configuración)
cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        # Voltear el fotograma horizontalmente para que sea como un espejo
        frame = cv2.flip(frame, 1)

        # Convertir el fotograma a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Realizar la detección de la malla facial
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for landmarks in results.multi_face_landmarks:
                # Dibujar la malla facial
                mp_drawing.draw_landmarks(frame, landmarks)

        cv2.imshow('Face Mesh Detection', frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
