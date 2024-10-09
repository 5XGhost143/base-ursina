from ursina import *

from WManage import Window
from player import Player
from world import create_world

app = Ursina()

WManage = Window()

ground, cube = create_world()

player = Player()

app.run()
