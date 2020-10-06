import pyglet

class Entity():

    def __init__(self, x: int, y: int, tile):
        self.x = x
        self.y = y
        self.tile = tile

    def render(self):
        self.tile.blit(self.x, self.y)