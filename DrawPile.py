# Define a class named 'DrawPile'
class DrawPile:
    
    # Constructor method to initialize the object
    def __init__(self, tiles):
        self.tiles = tiles

    def draw(self):
        return self.tiles.pop(0)

