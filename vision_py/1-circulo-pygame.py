import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Círculo en Pygame")

# Colores (en formato RGB)
white = (255, 255, 255)
red = (255, 0, 0)

# Coordenadas del centro y radio del círculo
circle_center = (400, 300)  # Centro del círculo
circle_radius = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo blanco
    screen.fill(white)

    # Dibujar un círculo rojo
    pygame.draw.circle(screen, red, circle_center, circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()
