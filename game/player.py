import pygame
from .weapons.pistol import Pistol
from .weapons.shotgun import Shotgun

class Player:
    def __init__(self, x, y):
        # base model
        self.rect = pygame.Rect(x, y, 50, 50)

        # player parameters
        self.speed = 5
        self.health = 10

        # Weapon system
        self.weapon = Pistol()

    def update(self, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1

        # movement normalization
        length = (dx*dx + dy*dy) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        # apply movement
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (150, 10, 222), camera.apply(self.rect))

