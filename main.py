import pygame
from pygame.locals import *
import sys
pygame.init()
width= 800
height = 600
window_screen=pygame.display.set_mode(width,height)
WHITE = (255,255,255)
BLACK = (0,0,0)
fps=60
pygame.display.set_caption("space shotter")
while True:
    pygame.display.update()
    fps_controller = pygame.time.Clock()
    fps_controller.tick(fps)
    for event in pygame.event.get():
        if event.key == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print ("space pressed")
        if event.type == pygame.QUIT:
            pygame.quit()

