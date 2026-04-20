class CollisionSystem:
    def __init__(self, player, enemy_manager, map_objects, bullet_manager):
        self.player = player
        self.enemy_manager = enemy_manager
        self.map_objects = map_objects
        self.bullet_manager = bullet_manager
        self._bullets_to_remove = set()

    def update(self):
        self._bullets_to_remove.clear()

        self.player_vs_map()
        self.player_vs_enemies()
        self.bullets_vs_enemies()
        self.bullets_vs_map()

        self._flush_bullet_removals()

    def _queue_bullet_removal(self, bullet):
        self._bullets_to_remove.add(bullet)

    def _flush_bullet_removals(self):
        for bullet in self._bullets_to_remove:
            if bullet in self.bullet_manager.bullets:
                self.bullet_manager.bullets.remove(bullet)

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
            if bullet in self._bullets_to_remove:
                continue

            for enemy in self.enemy_manager.enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    self._queue_bullet_removal(bullet)
                    self.enemy_manager.enemies.remove(enemy)
                    break

    def bullets_vs_map(self):
        for bullet in self.bullet_manager.bullets[:]:
            if bullet in self._bullets_to_remove:
                continue

            for map_object in self.map_objects:
                if map_object.rect.colliderect(bullet.rect):
                    self._queue_bullet_removal(bullet)
                    break