import pygame

from game.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.spawn_delay = 5000
        self.last_spawn = -5000
        self.points = 0

    def update(self, player):
        for enemy in self.enemies:
            enemy.update(player)

        self.spawn()

    def spawn(self):
        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.spawn_delay:
            self.last_spawn = now
            self.enemies.append(Enemy())

    def draw(self, screen, camera):
        for enemy in self.enemies:
            enemy.draw(screen, camera)
