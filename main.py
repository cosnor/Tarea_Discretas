import pygame

pygame.init()

# Dimensiones
ventana = pygame.display.set_mode((1000, 600))

# Título de la ventana
pygame.display.set_caption("Teorema de Hakimi-Havel")

# Color de fondo
color_fondo = (255, 255, 255)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    ventana.fill(color_fondo)
    
    # Actualizar la pantalla
    pygame.display.flip()