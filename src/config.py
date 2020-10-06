import pyglet

def init():
    pyglet.resource.path = ["../gfx"]
    pyglet.resource.reindex()