class BulletManager:
    def __init__(self, despawn_distance):
        self.bullets = []
        self.despawn_distance = despawn_distance

    def add(self, bullet_or_list):
        if isinstance(bullet_or_list, list):
            self.bullets.extend(bullet_or_list)
        else:
            self.bullets.append(bullet_or_list)

    def update(self, player):
        px, py = player.rect.center

        for bullet in self.bullets[:]:
            bullet.update()

            dx = bullet.rect.centerx - px
            dy = bullet.rect.centery - py

            if dx*dx + dy*dy > self.despawn_distance**2:
                self.bullets.remove(bullet)

    def draw(self, screen, camera):
        for bullet in self.bullets:
            bullet.draw(screen, camera)
