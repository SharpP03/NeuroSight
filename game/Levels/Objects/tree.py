import pygame

class Tree:
    def __init__(self, x, y, tile_size):
        self.rect = pygame.Rect(x, y, tile_size, tile_size)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (0, 150, 0), camera.apply(self.rect))
