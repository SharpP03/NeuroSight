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

    def drawPoints(self, points=None):
        if points is not None:
            text = self.font.render("Points: " + str(points), True, (255, 255, 255))
            self.txt_width = text.get_width()
            self.screen.blit(text, (self.WIDTH - self.txt_width - 10, 20))

    def debug(self, bullets_count):
        text = self.font.render(f"Bullets: {bullets_count}", True, pygame.Color("#FF00AA"))
        self.screen.blit(text, (10, 60))

    def drawAmmo(self, player):
        text = self.font.render(f"Ammo: {player.ammo_in_mag}/{player.reserve_ammo}", True, (255,240,103))
        self.screen.blit(text, (10, 100))
