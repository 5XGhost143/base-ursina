from ursina import *


def create_world():
    ground = Entity(
        model='plane',
        scale=(10, 1, 10),
        texture='grass',
        texture_scale=(10, 10),
        color=color.green,
        collider='box'
    )

    cube = Entity(
        model='cube',
        color=color.red,
        scale=(1, 1, 1),
        position=(2, 0.5, 2),
        collider='box'
    )

    return ground, cube
