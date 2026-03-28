from game.Levels.Map_Loader.map_registry import OBJECT_REGISTRY

class MapLoader:
    def __init__(self, tilemap, tile_size):
        self.tilemap = tilemap
        self.tile_size = tile_size

    def load(self):
        objects = []

        for y, row in enumerate(self.tilemap):
            for x, char in enumerate(row):
                if char in OBJECT_REGISTRY:
                    cls = OBJECT_REGISTRY[char]
                    world_x = x * self.tile_size
                    world_y = y * self.tile_size
                    objects.append(cls(world_x, world_y, self.tile_size))

        return objects
