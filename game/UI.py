import pygame


class UI:
    def __init__(self, screen):
        # Drawing settings
        self.screen = screen
        self.font = pygame.font.SysFont("none", 32)
        self.WIDTH, self.HEIGHT = screen.get_size()

    def drawPlayerHp(self, hp=None):
        if hp is not None:
            text = self.font.render("Health: " + str(hp), True, (255, 255, 255))
            self.screen.blit(text, (10, 20))

    def drawFrags(self, frags=None):
        if frags is not None:
            text = self.font.render("Frags: " + str(frags), True, (255, 255, 255))
            self.txt_width = text.get_width()
            self.screen.blit(text, (self.WIDTH - self.txt_width - 10, 20))

    def debug(self, bullets_count):
        text = self.font.render(f"Bullets: {bullets_count}", True, pygame.Color("#FF00AA"))
        self.screen.blit(text, (10, 60))