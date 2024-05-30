import pygame
import cv2
import numpy as np
import mediapipe as mp

# Definir el color del círculo (en formato RGB)
circle_color = (255, 0, 0)  # Rojo

# Librerías de dibujado y detección de MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Parámetros del círculo a dibujar
circle_radius = 5
circle_color = (0, 255, 0)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla de Pygame
screen_width, screen_height = 800, 600
camera_width, camera_height = 250, 150

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Cámara en Pygame")

# Inicializar la cámara de OpenCV
cap = cv2.VideoCapture(0)

font = pygame.font.Font(None, 36)  # Ajustar el tamaño de la fuente para el mensaje

# Lista para almacenar las posiciones de la nariz en la ventana principal
nose_positions = []

# Almacenar la última posición válida de la nariz
last_nose_x, last_nose_y = None, None

with mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()  # Liberar la cámara
                cv2.destroyAllWindows()  # Cerrar las ventanas de OpenCV
                exit()
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

        # Capturar un frame de la cámara
        success, frame = cap.read()

        # Verificar que haya frame disponible
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Invertir horizontalmente el frame para que la imagen no esté espejada
        frame = cv2.flip(frame, 1)

        # Escalar el frame a las dimensiones deseadas (250x150)
        frame = cv2.resize(frame, (camera_width, camera_height))

        # Convertir el frame de OpenCV a un formato adecuado para Pygame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detectar cara
        results = face_mesh.process(frame)

        # Obtener coordenadas de punto de referencia
        x, y = None, None

        # Verificar que se haya detectado una cara
        if results.multi_face_landmarks:
            # Tomar el primer rostro
            face_landmarks = results.multi_face_landmarks[0]

            # Obtener punto de referencia deseado
            # Ej: Punta de nariz
            x = int(face_landmarks.landmark[4].x * frame.shape[1])
            y = int(face_landmarks.landmark[4].y * frame.shape[0])

            # Actualizar la última posición válida de la nariz
            last_nose_x, last_nose_y = x, y
        else:
            # Si no se detecta la nariz, usar la última posición válida
            x, y = last_nose_x, last_nose_y

        # Verificar si hay una posición válida para dibujar el círculo
        if x is not None and y is not None:
            # Dibujar círculo en coordenadas deseadas
            frame = cv2.circle(frame, (x, y), circle_radius, circle_color, -1)
            nose_detected = True
        else:
            nose_detected = False

        # Voltear horizontalmente para sincronizar
        frame = cv2.flip(frame, 1)

        pygame_frame = pygame.surfarray.make_surface(np.rot90(frame))

        # Rellenar la pantalla con un color pastel morado
        screen.fill((230, 230, 250))  # Pastel morado

        # Dibujar el frame escalado en la esquina superior izquierda
        screen.blit(pygame_frame, (0, 0))

        # Mostrar mensaje si no se puede detectar la nariz
        if not nose_detected:
            text = font.render("No se detecta ninguna nariz", True, (255, 0, 0))
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text, text_rect)

        # Coordenadas del centro de la ventana pequeña
        cross_center_x_small = camera_width // 2
        cross_center_y_small = camera_height // 2

        # Dibujar la cruz que llega al límite de la ventana pequeña
        cross_color_small = (0, 0, 255)  # Color de la cruz (azul)
        cross_thickness_small = 2

        # Línea horizontal en la ventana pequeña
        pygame.draw.line(screen, cross_color_small, (0, cross_center_y_small), (camera_width, cross_center_y_small), cross_thickness_small)
        # Línea vertical en la ventana pequeña
        pygame.draw.line(screen, cross_color_small, (cross_center_x_small, 0), (cross_center_x_small, camera_height), cross_thickness_small)

        # Coordenadas del centro de la ventana principal
        cross_center_x_main = screen_width // 2
        cross_center_y_main = screen_height // 2

        # Dibujar la cruz que llega al límite de la ventana principal
        cross_color_main = (0, 0, 255)  # Color de la cruz (azul)
        cross_thickness_main = 2

        # Línea horizontal en la ventana principal
        pygame.draw.line(screen, cross_color_main, (0, cross_center_y_main), (screen_width, cross_center_y_main), cross_thickness_main)
        # Línea vertical en la ventana principal
        pygame.draw.line(screen, cross_color_main, (cross_center_x_main, 0), (cross_center_x_main, screen_height), cross_thickness_main)

        # Coordenadas de la nariz en la ventana pequeña
        if last_nose_x is not None and last_nose_y is not None:
            nose_x_small = int(last_nose_x * (screen_width / camera_width))
            nose_y_small = int(last_nose_y * (screen_height / camera_height))

            # Mostrar mensaje de salida del cursor si el círculo está fuera de la ventana blanca
            if not (0 <= nose_x_small < screen_width and 0 <= nose_y_small < screen_height):
                text = font.render("Salida del cursor", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, 20))
                screen.blit(text, text_rect)

            # Agregar la posición de la nariz a la lista
            nose_positions.append((nose_x_small, nose_y_small))

        # Dibujar todas las líneas que siguen el movimiento de la nariz
        line_color = (0, 0, 0)  # Negro
        line_thickness = 2
        if len(nose_positions) > 1:  # Verificar si hay suficientes puntos para dibujar una línea
            for i in range(len(nose_positions) - 1):
                pygame.draw.line(screen, line_color, nose_positions[i], nose_positions[i + 1], line_thickness)

        pygame.display.update()









