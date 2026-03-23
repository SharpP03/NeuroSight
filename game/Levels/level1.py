from .base_level import BaseLevel
from game.enemy import Enemy

class Level1(BaseLevel):
    def __init__(self, game):
        super().__init__(game)

        # player starting pos
        self.player.rect.x = 400
        self.player.rect.y = 400

        # sample enemy
        self.enemies.clear()
        self.enemies.append(Enemy(800, 800))
        self.enemies.append(Enemy(1200, 600))

        self.next_level = None

    def run(self):
        clock = self.game.clock

        running = True
        while running:
            dt = clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "MENU"

            self.update(dt)
            self.draw(self.game.screen)
            pygame.display.flip()
