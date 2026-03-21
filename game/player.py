import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 5
        self.health = 10;

    def update(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 10, 222), self.rect)
