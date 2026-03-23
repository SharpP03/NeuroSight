class SceneManager:
    def __init__(self, start_scene):
        self.current_scene = start_scene

    def run(self):
        while self.current_scene is not None:
            next_scene = self.current_scene.run() # run the scene

            if next_scene == "GAME":
                from game.Levels.level1 import Level1
                self.current_scene = Level1()


            elif next_scene == "MENU":
                from game.main_menu import MainMenu
                self.current_scene = MainMenu()

            else:
                break
