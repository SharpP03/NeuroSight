import pygame
from .player import Player
from .bullet import Bullet
from .UI import UI
from .enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()

        # Window setup
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("NeuroSight")

        # clock and game life cycle
        self.clock = pygame.time.Clock()
        self.running = True

        # game parameters
        self.points = 0

        # User Interface
        self.UI = UI(self.screen)

        # Entities
        self.bullets = []

        # Player parameters
        self.player = Player(self.WIDTH // 2, self.HEIGHT // 2)

        # Enemy parameters
        self.enemies = []
        self.spawn_delay = 5000
        self.last_spawn = -5000

    # Main loop
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self.player))

    def handle_bullet_enemy_collision(self):
        # copy lists [:]
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):

                    # actions
                    self.enemy_hit_actions()

                    # cleanup
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    break

    def enemy_hit_actions(self):
        self.points += 1


    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

        for bullet in self.bullets:
            bullet.update()

            # remove bullet if outside screen
            if (bullet.rect.x < 0 or bullet.rect.x > self.WIDTH or
                bullet.rect.y < 0 or bullet.rect.y > self.HEIGHT):
                    self.bullets.remove(bullet)

        for enemy in self.enemies:
            enemy.update(self.player)

        self.handle_bullet_enemy_collision()

        self.spawnEnemy()

    def spawnEnemy(self):
        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.spawn_delay:
            self.last_spawn = now
            self.enemies.append(Enemy())

    def enemyCollide(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                print("hit")

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.player.draw(self.screen)

        self.UI.drawPlayerHp(self.player.health)
        self.UI.debug(len(self.bullets))
        self.UI.drawPoints(self.points)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.flip()
