import pyglet

class Layer():

    def __init__(self, image_path: str, layer_width: int, layer_height: int):
        self.image = pyglet.resource.image(image_path)
        self.layer_width = layer_width
        self.layer_height = layer_height
        self.tiles = self.extract_tiles()

    def extract_tiles(self):
        tiles = []
        for tile_x in range(self.layer_width):
            for tile_y in range(self.layer_height):
                tile_data = {
                    "image": self.image.get_region(x=tile_x, y=tile_y, width=16, height=16),
                    "meta": {
                        "x": tile_x,
                        "y": tile_y
                    }
                }
                tiles.append(tile_data)
        return tiles

    def render(self):
        x = 0
        for tile in self.tiles:
            tile["image"].blit(x, 0)
            x + 16