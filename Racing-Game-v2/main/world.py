import manager
import tile
import pygame
import entity
import camera


class WorldScene(manager.Manager):

    def __init__(self, game, scene_name, my_map):
        super().__init__()
        self.game = game
        self.scene_name = scene_name
        self.my_map = my_map
        self.game_dim = self.game_width, self.game_height = self.game.win_dim
        self.world_dim = self.world_width, self.world_height = my_map.world_dim
        self.tile_dim = self.tile_width, self.tile_height = my_map.tile_dim
        self.map_id = my_map.map_id
        self.tile_map = tile.TileMap(self)
        self.tile_manager = tile.TileManager(self)

        self.player = entity.Player(self, my_map.player_x, my_map.player_y)
        self.enemy = entity.Enemy(self, my_map.enemy_x, my_map.enemy_y)
        self.entity_manager = entity.EntityManager(self, self.player, self.enemy)
        self.player_camera = camera.Camera(self, self.player)


    def load(self):
        self.tile_map.load_map()
        self.entity_manager.load()
        self.tile_manager.load()
        print("world height:", self.world_height)
        print("world width:", self.world_width)
        print("tile width:", self.tile_width)
        print("tile height:", self.tile_height)

    def control(self, events):
        self.entity_manager.control(events)
        self.tile_manager.control(events)

    def tick(self):
        self.entity_manager.tick()
        self.player_camera.tick()
        self.tile_manager.tick()

    def render(self, win):
        win.fill((0, 0, 0))
        self.tile_manager.render(win)
        self.entity_manager.render(win)
        pygame.display.update()

    def recv(self):
        while self.game.is_run():
            data = self.comm.recv()

            if data == "up":
                self.enemy.up = True

            elif data == "down":
                self.enemy.down = True

            elif data == "left":
                self.enemy.left = True

            elif data == "right":
                self.enemy.right = True

            elif data == "up-right":
                self.enemy.up = True
                self.enemy.right = True

            elif data == "up-left":
                self.enemy.up = True
                self.enemy.left = True

            elif data == "down-right":
                self.enemy.down = True
                self.enemy.right = True

            elif data == "down-left":
                self.enemy.down = True
                self.enemy.left = True



