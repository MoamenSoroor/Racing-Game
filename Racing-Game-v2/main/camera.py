import manager
import math
class Camera():

    def __init__(self,world, entity):
        self.world = world
        self.entity = entity
        self.entity.camera_on = True
        self.offset_x = 0
        self.offset_y = 0

    def tick(self):
        self.offset_x = self.entity.x + self.entity.move_x - self.world.game_width /2 + self.entity.width/2
        self.offset_y = self.entity.y + self.entity.move_y - self.world.game_height / 2 + self.entity.height / 2

        self.entity.move_x -= self.offset_x
        self.entity.move_y -= self.offset_y









