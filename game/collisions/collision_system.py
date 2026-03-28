class CollisionSystem:
    def __init__(self, player, enemies, map_objects, bullet_manager):
        self.player = player
        self.enemies = enemies
        self.map_objects = map_objects
        self.bullet_manager = bullet_manager

    def update(self):
        self.player_vs_enemies()
        self.player_vs_map()
        self.bullets_vs_enemies()
