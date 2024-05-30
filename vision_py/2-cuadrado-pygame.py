import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrado en Pygame")

# Colores (en formato RGB)
white = (255, 255, 255)
blue = (0, 0, 255)

# Coordenadas y tamaño del cuadrado
square_x = 350
square_y = 250
square_size = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo blanco
    screen.fill(white)

    # Dibujar un cuadrado azul
    pygame.draw.rect(screen, blue, (square_x, square_y, square_size, square_size))

    # Actualizar la pantalla
    pygame.display.flip()
