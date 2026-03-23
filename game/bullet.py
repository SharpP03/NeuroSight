import pygame
import math

class Bullet:
    def __init__(self, player, angle_offset=0):
        self.player = player

        # base bullet rect
        self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
        self.speed = 7

        # mouse
        self.mouse = pygame.mouse.get_pos()
        self.mouse_x = self.mouse[0]
        self.mouse_y = self.mouse[1]

        # Length vector from mouse to player
        self.dx = self.mouse_x - self.player.rect.centerx
        self.dy = self.mouse_y - self.player.rect.centery

        # Vector Normalization
        length = (self.dx ** 2 + self.dy ** 2) ** 0.5
        if length != 0:
            self.dx /= length
            self.dy /= length

        # Angle offset
        if angle_offset != 0:
            rad = math.radians(angle_offset)
            rotated_dx = self.dx * math.cos(rad) - self.dy * math.sin(rad)
            rotated_dy = self.dx * math.sin(rad) + self.dy * math.cos(rad)

            self.dx = rotated_dx
            self.dy = rotated_dy

    def update(self):
        # Apply direction and speed
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (255, 255, 0), camera.apply(self.rect))

