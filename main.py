import pygame
from pygame.locals import *
import sys
pygame.init()

#constants
width= 800
ship_width= 55
ship_height= 40
max_num_of_bullets= 5
height = 600
fps=60

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (110,194,54)
BLUE  = (23,54,235)

#recourses
window_screen=pygame.display.set_mode(size=(width,height))
background = pygame.transform.scale(pygame.image.load('gallery/sprites/background.png'),(width, height)).convert()
space_shooter_logo = pygame.image.load('gallery/sprites/space_shooter.png').convert_alpha()
space_shooter_logo = pygame.transform.scale(space_shooter_logo, (300, 150))
bullet_fire_sound = pygame.mixer.Sound('gallery/audio/sfx_fire.ogg')
pygame.display.set_caption("space shotter")

def main():
    clock = pygame.time.Clock()
    green_rect = pygame.Rect(100, 100, ship_width, ship_height)
    blue_rect = pygame.Rect(700, 300, ship_width, ship_height)

    green_bullets = []
    blue_bullets = []
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(green_bullets)< max_num_of_bullets:
                    bullet_fire_sound.play()
                if event.key == pygame.K_RCTRL and len(blue_bullets)< max_num_of_bullets:
                    bullet_fire_sound.play() 

                

        window_screen.blit(background, (0, 0))
        pygame.display.update()




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
                main()
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


