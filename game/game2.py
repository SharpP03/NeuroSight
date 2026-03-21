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

        # Main scene
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))

        # clock and game life cycle
        self.clock = pygame.time.Clock()
        self.running = True

        # visual effects parameters
        self.camera_offset = [0, 0]
        self.shake_timer = 0
        self.shake_intensity = 0
        self.shake_affects_ui = True

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
                # reload
                if event.key == pygame.K_r:
                    self.player.weapon.start_reload()

                # shoot action
                if event.key == pygame.K_SPACE:
                    result = self.player.weapon.fire(self.player)
                    if result:
                        if isinstance(result, list):
                            self.bullets.extend(result)
                        else:
                            self.bullets.append(result)
                        self.camera_shake(intensity=3, duration=80)

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

    def handle_enemy_melee_attack(self):
        for enemy in self.enemies[:]:
            if self.player.rect.colliderect(enemy.rect):
                self.player.health -= 1
                self.enemies.remove(enemy)

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
        self.handle_enemy_melee_attack()

        self.spawnEnemy()

        # camera shake
        dt = self.clock.get_time()

        if self.shake_timer > 0:
            self.shake_timer -= dt
            import random
            self.camera_offset[0] = random.randint(-self.shake_intensity, self.shake_intensity)
            self.camera_offset[1] = random.randint(-self.shake_intensity, self.shake_intensity)
        else:
            self.camera_offset = [0, 0]

            self.player.weapon.update(self.clock.get_time())

    def spawnEnemy(self):
        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.spawn_delay:
            self.last_spawn = now
            self.enemies.append(Enemy())

    def enemyCollide(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                print("hit")

    def camera_shake(self, intensity=5, duration=150):
        self.shake_intensity = intensity
        self.shake_timer = duration

    def draw(self):
        # Prepare scene
        self.display.fill((0, 0, 0))

        self.player.draw(self.display)

        for bullet in self.bullets:
            bullet.draw(self.display)

        for enemy in self.enemies:
            enemy.draw(self.display)

        # UI with shake effect
        if self.shake_affects_ui:
            self.UI.screen = self.display  # assign layer with shake

            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullets))
            self.UI.drawPoints(self.points)
            self.UI.drawAmmo(self.player.weapon)


        # Get offset
        ox, oy = self.camera_offset

        # Render scene with offset
        self.screen.blit(self.display, (ox, oy))

        # UI without shake effect
        if not self.shake_affects_ui:
            self.UI.screen = self.screen

            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullets))
            self.UI.drawPoints(self.points)
            self.UI.drawAmmo(self.player.weapon)


        pygame.display.flip()
