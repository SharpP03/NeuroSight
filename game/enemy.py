import pygame
import math
import random

class Enemy:
    def __init__(self):
        width, height = pygame.display.get_window_size()
        size = 40

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

    def update(self, player):
        # Enemy pos
        ex = self.rect.centerx
        ey = self.rect.centery

        # Player pos
        px = player.rect.centerx
        py = player.rect.centery


        # distance
        dx = px - ex
        dy = py - ey
        dist = math.sqrt(dx * dx + dy * dy)

        # normalizacja
        if dist != 0:
            dx /= dist
            dy /= dist

        # ruch przeciwnika
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (255, 0, 0), camera.apply(self.rect))


