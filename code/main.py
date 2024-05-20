import pygame 

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True

surf = pygame.Surface((100, 200))


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