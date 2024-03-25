# Define a class named 'DiscardPile'
class DiscardPile:
    
    # Constructor method to initialize the object
    def __init__(self):
        self.tiles = []

    def discardTile(self, tile):
        self.tiles.append(tile)
        return tile

    def printDiscardPile(self):
        print("\nDiscard pile: ", end="")
        for tile in self.tiles:
                print(tile.name, end=" ")
    
    def take(self):
        self.tiles.pop()
