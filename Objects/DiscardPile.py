# Define a class named 'DiscardPile'
class DiscardPile:
    
    # Constructor method to initialize the object
    def __init__(self):
        self.tiles = []

    def discardTile(self, tile):
        self.tiles.append(tile)

    def checkDiscardPile(self):
        discardedTileNames = []
        for tile in self.tiles:
            discardedTileNames.append(tile.getTileName())
        return discardedTileNames

