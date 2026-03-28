import pygame

class MapObject:
    TILE_CHAR = None 

    def __init__(self, x, y, tile_size):
        self.rect = pygame.Rect(x, y, tile_size, tile_size)
        self.solid = True
        self.destructible = False

    def draw(self, screen, camera):
        raise NotImplementedError
