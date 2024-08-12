import pygame 
import random
class Butterfly:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bgrmA.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move_left_to_right(self):
        self.x = self.x+1
        self.y = self.y+1

    def move_right_to_left(self):
        self.x = self.x-1
        self.y = self.y-1


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    butterfly = Butterfly(400, 300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        butterfly.draw(screen)
        pygame.display.update()

