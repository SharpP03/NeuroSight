import pygame
import math
import random
class Enemy:
    def __init__(self, x=None, y=None):
        size = 40

        # spawn on coordinates
        if x is not None and y is not None:
            self.rect = pygame.Rect(x, y, size, size)
            self.speed = 2
            return

        # Random spawn if no position provided
        width, height = pygame.display.get_window_size()

        side = random.choice(["top", "bottom", "left", "right"])

        positions = {
            "top":    (random.randint(0, width - size), -size),
            "bottom": (random.randint(0, width - size), height),
            "left":   (-size, random.randint(0, height - size)),
            "right":  (width, random.randint(0, height - size)),
        }

        x, y = positions[side]
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = 2
