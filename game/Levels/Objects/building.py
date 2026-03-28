import pygame

class Building:
    def __init__(self, x, y, tile_size):
        self.rect = pygame.Rect(x, y, tile_size * 2, tile_size * 2)  # np. 2×2 tile

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (150, 75, 0), camera.apply(self.rect))
