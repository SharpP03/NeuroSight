import pygame
from game.game2 import Game

class MainMenu:
    def __init__(self):
        pygame.init()

        # main menu window parameters
        self.WIDTH, self.HEIGHT = 800, 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("NeuroSight - Menu")

        # Caption font
        self.big_font = pygame.font.SysFont("none", 72)
        # options font
        self.small_font = pygame.font.SysFont("none", 28)

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = Game()
                    game.run()

                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self):
        self.screen.fill((10, 10, 10))

        title = self.big_font.render("NEUROSIGHT", True, (200, 200, 255))
        self.screen.blit(title, (self.WIDTH//2 - title.get_width()//2, 200))

        start = self.small_font.render("Press ENTER to start", True, (255, 255, 255))
        self.screen.blit(start, (self.WIDTH//2 - start.get_width()//2, 400))

        quit_text = self.small_font.render("Press ESC to quit", True, (180, 180, 180))
        self.screen.blit(quit_text, (self.WIDTH//2 - quit_text.get_width()//2, 450))
