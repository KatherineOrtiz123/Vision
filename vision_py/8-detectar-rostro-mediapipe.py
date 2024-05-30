import cv2
import mediapipe as mp

# Inicializar la clase de detección de rostros de MediaPipe
mp_face_detection = mp.solutions.face_detection

# Inicializar la webcam (puedes cambiar el número según tu configuración)
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        # Voltear el fotograma horizontalmente para que sea como un espejo
        frame = cv2.flip(frame, 1)

        # Convertir el fotograma a RGB para MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Realizar la detección de rostros
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
