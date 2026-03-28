class CollisionSystem:
    def __init__(self, player, enemy_manager, map_objects, bullet_manager):
        self.player = player
        self.enemy_manager = enemy_manager
        self.map_objects = map_objects
        self.bullet_manager = bullet_manager

    def update(self):
        self.player_vs_map()
        self.player_vs_enemies()
        self.bullets_vs_enemies()

    def player_vs_map(self):
        for obj in self.map_objects:
            if self.player.rect.colliderect(obj.rect):
                self.player.resolve_collision(obj.rect)

    def player_vs_enemies(self):
        for enemy in self.enemy_manager.enemies[:]:
            if self.player.rect.colliderect(enemy.rect):
                self.player.health -= 1
                self.enemy_manager.points += 1
                self.enemy_manager.enemies.remove(enemy)

    def bullets_vs_enemies(self):
        for bullet in self.bullet_manager.bullets[:]:
            for enemy in self.enemy_manager.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self.bullet_manager.bullets.remove(bullet)
                    self.enemy_manager.enemies.remove(enemy)
                    break
