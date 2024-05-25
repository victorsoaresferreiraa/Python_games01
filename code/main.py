import pygame 
from os.path import join

from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.clock()


surf = pygame.Surface((100, 200))
surf.fill('orange')

player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

star_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
star_position = [(randint (Q, WINDOW_WIDTH), radint(0, WINDOW_HEIGHT)) for i in range(20)]


while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            

    # Draw the game
    #fill the window 
    display_surface.fill('darkgray')
    display_surface.blit(surf, (100, 400))
    pygame.display.update()
    
        
pygame.quit()