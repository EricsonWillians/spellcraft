from config import init

from pathlib import Path
import pyglet
import os 

class App(pyglet.window.Window):

    def __init__(self):
        super(App, self).__init__(vsync = False)
        init()
        self.image = pyglet.resource.image('tilesets/tiles_packed.png')
        self.running = 1

    def on_key_press(symbol, modifiers):
        print(symbol)

    def on_draw(self):
        self.render

    def render(self):
        self.clear()
        self.image.blit(0, 0)
        self.flip()

    def on_close(self):
        self.running = 0

    def run(self):
        while self.running:
            self.render()
            event = self.dispatch_events() # <-- This is the event queue
        
if __name__ == "__main__":
    app = App()
    app.run()