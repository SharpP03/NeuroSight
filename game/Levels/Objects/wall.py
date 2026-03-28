import pygame

class Wall:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (100, 100, 100), camera.apply(self.rect))
