import pygame


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 5
        self.health = 10;

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
            dx = dx / length
            dy = dy / length

        # apply movement
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 10, 222), self.rect)
