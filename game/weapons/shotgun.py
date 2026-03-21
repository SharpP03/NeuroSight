from .weapon import Weapon
from ..bullet import Bullet
import math

class Shotgun(Weapon):
    def __init__(self):
        super().__init__()
        self.mag_size = 2
        self.ammo_in_mag = 2
        self.reserve_ammo = 20
        self.reload_time = 1500
        self.fire_rate = 800
        self.damage = 2

    def fire(self, player):
        if not self.can_fire():
            return []

        self.ammo_in_mag -= 1
        self.fire_cooldown = self.fire_rate

        bullets = []
        spread = [-15, -5, 0, 5, 15]

        for angle in spread:
            b = Bullet(player, angle_offset=angle)
            bullets.append(b)

        return bullets
