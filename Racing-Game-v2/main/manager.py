import pygame
import math


class Manager:

    def __init__(self):
        pass

    def load(self):
        print("Warning: load method is not implemented by subclass")

    def control(self,events):
        print("Warning: control method is not implemented by subclass")

    def tick(self):
        print("Warning: tick method is not implemented by subclass")

    def render(self, win):
        print("Warning: render method is not implemented by subclass")


class SceneSelector:

    def __init__(self, scene_lib=None):
        if scene_lib is None:
            self.scene_lib = {}

        self.selected_scene = None

    def add_scene(self, scene):
        self.scene_lib[scene.scene_name] = scene

    def select(self, scene_name):
        self.selected_scene = self.scene_lib[scene_name]
        return self.selected_scene

    def get_scene(self):
        return self.selected_scene
