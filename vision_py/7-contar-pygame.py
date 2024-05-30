import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisión y Contador en Pygame")

# Colores (en formato RGB)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Coordenadas y tamaño del cuadrado
square_x = 300
square_y = 200
square_size = 200

# Coordenadas del centro del círculo
circle_x = square_x + square_size // 2
circle_y = square_y + square_size // 2
circle_radius = 20

# Coordenadas y tamaño del rectángulo rojo
rectangle_x = square_x + 50
rectangle_y = square_y + 50
rectangle_width = 80
rectangle_height = 20

# Velocidad de movimiento del círculo
circle_speed = 0.2

# Bandera para controlar si hubo colisión
collision = False

font = pygame.font.Font(None, 36)  # Fuente para el letrero

# Tiempo de inicio de la colisión
collision_start_time = 0

# Contador para mostrar después de 2 segundos de colisión
counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Mover el círculo en respuesta a las teclas presionadas, pero asegurarse de que no supere los límites del cuadrado
    if keys[pygame.K_LEFT] and circle_x - circle_radius > square_x:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT] and circle_x + circle_radius < square_x + square_size:
        circle_x += circle_speed
    if keys[pygame.K_UP] and circle_y - circle_radius > square_y:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN] and circle_y + circle_radius < square_y + square_size:
        circle_y += circle_speed

    # Dibujar el fondo blanco
    screen.fill(white)

    # Dibujar un cuadrado azul
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

    # Dibujar un rectángulo rojo
    pygame.draw.rect(screen, red, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))

    # Comprobar colisión entre el círculo y el rectángulo
    if circle_x + circle_radius > rectangle_x and circle_x - circle_radius < rectangle_x + rectangle_width and circle_y + circle_radius > rectangle_y and circle_y - circle_radius < rectangle_y + rectangle_height:
        if not collision:
            collision_start_time = time.time()  # Registrar el tiempo de inicio de la colisión
        collision = True
    else:
        collision = False

    # Calcular el tiempo de colisión
    if collision:
        collision_time = time.time() - collision_start_time
    else:
        collision_time = 0

    # Mostrar el tiempo de colisión en el letrero
    collision_text = font.render(f"Colisión: {collision_time:.2f} segundos", True, (0, 0, 0))

    # Dibujar el letrero de colisión
    screen.blit(collision_text, (10, 10))

    # Aumentar el contador después de 2 segundos de colisión
    if collision_time >= 2:
        counter += 1

    # Mostrar el contador en el letrero
    counter_text = font.render(f"Contador: {counter}", True, (0, 0, 0))

    # Dibujar el letrero del contador
    screen.blit(counter_text, (10, 50))

    # Dibujar un círculo en el centro del cuadrado
    pygame.draw.circle(screen, white, (circle_x, circle_y), circle_radius - 10)

    # Actualizar la pantalla
    pygame.display.flip()
