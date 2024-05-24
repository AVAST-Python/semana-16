import pygame
import sys
import os

# Initialize Pygame
pygame.init()

DIRECTORY = os.path.dirname(__file__)

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Disparo")

FPS = 30
square_x, square_y = WIDTH // 2, HEIGHT // 2
square_size = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)

disparando = False
disparo_actual = 0
duracion_disparo = 1000  # Duration of each frame in milliseconds
disparo_coords = (100, 100)
tamaño_disparo = (50, 50)

disparo = [
    pygame.transform.scale(pygame.image.load(f'{DIRECTORY}/../sprites/game/disparo_{i+1}.png'), tamaño_disparo)
    for i in range(3)
]

# Main game loop
running = True
clock = pygame.time.Clock()

current_time = pygame.time.get_ticks()
last_frame_update = 0

def cambio_frame(current_time, last_frame_update):
    elapsed_time = current_time - last_frame_update
    return elapsed_time > duracion_disparo

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                disparando = True

    clock.tick(FPS)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the door
    # pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Draw the bullet
    if disparando:
        screen.blit(disparo[disparo_actual], disparo_coords)

        current_time = pygame.time.get_ticks()
        if(cambio_frame(current_time, last_frame_update)):
            last_frame_update = current_time
            disparo_actual += 1

        if disparo_actual >= len(disparo):
            disparando = False
            disparo_actual = 0

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
