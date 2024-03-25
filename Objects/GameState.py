from random import randint

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

        # Sets the dead wall
        self.deadWall = None

        # Sets the discard pile
        self.discardPile = None

        # Default value is 0, it is set to 1 only if chi or pong is called
        self.interrupted = 0

    # Used at the start of Mahjong to determine who goes first
    def rollDice(self):
        while (not self.diceRolls or len(list(set(self.diceRolls))) < 4):
            self.diceRolls = []
            for _ in range(4):
                self.diceRolls.append(randint(3, 18))

    # Used at the start of Mahjong and Round to determine who goes in what order
    def setOrderFirstRound(self):
        sortedDiceRolls = sorted(self.diceRolls)

        firstPlayer = sortedDiceRolls[0]
        firstPlayerId = self.diceRolls.index(firstPlayer)

        secondPlayer = sortedDiceRolls[1]
        secondPlayerId = self.diceRolls.index(secondPlayer)

        thirdPlayer = sortedDiceRolls[2]
        thirdPlayerId = self.diceRolls.index(thirdPlayer)

        fourthPlayer = sortedDiceRolls[3]
        fourthPlayerId = self.diceRolls.index(fourthPlayer)

        self.order.append(firstPlayerId+1)
        self.order.append(secondPlayerId+1)
        self.order.append(thirdPlayerId+1)
        self.order.append(fourthPlayerId+1)

        print("Order of player ID:", self.order)

    # Used at the start of subsequent rounds to change the player order 
    def setOrderSubsequentRounds(self):
        self.order.append(self.order.pop(0))
        print("Order of player ID:", self.order)

    # Check number of wins each player has
    def checkWins(self):
        pass

    # Check number of wins player has
    def checkWinPlayer(self, playerId):
        pass

    # Check which turn it is now
    def checkCurrentTurn(self):
        return self.currentTurn

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

    def nextRound(self):
        self.currentTurn = 0
        self.setOrderSubsequentRounds()

    def discard(self, userInput):
        return self.discardPile.discardTile(self.players[self.currentPlayer-1].discard(userInput))

    def checkPong(self, playerId, discardedTile):
        
        player = self.players[playerId-1]
        
        if player.checkPong(discardedTile) == True:
            self.interrupted = 1
            self.discardPile.take()
        
            while self.order[self.currentTurn % 4] != playerId:
                self.currentTurn += 1
            
    def printOpenedTiles(self):
        playerId = 1
        for player in self.players:
            if player.opened != []:
                print("\nPlayer %d's opened tiles: " % playerId, end="")
                for tile in player.opened:
                    print(tile.name, end=" ")
            playerId += 1

    def tsumo(self):
        melds, pairs = self.players[self.currentPlayer-1].checkMelds(0)
        isWin = self.players[self.currentPlayer-1].checkSelfDrawnWin(melds, pairs)
        
        if isWin:
            print("Player %d wins!" % self.players[self.currentPlayer-1].playerId)
            self.players[self.currentPlayer-1].viewHand()
            self.players[self.currentPlayer-1].wins += 1
            print("")
            return True
        
        return False

    def checkIfWin(self, discardedTile):

        player1 = self.players[self.order[(self.currentTurn + 1) % 4] - 1]
        player2 = self.players[self.order[(self.currentTurn + 2) % 4] - 1]
        player3 = self.players[self.order[(self.currentTurn + 3) % 4] - 1]

        # Save old instances of hand
        savedPlayer1Hand = player1.hand.copy()
        savedPlayer2Hand = player2.hand.copy()
        savedPlayer3Hand = player3.hand.copy()

        # Temporarily append the discarded tile to each players' hands
        player1.hand.append(discardedTile)
        player2.hand.append(discardedTile)
        player3.hand.append(discardedTile)

        player1.sort_hand()
        player2.sort_hand()
        player3.sort_hand()

        melds1, pair1 = player1.checkMelds(0)
        if melds1 == 4 and pair1 == 1:
            print("Player %d wins!" % player1.playerId)
            player1.wins += 1

            player1.viewHand()

            player1.hand = savedPlayer1Hand
            player2.hand = savedPlayer2Hand
            player3.hand = savedPlayer3Hand
            
            print("")

            return player1

        melds2, pair2 = player2.checkMelds(0)
        if melds2 == 4 and pair2 == 1:
            print("Player %d wins!" % player2.playerId)
            player2.wins += 1

            player2.viewHand()

            player1.hand = savedPlayer1Hand
            player2.hand = savedPlayer2Hand
            player3.hand = savedPlayer3Hand

            print("")

            return player2

        melds3, pair3 = player3.checkMelds(0)
        if melds3 == 4 and pair3 == 1:
            print("Player %d wins!" % player3.playerId)
            player3.wins += 1

            player3.viewHand()

            player1.hand = savedPlayer1Hand
            player2.hand = savedPlayer2Hand
            player3.hand = savedPlayer3Hand

            print("")

            return player3

        # Put back the old hands
        player1.hand = savedPlayer1Hand
        player2.hand = savedPlayer2Hand
        player3.hand = savedPlayer3Hand

        return False
