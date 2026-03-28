import pygame
from game.player import Player
from game.UI import UI
from game.enemy import Enemy
from game.camera import Camera

from game.Levels.tilemap_level1 import tilemap, TILE_SIZE
from game.Levels.map_loader import MapLoader


class Level1:
    def __init__(self):
        # Window setup
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("NeuroSight – Level 1")

        # MAP SIZE
        map_width_tiles = max(len(row) for row in tilemap)
        map_height_tiles = len(tilemap)

        self.MAP_WIDTH = map_width_tiles * TILE_SIZE
        self.MAP_HEIGHT = map_height_tiles * TILE_SIZE

        # assign camera
        self.camera = Camera(self.WIDTH, self.HEIGHT)

        # Main scene surface
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
        self.DESPAWN_DISTANCE = 2000

        # Player
        self.player = Player(self.WIDTH // 2, self.HEIGHT // 2)

        # Enemies
        self.enemies = []
        self.spawn_delay = 5000
        self.last_spawn = -5000

        # Load tilemap to level
        loader = MapLoader(tilemap, TILE_SIZE)
        self.map_objects = loader.load()

    # -----------------------------
    # MAIN LOOP
    # -----------------------------
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
            self.camera.update(self.player)

        return "MENU"

    # -----------------------------
    # EVENTS
    # -----------------------------
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return

                # reload
                if event.key == pygame.K_r:
                    self.player.weapon.start_reload()

                # shoot action
                if event.key == pygame.K_SPACE:
                    result = self.player.weapon.fire(self.player, self.camera)

                    if result:
                        if isinstance(result, list):
                            self.bullets.extend(result)
                        else:
                            self.bullets.append(result)
                        self.camera_shake(intensity=3, duration=80)

    # -----------------------------
    # COLLISIONS
    # -----------------------------
    def handle_bullet_enemy_collision(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemy_hit_actions()
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    break

    def handle_enemy_melee_attack(self):
        for enemy in self.enemies[:]:
            if self.player.rect.colliderect(enemy.rect):
                self.player.health -= 1
                self.enemies.remove(enemy)

    def handle_player_collisions(self):
        for obj in self.map_objects:
            if self.player.rect.colliderect(obj.rect):
                self.player.resolve_collision(obj.rect)

    def enemy_hit_actions(self):
        self.points += 1

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, [obj.rect for obj in self.map_objects])

        for bullet in self.bullets[:]:
            bullet.update()

            px, py = self.player.rect.center

            dx = bullet.rect.centerx - px
            dy = bullet.rect.centery - py

            if dx * dx + dy * dy > self.DESPAWN_DISTANCE * self.DESPAWN_DISTANCE:
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

        # weapon cooldown & reload
        self.player.weapon.update(self.clock.get_time())

    # -----------------------------
    # ENEMY SPAWN
    # -----------------------------
    def spawnEnemy(self):
        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.spawn_delay:
            self.last_spawn = now
            self.enemies.append(Enemy())

    # -----------------------------
    # CAMERA SHAKE
    # -----------------------------
    def camera_shake(self, intensity=5, duration=150):
        self.shake_intensity = intensity
        self.shake_timer = duration

    # -----------------------------
    # DRAW
    # -----------------------------
    def draw(self):
        self.display.fill((0, 0, 0))

        # 1. MAP
        for obj in self.map_objects:
            obj.draw(self.display, self.camera)

        # 2. BULLETS
        for bullet in self.bullets:
            bullet.draw(self.display, self.camera)

        # 3. ENEMIES
        for enemy in self.enemies:
            enemy.draw(self.display, self.camera)

        # 4. PLAYER
        self.player.draw(self.display, self.camera)

        # 5. UI
        if self.shake_affects_ui:
            self.UI.screen = self.display
            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullets))
            self.UI.drawPoints(self.points)
            self.UI.drawAmmo(self.player.weapon)

        ox, oy = self.camera_offset
        self.screen.blit(self.display, (ox, oy))

        if not self.shake_affects_ui:
            self.UI.screen = self.screen
            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullets))
            self.UI.drawPoints(self.points)
            self.UI.drawAmmo(self.player.weapon)

        pygame.display.flip()
