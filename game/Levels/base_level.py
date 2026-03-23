import pygame
from game.camera import Camera

class BaseLevel:
    def __init__(self, game):
        self.game = game
        self.player = game.player
        self.camera = game.camera

        self.enemies = game.enemies
        self.bullets = game.bullets
        self.points = game.points

        self.next_level = None

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        for enemy in self.enemies:
            enemy.update(self.player)

        for bullet in self.bullets:
            bullet.update()

        self.camera.update(self.player)

    def draw(self, screen):
        screen.fill((0, 0, 0))

        for enemy in self.enemies:
            enemy.draw(screen, self.camera)

        for bullet in self.bullets:
            bullet.draw(screen, self.camera)

        self.player.draw(screen, self.camera)
