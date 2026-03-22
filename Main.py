import pygame
from game.scene_manager import SceneManager
from game.main_menu import MainMenu

if __name__ == "__main__":
    pygame.init()

    manager = SceneManager(MainMenu())
    manager.run()

    pygame.quit()
