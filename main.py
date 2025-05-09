import pygame
from pygame.locals import *
import sys
pygame.init()
width= 800
height = 600
window_screen=pygame.display.set_mode(size=(width,height))
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (110,194,54)
BLUE  = (23,54,235)
background = pygame.transform.scale(pygame.image.load('gallery/sprites/background.png'),(width, height)).convert()
space_shooter_logo = pygame.image.load('gallery/sprites/space_shooter.png').convert_alpha()
fps=60
pygame.display.set_caption("space shotter")
def welcome_screen():
    while True:
        window_screen.blit(background, (0, 0))
        window_screen.blit(space_shooter_logo, (width//3, 40))

while True:
    pygame.display.update()
    fps_controller = pygame.time.Clock()
    fps_controller.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print ("space pressed")
        if event.type == pygame.QUIT:
            pygame.quit()

