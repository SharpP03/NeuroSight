class Weapon:
    def __init__(self):
        self.mag_size = 0
        self.ammo_in_mag = 0
        self.reserve_ammo = 0

        self.reload_time = 0
        self.reloading = False
        self.reload_timer = 0

        self.fire_rate = 0
        self.fire_cooldown = 0

        self.damage = 1

    def update(self, dt):
        # cooldown
        if self.fire_cooldown > 0:
            self.fire_cooldown -= dt

        # reload
        if self.reloading:
            self.reload_timer -= dt
            if self.reload_timer <= 0:
                self.finish_reload()

    def start_reload(self):
        if not self.reloading and self.ammo_in_mag < self.mag_size and self.reserve_ammo > 0:
            self.reloading = True
            self.reload_timer = self.reload_time

    def finish_reload(self):
        self.reloading = False
        needed = self.mag_size - self.ammo_in_mag
        to_load = min(needed, self.reserve_ammo)
        self.ammo_in_mag += to_load
        self.reserve_ammo -= to_load

    def can_fire(self):
        return (
            not self.reloading and
            self.ammo_in_mag > 0 and
            self.fire_cooldown <= 0
        )

    def fire(self, player):
        """Override in subclasses"""
        pass
