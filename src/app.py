from config import init
from pathlib import Path
from entity import Entity
from layer import Layer
import pyglet
import os 
class App(pyglet.window.Window):

    def __init__(self):
        super(App, self).__init__(vsync = False)
        init()
        
        self.ground_layer = Layer('tilesets/tiles_packed.png', 23, 8)
        self.test_entity = Entity(0, 0, self.ground_layer.tiles[0])
        self.running = 1

    def on_key_press(symbol, modifiers):
        print(symbol)

    def on_draw(self):
        self.render

    def render(self):
        self.clear()
        self.ground_layer.render()
        self.flip()

    def on_close(self):
        self.running = 0

    def run(self):
        while self.running:
            self.render()
            event = self.dispatch_events() 
        
if __name__ == "__main__":
    app = App()
    app.run()