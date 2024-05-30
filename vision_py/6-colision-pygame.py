import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colisión de Círculo y Rectángulo en Pygame")

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
rectangle_width = 10
rectangle_height = 40

# Velocidad de movimiento del círculo
circle_speed = 0.2

# Bandera para controlar si hubo colisión
collision = False

font = pygame.font.Font(None, 36)  # Fuente para el letrero

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
        collision = True
    else:
        collision = False

    # Dibujar un letrero si hay colisión
    if collision:
        text = font.render("Colisión (ó, dio click! :))", True, (0, 0, 0))  # Texto de colisión en negro
        screen.blit(text, (400, 10))

    # Dibujar un círculo en el centro del cuadrado
    pygame.draw.circle(screen, white, (circle_x, circle_y), circle_radius - 10)

    # Actualizar la pantalla
    pygame.display.flip()
