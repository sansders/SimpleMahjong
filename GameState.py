# Define a class named 'GameState'
class GameState:
    
    # Constructor method to initialize the object
    def __init__(self):

        # Order in which players take their turns.
        # Each index represents the order, while each value represents the player's id.
        self.order = []

        # Tracker to track which player's turn is it
        self.currentPlayer = 0

        # Number of wins per player.
        # Each index corresponds to a player's id.
        self.wins = []

        # Counter for number of turns in the current game
        self.currentTurn = 0

        # List to store the result of dice rolls.
        # Only used once, at the very start of the Mahjong.
        self.diceRolls = []

        # List to store all 4 players in Mahjong
        self.players = []

        # Sets the draw pile
        self.drawPile = None

        # Sets the discard pile
        self.discardPile = None

    # Check number of wins each player has
    def checkWins(self):
        pass

    # Check which turn it is now
    def checkCurrentTurn(self):
        pass

    # Check which player's turn is it
    def checkCurrentPlayer(self):
        pass

    # Used at the start of the game to draw tiles for each player
    def startGameDraw(self):
        pass

    # Used at the start of Mahjong to determine who goes first
    def rollDice(self):
        pass

    # Used to check the board for all the opened tiles, and to which player they belong to
    def checkOpenedTiles(self):
        pass

    # Used to check which tiles are in the discard pile
    def checkDiscardPile(self):
        return self.discardPile.checkDiscardPile()
    
    # Used to check the number of tiles left in the draw pile
    def checkDrawPile(self):
        return self.drawPile.checkNumberOfTilesLeft()

    # Sets the order of play, draw pile, and each players' hands
    def initialiseRound(self):
        pass
