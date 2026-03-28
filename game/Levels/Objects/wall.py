from .map_object import MapObject
import pygame

class Wall(MapObject):
    TILE_CHAR = "B"

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (100, 100, 100), camera.apply(self.rect))
