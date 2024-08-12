import pygame
import sys

#  class
class Barbie:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= 2
    
    
    def move_right(self):
        if self.rect.x < 600 - 50:
            self.rect.x += 2
    
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 2
    
    
    def move_down(self):
        if self.rect.y < 400 - 50:
            self.rect.y += 2
