import pygame

class Tree:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (0, 150, 0), camera.apply(self.rect))
