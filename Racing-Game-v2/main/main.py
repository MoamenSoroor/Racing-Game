import pygame
import math
import manager
import world
import maps


def main():
    game = Game()
    game.start()


class Game:

    def __init__(self, win_width=800, win_height=600, game_name="Race-Game"):
        self.win_dim = self.win_width, self.win_height = win_width, win_height
        self.game_name = game_name
        self.window = None
        self.my_scene_selector = None
        self.current_scene = None
        self.run = False
        self.play = False

    def start(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.win_dim)
        pygame.display.set_caption(self.game_name)
        clock = pygame.time.Clock()

        self.my_scene_selector = manager.SceneSelector()

        my_map = maps.get_map1()

        self.current_scene = world.WorldScene(self, "world-scene", my_map)
        self.my_scene_selector.add_scene(self.current_scene)
        self.my_scene_selector.select("world-scene")

        self.current_scene.load()



        self.run = True
        self.play = True
        while self.run:
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.run = False

            self.current_scene.control(events)
            if self.play:
                self.current_scene.tick()
                self.current_scene.render(self.window)

        pygame.quit()

    def pause(self):
        self.play = False

    def play(self):
        self.play = True

    def quite(self):
        self.play = False
        self.run = False


# main call
if __name__ == "__main__":
    main()
