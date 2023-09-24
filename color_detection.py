import pygame
import numpy as np
import pandas as pd

# Reading the image file path from user input
img_path = input("Enter the image path: ")

# Reading the image with Pygame
pygame.init()
img = pygame.image.load(img_path)
img = pygame.transform.scale(img, (800, 600))  # Resize the image to fit the screen

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

# Pygame setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Color Picker")

def get_color_at_position(x, y):
    color = img.get_at((x, y))
    return color.r, color.g, color.b

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.blit(img, (0, 0))

    # Check if the "C" key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c]:
        xpos, ypos = pygame.mouse.get_pos()
        r, g, b = get_color_at_position(xpos, ypos)

        pygame.draw.rect(screen, (b, g, r), (20, 20, 750, 60))
        text = f'R={r} G={g} B={b}'
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, 50))

        if r + g + b >= 600:
            text_surface = font.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (50, 50))

    pygame.display.flip()

pygame.quit()
