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
        pass

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

    def discard(self, userInput):
        self.discardPile.discardTile(self.players[self.currentPlayer-1].discard(userInput))

    def checkPong(self, playerId, discardedTile):
        
        player = self.players[playerId-1]
        
        if player.checkPong(discardedTile) == True:
            self.interrupted = 1
            self.discardPile.take()
        
            while self.order[self.currentTurn % 4] != playerId:
                self.currentTurn += 1
            
    def checkMelds(self, playerId):

        player = self.players[playerId-1]
        player.sort_hand()

        tempHand1 = player.hand
        tempHand2 = player.hand

        playerTilesDict1 = self.list_to_dict(player.hand)
        playerTilesDict2 = self.list_to_dict(player.hand)

        maxMelds = 0
        pairs = 0
        melds1 = 0
        pairs1 = 0
        melds2 = 0
        pairs2 = 0

        # Part 1: Check sequences, then triplets, then pairs
        # Part 1a: Check sequences
        for tile in range(0, len(tempHand1)-2):

            if playerTilesDict1[tempHand1[tile]] == 0:
                continue

            tilePlusOne = tempHand1[tile].getTileNumber() + 1
            tilePlusTwo = tempHand1[tile].getTileNumber() + 2
            tileSuit = tempHand1[tile].getTileSuit()

            passOne = 0
            firstTile = tempHand1[tile]
            secondTile = "" 
            thirdTile = ""

            for playerTileDictKeys in playerTilesDict1:
                
                if passOne == 0:
                    if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                        and playerTilesDict1[playerTileDictKeys] != 0:
                        passOne = 1
                        secondTile = playerTileDictKeys
                
                elif passOne == 1:
                    if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                        and playerTilesDict1[playerTileDictKeys] != 0:
                        thirdTile = playerTileDictKeys
                        playerTilesDict1[firstTile] -= 1
                        playerTilesDict1[secondTile] -= 1
                        playerTilesDict1[thirdTile] -= 1

                        melds1 += 1
                        passOne = 0

                        break

        # Part 1b: Check triplets
        for tile in range(0, len(tempHand1)-2):
            
            tileWind = tempHand1[tile].getTileWind()
            tileDragon = tempHand1[tile].getTileDragon()
            tileSuit = tempHand1[tile].getTileSuit()
            tileNumber = tempHand1[tile].getTileNumber()

            if playerTilesDict1[tempHand1[tile]] == 0:
                continue

            if tempHand1[tile+1].getTileSuit() == tileSuit and tempHand1[tile+1].getTileNumber() == tileNumber \
                and tempHand1[tile+1].getTileDragon() == tileDragon and tempHand1[tile+1].getTileWind() == tileWind:
                if tempHand1[tile+2].getTileSuit() == tileSuit and tempHand1[tile+2].getTileNumber() == tileNumber \
                    and tempHand1[tile+2].getTileDragon() == tileDragon and tempHand1[tile+2].getTileWind() == tileWind:
                    playerTilesDict1[tempHand1[tile]] -= 1
                    playerTilesDict1[tempHand1[tile+1]] -= 1
                    playerTilesDict1[tempHand1[tile+2]] -= 1
                    melds1 += 1
                    tile += 3         

        # Part 1c: Check pairs
        for tile in range(0, len(tempHand1)-1):

            tileWind = tempHand1[tile].getTileWind()
            tileDragon = tempHand1[tile].getTileDragon()
            tileSuit = tempHand1[tile].getTileSuit()
            tileNumber = tempHand1[tile].getTileNumber()

            if playerTilesDict1[tempHand1[tile]] == 0:
                continue

            if tempHand1[tile+1].getTileSuit() == tileSuit and tempHand1[tile+1].getTileNumber() == tileNumber \
                and tempHand1[tile+1].getTileDragon() == tileDragon and tempHand1[tile+1].getTileWind() == tileWind:
                    playerTilesDict1[tempHand1[tile]] -= 1
                    playerTilesDict1[tempHand1[tile+1]] -= 1
                    pairs1 += 1
                    tile += 2         
        
        # print("\nMelds/Pairs1:%d,%d" % (melds1, pairs1))
            
        # Part 2: Check triplets, then sequences, then pairs
        # Part 2a: Check triplets
        for tile in range(0, len(tempHand2)-2):
            
            tileWind = tempHand2[tile].getTileWind()
            tileDragon = tempHand2[tile].getTileDragon()
            tileSuit = tempHand2[tile].getTileSuit()
            tileNumber = tempHand2[tile].getTileNumber()

            if playerTilesDict2[tempHand2[tile]] == 0:
                continue

            if tempHand2[tile+1].getTileSuit() == tileSuit and tempHand2[tile+1].getTileNumber() == tileNumber \
                and tempHand2[tile+1].getTileDragon() == tileDragon and tempHand2[tile+1].getTileWind() == tileWind:
                if tempHand2[tile+2].getTileSuit() == tileSuit and tempHand2[tile+2].getTileNumber() == tileNumber \
                    and tempHand2[tile+2].getTileDragon() == tileDragon and tempHand2[tile+2].getTileWind() == tileWind:

                    playerTilesDict2[tempHand2[tile]] -= 1
                    playerTilesDict2[tempHand2[tile+1]] -= 1
                    playerTilesDict2[tempHand2[tile+2]] -= 1

                    melds2 += 1
                    tile += 3      

        # Part 2b: Check sequences
        for tile in range(0, len(tempHand2)-2):

            if playerTilesDict2[tempHand2[tile]] == 0:
                continue

            tilePlusOne = tempHand2[tile].getTileNumber() + 1
            tilePlusTwo = tempHand2[tile].getTileNumber() + 2
            tileSuit = tempHand2[tile].getTileSuit()

            passOne = 0
            firstTile = tempHand2[tile]
            secondTile = "" 
            thirdTile = ""

            for playerTileDictKeys in playerTilesDict2:
                
                if passOne == 0:
                    if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                        and playerTilesDict2[playerTileDictKeys] != 0:
                        passOne = 1
                        secondTile = playerTileDictKeys
                
                elif passOne == 1:
                    if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                        and playerTilesDict2[playerTileDictKeys] != 0:
                        thirdTile = playerTileDictKeys
                        playerTilesDict2[firstTile] -= 1
                        playerTilesDict2[secondTile] -= 1
                        playerTilesDict2[thirdTile] -= 1

                        melds2 += 1
                        passOne = 0

                        break

        # Part 2c: Check pairs
        for tile in range(0, len(tempHand2)-1):

            tileWind = tempHand2[tile].getTileWind()
            tileDragon = tempHand2[tile].getTileDragon()
            tileSuit = tempHand2[tile].getTileSuit()
            tileNumber = tempHand2[tile].getTileNumber()

            if playerTilesDict2[tempHand2[tile]] == 0:
                continue

            if tempHand2[tile+1].getTileSuit() == tileSuit and tempHand2[tile+1].getTileNumber() == tileNumber \
                and tempHand2[tile+1].getTileDragon() == tileDragon and tempHand2[tile+1].getTileWind() == tileWind:
                    playerTilesDict2[tempHand2[tile]] -= 1
                    playerTilesDict2[tempHand2[tile+1]] -= 1
                    pairs2 += 1
                    tile += 2         
        
        # print("Melds/Pairs2:%d,%d" % (melds2, pairs2))

        # Get best meld count based on order of obtaining the melds
        if melds1 > melds2:
            maxMelds = melds1
            pairs = pairs1
        elif melds2 > melds1:
            maxMelds = melds2
            pairs = pairs2
        else:
            if pairs1 > pairs2:
                maxMelds = melds1
                pairs = pairs1
            elif pairs2 > pairs1:
                maxMelds = melds2
                pairs = pairs2
            else:
                maxMelds = melds1
                pairs = pairs1
        
        print("\nMelds/Pairs:%d,%d" % (maxMelds, pairs))

        return maxMelds, pairs

    def printOpenedTiles(self):
        playerId = 1
        for player in self.players:
            if player.opened != []:
                print("\nPlayer %d's opened tiles: " % playerId, end="")
                for tile in player.opened:
                    print(tile.name, end=" ")
            playerId += 1

    def list_to_dict(self, lst):
        # Initialize an empty dictionary
        result_dict = {}
        
        # Iterate over the list
        for key in lst:
            # Increment the value if the key is already present, otherwise set it to 1
            result_dict[key] = result_dict.get(key, 0) + 1
        
        return result_dict