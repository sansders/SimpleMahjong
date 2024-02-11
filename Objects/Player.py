# Define a class named 'Player'
class Player:
    
    # Constructor method to initialize the object
    def __init__(self, playerId, hand, opened):
        self.playerId = playerId
        self.hand = hand
        self.opened = opened
        self.closed = []

    def chi(self, tile1, tile2, tile3):
        pass

    def pong(self, tile1, tile2, tile3):
        pass

    def win(self, tiles):
        pass

    def viewHand(self):
        self.sort_hand()
        print("Player %d tiles: " % self.playerId, end="")
        for tile in self.hand:
            print(tile.name, end=" ")
        print("")

    def draw(self, drawPile):
        self.hand.append(drawPile.draw())

    def checkSelfDrawWin(self):
        pass

    def checkWin(self, tile):
        pass

    def checkChi(self, tile):
        pass

    def checkPong(self, tile):
        pass

    def sort_hand(self):
        # Define the custom order of tiles
        tile_order = [
            "Red", "Green", "White",
            "East", "South", "West", "North",
            "1Dot", "2Dot", "3Dot", "4Dot", "5Dot", "6Dot", "7Dot", "8Dot", "9Dot",
            "1Bam", "2Bam", "3Bam", "4Bam", "5Bam", "6Bam", "7Bam", "8Bam", "9Bam",
            "1Cha", "2Cha", "3Cha", "4Cha", "5Cha", "6Cha", "7Cha", "8Cha", "9Cha"
        ]

        # Sort the hand based on the custom order
        self.hand.sort(key=lambda tile: tile_order.index(tile.getTileName()))
    

