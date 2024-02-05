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
        print(self.hand)

    def draw(self):
        pass

    def checkSelfDrawWin(self):
        pass

    def checkWin(self, tile):
        pass

    def checkChi(self, tile):
        pass

    def checkPong(self, tile):
        pass
    

