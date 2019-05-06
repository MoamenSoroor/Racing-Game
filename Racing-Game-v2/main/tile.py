import manager
import pygame
import math


TILE_GRASS = 0, "GRASS"
TILE_ROAD = 1, "ROAD"
TILE_WALL = 2, "WALL"


class Tile(manager.Manager):

    def __init__(self, x, y, width, height, tile_type, color, resistance , solid):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = tile_type
        self.color = color
        self.resistance = resistance
        self.is_solid = solid


class Grass(Tile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, TILE_GRASS, (81, 214, 44), 0.3, False)

    def load(self):
        pass

    def control(self, events):
        pass

    def tick(self):
        pass

    def render(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        #pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)


class Road(Tile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, TILE_ROAD, (86, 85, 83), 0.0, False)

    def load(self):
        pass

    def control(self, events):
        pass

    def tick(self):
        pass

    def render(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)


class Wall(Tile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, TILE_WALL, (158, 90, 18), 0.99, True)

    def load(self):
        pass

    def control(self, events):
        pass

    def tick(self):
        pass

    def render(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)


class TileMap:

    def __init__(self, world):
        self.world = world
        self.world_map = []
        self.zero_x, self.zero_y = 0,0

    def load_map(self):
        x, y = 0, 0
        for i in range(self.world.world_width):
            self.world_map.append([])
            for j in range(self.world.world_height):
                x, y = i * self.world.tile_width, j * self.world.tile_height
                if self.world.map_id[i][j] == "w":
                    self.world_map[i].append(Wall(x, y, self.world.tile_width, self.world.tile_height))
                    print("map w - ", i, j, x, y, self.world_map[i][j])

                elif self.world.map_id[i][j] == "g":
                    self.world_map[i].append(Grass(x, y, self.world.tile_width, self.world.tile_height))
                    print("map g - ", i, j, x, y, self.world_map[i][j])

                elif self.world.map_id[i][j] == "r":
                    self.world_map[i].append(Road(x, y, self.world.tile_width, self.world.tile_height))
                    print("map r - ", i, j, x, y, self.world_map[i][j])

                else:
                    raise Exception()
            print("map === ", self.world_map)
        print("map == ", self.world_map)

    def get_resistance(self, x, y):
        print(self.get_tile(x,y), self.get_tile_type(x,y))
        return self.get_tile(x, y).resistance

    def get_tile_type(self, x, y):
        return self.get_tile(x, y).type

    def get_tile(self, x, y):
        tile_x = x // self.world.tile_width
        tile_y = y // self.world.tile_height
        return self.world_map[int(tile_x + 1)][int(tile_y + 1)]

    def get_location(self, x, y):
        tile = self.get_tile(x, y)
        return tile.x, tile.y

    def get_location_by_index(self,i, j):
        return self.world_map[i].x, self.world_map[j].y


class TileManager(manager.Manager):
    def __init__(self, world):
        super().__init__()
        self.world = world

    def load(self):
        for tile_row in self.world.tile_map.world_map:
            for tile in tile_row:
                tile.load()

    def control(self, events):
        pass

    def tick(self):
        for tile_row in self.world.tile_map.world_map:
            for tile in tile_row:
                tile.tick()
                tile.x -= self.world.player_camera.offset_x
                tile.y -= self.world.player_camera.offset_y


    def render(self, win):
        for tile_row in self.world.tile_map.world_map:
            for tile in tile_row:
                tile.render(win)


