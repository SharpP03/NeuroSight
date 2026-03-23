import pygame
import math

class Bullet:
    def __init__(self, player, camera, angle_offset=0):
        self.player = player

        # base bullet rect
        self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
        self.speed = 7

        # mouse position on SCREEN
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # convert to WORLD coordinates
        mouse_world_x = mouse_x + camera.offset.x
        mouse_world_y = mouse_y + camera.offset.y

        # direction vector from player to mouse in WORLD space
        self.dx = mouse_world_x - self.player.rect.centerx
        self.dy = mouse_world_y - self.player.rect.centery

        # normalize
        length = (self.dx ** 2 + self.dy ** 2) ** 0.5
        if length != 0:
            self.dx /= length
            self.dy /= length

        # angle offset (shotgun spread etc.)
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

