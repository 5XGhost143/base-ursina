from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Window(FirstPersonController):
    def __init__(self):
        super().__init__()
        window.title = "Ursina"
        window.borderless = False
        window.resizable = False
        window.size = (1280, 720)
        window.position = (100, 100)
        window.exit_button.visible = False