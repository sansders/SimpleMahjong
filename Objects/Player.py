from collections import Counter

# Define a class named 'Player'
class Player:
    
    # Constructor method to initialize the object
    def __init__(self, playerId, hand):
        self.playerId = playerId
        self.hand = hand
        self.wins = 0

    def discard(self, tileIndex):
        return self.hand.pop(tileIndex)

    def chi(self, tile1, tile2, tile3):
        pass

    def pong(self, discardedTile):
        pongedTiles = [discardedTile]

        for index in range(len(self.hand) - 1):
            if self.hand[index].name == discardedTile.name:
                pongedTiles.append(self.hand.pop(index))
                pongedTiles.append(self.hand.pop(index))
                break

        for tile in pongedTiles:
            self.opened.append(tile)

        return True
        
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

    def checkWin(self):
        pass

    def checkSelfDrawnWin(self, melds, pairs):
        if melds == 4 and pairs == 1:
            return True
        else:
            return False

    def checkChi(self, tile):
        pass

    def checkPong(self, discardedTile):
        
        namesOfTilesInHand = []

        for tile in self.hand:
            namesOfTilesInHand.append(tile.name)

        numOfEachTile = Counter(namesOfTilesInHand)

        if (numOfEachTile[discardedTile.name] == 2):
            
            print("Pong possible! Would you like to pong? Enter y/n: ")
            userInput = input()
            
            if userInput == "Y" or userInput == "y":
                return self.pong(discardedTile)
            else:
                return False

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
    
    def checkMelds(self, printResult):

            self.sort_hand()

            tempHand1 = self.hand
            tempHand2 = self.hand

            playerTilesDict1 = self.list_to_dict(self.hand)
            playerTilesDict2 = self.list_to_dict(self.hand)

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
            
            if printResult == True:
                print("\nMelds/Pairs:%d/%d" % (maxMelds, pairs))

            return maxMelds, pairs

    def list_to_dict(self, lst):
        # Initialize an empty dictionary
        result_dict = {}
        
        # Iterate over the list
        for key in lst:
            # Increment the value if the key is already present, otherwise set it to 1
            result_dict[key] = result_dict.get(key, 0) + 1
        
        return result_dict
