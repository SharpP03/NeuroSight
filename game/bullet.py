import pygame

class Bullet:
    def __init__(self, player):
        self.rect = pygame.Rect(player.rect.centerx, player.rect.centery, 10, 10)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
