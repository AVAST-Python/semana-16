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

while running:
    # Gestiona eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(30) # Ajusta FPS

    # Pinta algo
    pygame.draw.rect(
      screen, (255,0,0),
      (square_x, square_y, square_size, square_size)
    )

    # Actualiza el display
    pygame.display.flip()
```

Notes:
```python
# Clear the screen
screen.fill((255,255,255))
```


---

Pybox2D

Sprites:
https://www.reddit.com/r/spelunky/comments/ur5eor/terminalmontages_mario_sprite_for_spelunky_made/

---

Ejemplo de juego a conseguir
Cómo funciona pygame
Event Loop
Pintar imágenes
Layers
Sprites

Ajustar velocidad / fps
https://realpython.com/lessons/game-speed/
Time deltas






---

# Rangos


---

# Tuplas

https://realpython.com/python-tuple/
fixed and unchangeable series of values
puede contener múltiples tipos
cero index





---


# Diccionarios


