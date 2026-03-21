import pygame

from game import player


class Bullet:
    def __init__(self, player):
        self.player = player
        self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
        self.speed = 7

        #mouse
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

    def update(self):
        # Apply direction and speed
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
