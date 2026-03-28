import pygame

from game.Enemies.enemy_manager import EnemyManager
from game.collisions.collision_system import CollisionSystem
from game.player import Player
from game.UI import UI
from game.camera import Camera
from game.bullets.bullet_manager import BulletManager

from game.Levels.Map_Loader.tilemap_level1 import tilemap, TILE_SIZE
from game.Levels.Map_Loader.map_loader import MapLoader


class Level1:
    def __init__(self):
        # Window setup
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("NeuroSight – Level 1")

        # Map size
        map_width_tiles = max(len(row) for row in tilemap)
        map_height_tiles = len(tilemap)
        self.MAP_WIDTH = map_width_tiles * TILE_SIZE
        self.MAP_HEIGHT = map_height_tiles * TILE_SIZE

        # Camera
        self.camera = Camera(self.WIDTH, self.HEIGHT)

        # Main scene surface
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))

        # Clock
        self.clock = pygame.time.Clock()
        self.running = True

        # Camera shake
        self.camera_offset = [0, 0]
        self.shake_timer = 0
        self.shake_intensity = 0
        self.shake_affects_ui = True

        # UI
        self.UI = UI(self.screen)

        # Managers
        self.bullet_manager = BulletManager(despawn_distance=2000)
        self.enemy_manager = EnemyManager()

        # Player
        self.player = Player(self.WIDTH // 2, self.HEIGHT // 2)

        # Map
        loader = MapLoader(tilemap, TILE_SIZE)
        self.map_objects = loader.load()

        # Collision system
        self.collision = CollisionSystem(
            self.player,
            self.enemy_manager,
            self.map_objects,
            self.bullet_manager
        )

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

                if event.key == pygame.K_r:
                    self.player.weapon.start_reload()

                if event.key == pygame.K_SPACE:
                    bullets = self.player.weapon.fire(self.player, self.camera)
                    self.bullet_manager.add(bullets)
                    self.camera_shake(intensity=3, duration=80)

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys, [obj.rect for obj in self.map_objects])

        self.bullet_manager.update(self.player)
        self.enemy_manager.update(self.player)
        self.collision.update()

        # Camera shake
        dt = self.clock.get_time()
        if self.shake_timer > 0:
            self.shake_timer -= dt
            import random
            self.camera_offset[0] = random.randint(-self.shake_intensity, self.shake_intensity)
            self.camera_offset[1] = random.randint(-self.shake_intensity, self.shake_intensity)
        else:
            self.camera_offset = [0, 0]

        self.player.weapon.update(self.clock.get_time())

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

        # Map
        for obj in self.map_objects:
            obj.draw(self.display, self.camera)

        # Bullets
        self.bullet_manager.draw(self.display, self.camera)

        # Enemies
        self.enemy_manager.draw(self.display, self.camera)

        # Player
        self.player.draw(self.display, self.camera)

        # UI
        if self.shake_affects_ui:
            self.UI.screen = self.display
            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullet_manager.bullets))
            self.UI.drawPoints(self.player.points)
            self.UI.drawAmmo(self.player.weapon)

        ox, oy = self.camera_offset
        self.screen.blit(self.display, (ox, oy))

        if not self.shake_affects_ui:
            self.UI.screen = self.screen
            self.UI.drawPlayerHp(self.player.health)
            self.UI.debug(len(self.bullet_manager.bullets))
            self.UI.drawPoints(self.player.points)
            self.UI.drawAmmo(self.player.weapon)

        pygame.display.flip()
