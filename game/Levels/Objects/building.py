import pygame

class Building:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 128, 128)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (150, 75, 0), camera.apply(self.rect))
