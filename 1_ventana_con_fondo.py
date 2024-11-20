# ------------------------------------------------------------
# Programa para crear una ventana y pintarla del color deseado
# ------------------------------------------------------------

# Importar los módulos de "pygame" e iniciarlos
import pygame
pygame.init()


# Definir el tamaño de la ventana ancho x alto (en pixels)
screen = pygame.display.set_mode([500, 500])


# Escoger un color para la pantalla (RGB)
# https://www.w3schools.com/colors/colors_picker.asp
screen.fill((51, 153, 102))

# Pintar (refrescar) la pantalla (y salir del programa...)
pygame.display.flip()
