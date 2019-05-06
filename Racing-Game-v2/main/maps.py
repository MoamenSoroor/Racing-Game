
class Map:

    def __init__(self, world_dim, tile_dim, player_tile_loc, enemy_tile_loc, map_id):
        self.world_dim = self.world_width, self.world_height = world_dim
        self.tile_dim = self.tile_width, self.tile_height = tile_dim
        self.player_tile_loc = self.player_i , self.player_j = player_tile_loc
        self.enemy_tile_loc = self.enemy_i , self.enemy_j = enemy_tile_loc
        self.player_x = self.player_i * self.tile_width + self.tile_width / 2
        self.player_y = self.player_j * self.tile_height + self.tile_height / 2
        self.enemy_x = self.enemy_i * self.tile_width + self.tile_width / 2
        self.enemy_y = self.enemy_j * self.tile_height + self.tile_height / 2
        self.map_id = map_id

    def print_map(self):
        print("=" * 50)
        print("self.world_dim       :", self.world_dim )
        print("self.tile_dim        :", self.tile_dim )
        print("self.player_tile_loc :", self.player_tile_loc )
        print("self.enemy_tile_loc  :", self.enemy_tile_loc )
        print("self.player_x        :", self.player_x )
        print("self.player_y        :", self.player_y )
        print("self.enemy_x         :", self.enemy_x )
        print("self.enemy_y         :", self.enemy_y )
        print("=" * 50)

        for i in range(self.world_width):
            for j in range(self.world_height):
                print(self.map_id[i][j], end=" ")
            print("")
        print("=" * 50)


def get_map1():
    map_id = [
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w",
         "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
        ["w", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",
         "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "w"],
        ["w", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r",
         "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "w"],
        ["w", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r",
         "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "w"],
        ["w", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",
         "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "w"],
        ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w",
         "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w", "w"]]
    print("map id:", len(map_id), len(map_id[0]))
    return Map(len(map_id), len(map_id[0]), 256, 256, map_id)


def load_map(map_path, tile_dim):

    file = open(map_path, "rt")
    world_line = file.readline().strip().split(" ")
    print(world_line)
    world_dim = int(world_line[0]), int(world_line[1])

    player_line = file.readline().strip().split(" ")
    print(player_line)
    player_dim = int(player_line[0]), int(player_line[1])

    enemy_line = file.readline().strip().split(" ")
    print(enemy_line)
    enemy_dim = int(enemy_line[0]), int(enemy_line[1])

    lines = file.readlines()
    my_map_id = []
    for line in lines:
        t = line.strip().split(" ")
        my_map_id.append(t)

    print(my_map_id)
    print(len(my_map_id), len(my_map_id[0]))

    my_map_id2 = []
    for i in range(world_dim[0]):
        row = []
        for j in range(world_dim[1]):
            row.append(my_map_id[j][i])
        my_map_id2.append(row)


    my_map = Map(world_dim,tile_dim,player_dim,enemy_dim,my_map_id2)
    my_map.print_map()
    return my_map



