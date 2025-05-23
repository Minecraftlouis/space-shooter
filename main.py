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
space_shooter_logo = pygame.transform.scale(space_shooter_logo, (300, 150))
fps=60
pygame.display.set_caption("space shotter")
def welcome_screen():
    while True:
        window_screen.blit(background, (0, 0))
        window_screen.blit(space_shooter_logo, (width//3, 40))
        welcome_font = pygame.font.SysFont("impact", 24)
        welcome_text = welcome_font.render("Press Any Key To Begin...", 1, WHITE)
        window_screen.blit(welcome_text, (width //2 - welcome_text.get_width() //2, height //2 - welcome_text.get_height() //2))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print("Start the game")
        pygame.display.update()
welcome_screen()
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


