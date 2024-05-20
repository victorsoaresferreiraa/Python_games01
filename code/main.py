import pygame 

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
Running = pygame.window("lalala")



while Running:
    #event loop
    for event in pygame.event.get():
        if event.tipe == pygame.QUIT:
            pygame.quit()
            

    # Draw the game
    #fill the window 
    
    pygame.display.update()
    
        
pygame.quit()