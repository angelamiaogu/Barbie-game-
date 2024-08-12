import pygame
from barbie import Barbie
from butterfly import Butterfly
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Barbie on Screen")
        
        # Create a Barbie object
        self.barbie = Barbie("small_barbie.png", 100, 100)
        self.butterflys = [Butterfly(400, 300)]



    
    
        
    
    
    def run(self):
        terminate = 'no'
        while True:
            if terminate == 'yes':
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Move the Barbie object
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.barbie.move_left()
            if keys[pygame.K_RIGHT]:
                self.barbie.move_right()
            if keys[pygame.K_UP]:
                self.barbie.move_up()
            if keys[pygame.K_DOWN]:
                self.barbie.move_down()

            # Move the Butterfly object
            for butterfly in self.butterflys:
                if self.barbie.rect.colliderect(butterfly.rect):
                    terminate = 'yes'
                

            # Fill the screen with white
            self.screen.fill((255, 255, 255))
            
            # Draw the Barbie object
            self.barbie.draw(self.screen)
            for butterfly in self.butterflys:
                butterfly.draw(self.screen)
            
            # Update the display
            pygame.display.flip()
