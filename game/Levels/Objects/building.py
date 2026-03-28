from .map_object import MapObject
import pygame

class Building(MapObject):
    TILE_CHAR = "H"

    def __init__(self, x, y, tile_size):
        super().__init__(x, y, tile_size * 2)  # 2×2 tile
        self.solid = True

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (150, 75, 0), camera.apply(self.rect))
