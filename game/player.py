import pygame


class Player:
    def __init__(self, x, y):
        # base model
        self.rect = pygame.Rect(x, y, 50, 50)

        # player parameters
        self.speed = 5
        self.health = 10;

        # Ammo system
        self.mag_size = 8        # mag size
        self.ammo_in_mag = 8     # current ammo
        self.reserve_ammo = 40   # ammo capacity
        self.reloading = False
        self.reload_time = 1000  # reload time
        self.reload_timer = 0

    def start_reload(self):
        if not self.reloading and self.ammo_in_mag < self.mag_size and self.reserve_ammo > 0:
            self.reloading = True
            self.reload_timer = self.reload_time

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

        if self.reloading:
            self.reload_timer -= 16  # ~60 FPS
            if self.reload_timer <= 0:
                self.reloading = False
                needed = self.mag_size - self.ammo_in_mag
                to_load = min(needed, self.reserve_ammo)
                self.ammo_in_mag += to_load
                self.reserve_ammo -= to_load

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 10, 222), self.rect)
