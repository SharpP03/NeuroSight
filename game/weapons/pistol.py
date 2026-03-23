from .weapon import Weapon
from ..bullet import Bullet

class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.mag_size = 8
        self.ammo_in_mag = 8
        self.reserve_ammo = 40
        self.reload_time = 1000
        self.fire_rate = 250  # ms
        self.damage = 1

    def fire(self, player, camera):
        if not self.can_fire():
            return None

        self.ammo_in_mag -= 1
        self.fire_cooldown = self.fire_rate

        return Bullet(player, camera)

