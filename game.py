import pygame 


if __name__ == "__main__":
    pygame.init() 
    canvas = pygame.display.set_mode((500, 500)) 
    pygame.display.set_caption("RL Game") 
    exit = False

    while not exit: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                exit = True
        pygame.display.update() 
