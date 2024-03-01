# Define a class named 'Tile'
class Tile:
    
    # Constructor method to initialize the object
    def __init__(self, suit, number, dragon, wind, name):

        # Initialize lists to store properties
        self.suit = [0, 0, 0, 0]
        self.number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.dragon = [0, 0, 0, 0]
        self.wind = [0, 0, 0, 0, 0]
        self.name = name

        self.suit[suit] = 1
        self.number[number] = 1
        self.dragon[dragon] = 1
        self.wind[wind] = 1

    def getTileSuit(self):
        for x in range(4):
            if self.suit[x] == 1:
                return x
            
    def getTileNumber(self):
        for x in range(10):
            if self.number[x] == 1:
                return x
            
    def getTileDragon(self):
        for x in range(4):
            if self.dragon[x] == 1:
                return x
            
    def getTileWind(self):
        for x in range(5):
            if self.wind[x] == 1:
                return x
            
    def getTileName(self):
        return self.name


