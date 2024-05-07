# Introducción a Python

## Semana 15
<!-- .element style="text-align:center" -->

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

<section data-background-iframe="https://www.youtube.com/embed/Ln0T5bjDuWw?si=u7CGP0xyLahAQloF&amp;start=16">
</section>

---

# Pygame

Qué es:
- Motor de juegos 2D
- Gestión de eventos y dibujo de frames
- Colisiones

Qué no es:
- Juegos 3D
- Motor físico (se puede usar uno como Pybox2D)

---

# Cómo trabajar

En local:
- Sigue las instrucciones de `ejemplos/README.md`

Online:
- https://trinket.io/features/pygame
- https://replit.com/languages/pygame

---

# Main Loop

```python
import pygame

running = True

while running:
    # Gestiona eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(30) # Ajusta FPS

    # Actualiza el display
    pygame.display.flip()
```
<!-- .element style="font-size: 1.5rem;" -->

---

# Pintar algo

```python
...

# Prepara la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

square_size = 10
x, y = 100,100

while running:
    # Gestiona eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(30) # Ajusta FPS

    # Pinta algo
    pygame.draw.rect(
      screen, (255,0,0),
      (x, y, square_size, square_size)
    )

    # Actualiza el display
    pygame.display.flip()
```
<!-- .element style="font-size: 1.5rem;" -->

---

# Movimiento

- Hay que mover las cosas "a mano": manten la posición en variables
- Ojo con la velocidad:
    ```python
    # dt = tiempo desde el último frame, en ms
    dt = clock.tick(30) / 1000.0  # Convert milliseconds to seconds

    # Move the text based on velocity and time elapsed
    text_rect.x += velocity_x * dt
    text_rect.y += velocity_y * dt
    ```
    <!-- .element style="font-size: 1.5rem;" -->
- Controlar las teclas: ojo, que no es lo mismo apretar que soltar

- Hay que repintar el fondo o se deja rastro



Notes:
```python
# Clear the screen
screen.fill((255,255,255))
```

---

# Imágenes

Uso básico de imágenes:
```python
mario = pygame.image.load('sprites/mario/mario_quieto.png')
screen.blit(mario, (mario_x, mario_y))
```
<!-- .element style="font-size: 1.5rem;" -->

Se pueden usar varias imágenes para simular movimiento

---

# Próximo día

- Layers
- Sprites




