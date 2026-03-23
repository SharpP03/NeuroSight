import pygame
from game.player import Player
from game.enemy import Enemy
from game.camera import Camera

class Level1:
    def __init__(self):
        # okno
        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Level 1")

        # clock
        self.clock = pygame.time.Clock()

        # kamera
        self.camera = Camera(self.WIDTH, self.HEIGHT)

        # gracz
        self.player = Player(400, 400)

        # przeciwnicy
        self.enemies = [
            Enemy(800, 800),
            Enemy(1200, 600)
        ]

        self.running = True

    def run(self):
        while self.running:
            dt = self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return "MENU"

            # update
            keys = pygame.key.get_pressed()
            self.player.update(keys)

            for enemy in self.enemies:
                enemy.update(self.player)

            self.camera.update(self.player)

            # draw
            self.screen.fill((20, 20, 20))

            for enemy in self.enemies:
                enemy.draw(self.screen, self.camera)

            self.player.draw(self.screen, self.camera)

            pygame.display.flip()

        return "MENU"
