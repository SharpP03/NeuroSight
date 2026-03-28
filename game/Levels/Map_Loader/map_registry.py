from game.Levels.Objects.wall import Wall
from game.Levels.Objects.tree import Tree
from game.Levels.Objects.building import Building

# Mapping chars to obj classes
OBJECT_REGISTRY = {
    Wall.TILE_CHAR: Wall,
    Tree.TILE_CHAR: Tree,
    Building.TILE_CHAR: Building,
}
