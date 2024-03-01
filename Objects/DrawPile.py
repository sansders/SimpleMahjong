import random

# Define a class named 'DrawPile'
class DrawPile:
    
    # Constructor method to initialize the object
    def __init__(self, tiles):
        self.tiles = tiles
        self.shuffle()

    def draw(self):
        return self.tiles.pop(0)
    
    def shuffle(self):
        random.shuffle(self.tiles)

    def putIntoDeadWall(self):
        boundForDeadWall = []
        for _ in range (10):
            boundForDeadWall.append(self.tiles.pop(0))
        return boundForDeadWall

