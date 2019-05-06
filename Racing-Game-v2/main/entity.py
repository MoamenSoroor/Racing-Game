import manager
import pygame

PLAYER_WIDTH = 32
PLAYER_HEIGHT = 64
PLAYER_CENTER = PLAYER_WIDTH/2 , PLAYER_HEIGHT/2

ENEMY_WIDTH = 32
ENEMY_HEIGHT = 64
ENEMY_CENTER = ENEMY_WIDTH/2 , ENEMY_HEIGHT/2


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UP_RIGHT = 4
UP_LEFT = 5
DOWN_RIGHT = 6
DOWN_LEFT = 7


class Entity(manager.Manager):
    def __init__(self, world, x, y, width, height, speed_x , speed_y, asset_name):
        super().__init__()
        self.world = world
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = UP
        self.base_speed_x = speed_x
        self.base_speed_y = speed_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_max = 80
        self.move_x= 0.0
        self.move_y = 0.0
        self.asset_name = asset_name
        self.asset = None
        self.camera_on = False

    def center(self):
        return (self.x + self.width)/2 , (self.y + self.height)/2

    def up_left(self):
        return self.x , self.y

    def up_right(self):
        return (self.x + self.width) , self.y

    def down_left(self):
        return self.x, (self.y + self.height)

    def down_right(self):
        return (self.x + self.width) , (self.y + self.height)

    #def check_collision(self,entity):


class Player(Entity):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, PLAYER_WIDTH, PLAYER_HEIGHT, 5,10, "car1.png")
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def load(self):
        self.asset = pygame.image.load(self.asset_name).convert()

    def control(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.right = True

        if keys[pygame.K_a]:
            self.left = True

        if keys[pygame.K_w]:
            self.up = True

        if keys[pygame.K_s]:
            self.down = True

    def tick(self):
        self.speed_x , self.speed_y = self.base_speed_x , self.base_speed_y
        resistance = self.world.tile_map.get_resistance(self.x, self.y)
        print("tile resistance:", resistance)
        print("player location: ", self.x, self.y)

        if self.up and not self.down and not self.right and not self.left:
            self.move_y = -(self.speed_y - self.speed_y * resistance)
            print("up",self.move_x, self.move_y)

        elif self.up and not self.down and self.right and not self.left:
            self.move_y = -(self.speed_y - self.speed_y * resistance)
            self.move_x = self.speed_x  - self.speed_x * resistance

        elif self.up and not self.down and not self.right and self.left:
            self.move_y = -(self.speed_y - self.speed_y * resistance)
            self.move_x = -(self.speed_x  - self.speed_x * resistance)

        elif not self.up and self.down and not self.right and not self.left:
            self.move_y = self.speed_y - self.speed_y * resistance

        elif not self.up and self.down and self.right and not self.left:
            self.move_y = self.speed_y - self.speed_y * resistance
            self.move_x = self.speed_x  - self.speed_x * resistance

        elif not self.up and self.down and not self.right and self.left:
            self.move_y = self.speed_y - self.speed_y * resistance
            self.move_x = -(self.speed_x  - self.speed_x * resistance)
        else:
            self.move_x = 0.0
            self.move_y = 0.0
            print("else", self.move_x, self.move_y)


        self.right = False
        self.left = False
        self.up = False
        self.down = False


    def render(self, win):
        self.x += self.move_x
        self.y += self.move_y
        win.blit(self.asset, (self.x, self.y))



class Enemy(Entity):

    def __init__(self, world, x, y):
        super().__init__(world, x, y, ENEMY_WIDTH, ENEMY_HEIGHT, 5, 10, "car2.png")

    def load(self):
        self.asset = pygame.image.load(self.asset_name).convert()

    def control(self, events):
        pass

    def tick(self):

        self.x -= self.world.player_camera.offset_x
        self.y -= self.world.player_camera.offset_y

    def render(self, win):
        #print("car2 : ", self.x // self.world.tile_width, self.y // self.world.tile_height)
        win.blit(self.asset, (self.x, self.y))
        #pygame.draw.rect(win, (255,255,255), (400, 400, self.width, self.height))


class EntityManager(manager.Manager):

    def __init__(self, world, player, enemy):
        super().__init__()
        self.world = world
        self.player = player
        self.enemy = enemy

    def load(self):
        self.player.load()
        self.enemy.load()

    def control(self,events):
        self.player.control(events)
        self.enemy.control(events)

    def tick(self):
        self.player.tick()
        self.enemy.tick()

    def render(self, win):
        self.player.render(win)
        self.enemy.render(win)


