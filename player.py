from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, position=(0, 1, 0)):
        super().__init__(position=position)
        self.collider = 'box'
        self.speed = 9
        self.jump_height = 2.5
        camera.fov = 120
