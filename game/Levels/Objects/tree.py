from .map_object import MapObject
import pygame

class Tree(MapObject):
    TILE_CHAR = "T"

    def __init__(self, x, y, tile_size):
        super().__init__(x, y, tile_size)
        self.destructible = True

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (0, 150, 0), camera.apply(self.rect))
