import pygame
from pygame.locals import *
import sys

pygame.init()

# constants
width = 800
ship_width = 55
ship_height = 40
max_num_of_bullets = 5
bullet_velocity = 7
height = 600
fps = 60
paused = False
ship_velocity = 5
green_hit = pygame.USEREVENT + 1
blue_hit = pygame.USEREVENT + 2
border = pygame.Rect((width // 2)- 5, 0, 10, height)

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (110,194,54)
BLUE  = (23,54,235)


# resources
window_screen=pygame.display.set_mode(size=(width,height))
background = pygame.transform.scale(pygame.image.load('gallery/sprites/background.png'),(width, height)).convert()
space_shooter_logo = pygame.image.load('gallery/sprites/space_shooter.png').convert_alpha()
space_shooter_logo = pygame.transform.scale(space_shooter_logo, (300, 150))

explosion_image = pygame.image.load ('gallery/sprites/do_explosion.png').convert_alpha()
explosion_image = pygame.transform.scale(explosion_image, (200, 150))
green_ship_img = pygame.transform.rotate(pygame.image.load('gallery/sprites/shipGreen.png'), 270)
blue_ship_img = pygame.transform.rotate(pygame.image.load('gallery/sprites/shipBlue.png'), 90)
green_ship = pygame.transform.scale (green_ship_img, (ship_width, ship_height)).convert_alpha()
blue_ship = pygame.transform.scale(blue_ship_img, (ship_width, ship_height)).convert_alpha()
bullet_fire_sound = pygame.mixer.Sound('gallery/audio/sfx_fire.ogg')
bullet_hit_sound = pygame.mixer.Sound('gallery/audio/sfx_hit.ogg')

pygame.display.set_caption("space shotter")

def handle_bullets(green_bullets, blue_bullets, green_rect, blue_rect):
    for bullet in green_bullets:
        bullet.x += bullet_velocity
        if blue_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(blue_hit))
            green_bullets.remove(bullet)
        elif bullet.x > width:
            green_bullets.remove(bullet)
    for bullet in blue_bullets:
        bullet.x -= bullet_velocity
        if green_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(green_hit))
            blue_bullets.remove(bullet)
        elif bullet.x < 0:
            blue_bullets.remove(bullet)
            
def blue_movement_handler(keys_pressed, blue_ship):
    global paused
    if paused == False:
        if keys_pressed[pygame.K_LEFT] and blue_ship.x - ship_velocity > border.x + border.width -5:
            blue_ship.x -= ship_velocity
        if keys_pressed[pygame.K_RIGHT] and blue_ship.x - ship_velocity + blue_ship.width < width - 5:
            blue_ship.x += ship_velocity
        if keys_pressed[pygame.K_UP] and blue_ship.y - ship_velocity > 0:
            blue_ship.y -= ship_velocity
        if keys_pressed[pygame.K_DOWN] and blue_ship.y - ship_velocity + blue_ship.height < height - 5:
            blue_ship.y += ship_velocity
        
            
            
def green_movement_handler(keys_pressed, green_ship):
    global paused
    if paused == False:
        if keys_pressed[pygame.K_w] and green_ship.y - ship_velocity > 0:
            green_ship.y -= ship_velocity
        if keys_pressed[pygame.K_a] and green_ship.x - ship_velocity > -5:
            green_ship.x -= ship_velocity
        if keys_pressed[pygame.K_s] and green_ship.y - ship_velocity +    green_ship.height < height - 5:
            green_ship.y += ship_velocity
        if keys_pressed[pygame.K_d] and green_ship.x - ship_velocity + green_ship.width < border.x -5:
            green_ship.x += ship_velocity
            
        
        

def main(): 
    global paused
    clock = pygame.time.Clock()
    green_rect = pygame.Rect(100, 100, ship_width, ship_height)
    blue_rect = pygame.Rect(700, 300, ship_width, ship_height)

    green_bullets = []
    blue_bullets = []
    green_health = 10
    blue_health = 10

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if paused == False:
                    if event.key == pygame.K_LCTRL and len(green_bullets)< max_num_of_bullets:
                        bullet = pygame.Rect(green_rect.x + green_rect.width, green_rect.y + green_rect.height // 2,10,5)
                        green_bullets.append(bullet)
                        bullet_fire_sound.play()
                    if event.key == pygame.K_RCTRL and len(blue_bullets)< max_num_of_bullets:
                        bullet = pygame.Rect(blue_rect.x, blue_rect.y + blue_rect.height // 2, 10, 5)
                        blue_bullets.append(bullet)                        
                        bullet_fire_sound.play()
                        
                        
                    
                    
            #health changes
            if event.type == green_hit:
                    green_health -= 1
                    bullet_hit_sound.play()
                    
            if event.type == blue_hit:
                    blue_health -= 1
                    bullet_hit_sound.play()
                    
        # print(keys_pressed[pygame.K_LEFT], keys_pressed[pygame.K_RIGHT])
        # print(green_health, blue_health)
        # print(green_bullets, blue_bullets)
        
        # handle movements and bullets
        keys_pressed = pygame.key.get_pressed()
        green_movement_handler(keys_pressed, green_rect)
        blue_movement_handler(keys_pressed, blue_rect)
        handle_bullets(green_bullets, blue_bullets, green_rect, blue_rect)
        
        # rendering stuff
        window_screen.blit(background, (0, 0))
        pygame.draw.rect(window_screen, WHITE, border)
        
        #ship health
        health_font = pygame.font.SysFont("impact", 24)
        green_health_text = health_font.render( str(green_health), 1, GREEN)
        window_screen.blit(green_health_text, (10,10))
    
        blue_health_text = health_font.render( str(blue_health), 1, BLUE)
        window_screen.blit(blue_health_text, (770,10))
        
        window_screen.blit(green_ship, (green_rect.x, green_rect.y))
        window_screen.blit(blue_ship, (blue_rect.x, blue_rect.y))
        
        for bullet in green_bullets:
            pygame.draw.rect(window_screen, GREEN, bullet)
        for bullet in blue_bullets:
            pygame.draw.rect(window_screen, BLUE, bullet)
            
        game_over(green_health,blue_health,green_rect,blue_rect)

        pygame.display.update()
        
def game_over(green_health, blue_health,green_rect,blue_rect):
    global paused
    if (green_health == 0):
        print("GREEN DEAD")
        window_screen.blit(explosion_image, (green_rect.x-50,green_rect.y-50))
        paused = True     
        
    if (blue_health == 0):
        print("BLUE DEAD")
        window_screen.blit(explosion_image, (blue_rect.x-50,blue_rect.y-50))
        paused = True       

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


