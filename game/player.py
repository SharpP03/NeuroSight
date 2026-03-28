import pygame
from .weapons.pistol import Pistol
from .weapons.shotgun import Shotgun

class Player:
    def __init__(self, x, y):
        # collider
        self.rect = pygame.Rect(x, y, 50, 50)

        # movement
        self.speed = 5
        self.vel_x = 0
        self.vel_y = 0

        # stats
        self.health = 10

        # weapon system
        self.weapon = Shotgun()

    # -----------------------------------
    # MOVEMENT + NORMALIZATION
    # -----------------------------------
    def handle_input(self, keys):
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

        # normalize diagonal movement
        length = (dx*dx + dy*dy) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        self.vel_x = dx * self.speed
        self.vel_y = dy * self.speed

    # -----------------------------------
    # UPDATE
    # -----------------------------------
    def update(self, keys, colliders):
        self.handle_input(keys)

        # --- MOVE X ---
        self.rect.x += self.vel_x
        for rect in colliders:
            self.resolve_collision(rect, self.vel_x, 0)

        # --- MOVE Y ---
        self.rect.y += self.vel_y
        for rect in colliders:
            self.resolve_collision(rect, 0, self.vel_y)

    # -----------------------------------
    # COLLISION RESOLUTION (AABB)
    # -----------------------------------
    def resolve_collision(self, rect, vel_x, vel_y):
        if not self.rect.colliderect(rect):
            return

        # --- X AXIS ---
        if vel_x > 0:      # moving right
            self.rect.right = rect.left
        elif vel_x < 0:    # moving left
            self.rect.left = rect.right

        # --- Y AXIS ---
        if vel_y > 0:      # moving down
            self.rect.bottom = rect.top
        elif vel_y < 0:    # moving up
            self.rect.top = rect.bottom

    # -----------------------------------
    # DRAW
    # -----------------------------------
    def draw(self, screen, camera):
        pygame.draw.rect(screen, (150, 10, 222), camera.apply(self.rect))
