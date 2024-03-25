from collections import Counter

# Define a class named 'Player'
class Player:
    
    # Constructor method to initialize the object
    def __init__(self, playerId, hand):
        self.playerId = playerId
        self.hand = hand
        self.wins = 0

    def discard(self, tileIndex):
        discardedTile = self.hand.pop(tileIndex)
        return discardedTile

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
            tempHand3 = self.hand
            tempHand4 = self.hand
            tempHand5 = self.hand
            tempHand6 = self.hand

            playerTilesDict1 = self.list_to_dict(self.hand)
            playerTilesDict2 = self.list_to_dict(self.hand)
            playerTilesDict3 = self.list_to_dict(self.hand)
            playerTilesDict4 = self.list_to_dict(self.hand)
            playerTilesDict5 = self.list_to_dict(self.hand)
            playerTilesDict6 = self.list_to_dict(self.hand)

            maxMelds = 0
            pairs = 0
            melds1 = 0
            pairs1 = 0
            melds2 = 0
            pairs2 = 0
            melds3 = 0
            pairs3 = 0
            melds4 = 0
            pairs4 = 0
            melds5 = 0
            pairs5 = 0
            melds6 = 0
            pairs6 = 0

            # Part 1: Check sequences, then triplets, then pairs
            # Part 2: Check triplets, sequences, then pairs
            # Part 3: Check pairs, sequences, then triplets
            # Part 4: Check pairs, triplets, then sequences
            # Part 5: Check sequences, pairs, then triplets
            # Part 6: Check triplets, pairs, then sequences

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
                        
            # Part 3: Check pairs, sequences, then triplets
            # Part 3a: Check pairs
            for tile in range(0, len(tempHand3)-1):

                tileWind = tempHand3[tile].getTileWind()
                tileDragon = tempHand3[tile].getTileDragon()
                tileSuit = tempHand3[tile].getTileSuit()
                tileNumber = tempHand3[tile].getTileNumber()

                if playerTilesDict3[tempHand3[tile]] == 0:
                    continue

                if tempHand3[tile+1].getTileSuit() == tileSuit and tempHand3[tile+1].getTileNumber() == tileNumber \
                    and tempHand3[tile+1].getTileDragon() == tileDragon and tempHand3[tile+1].getTileWind() == tileWind:
                        playerTilesDict3[tempHand3[tile]] -= 1
                        playerTilesDict3[tempHand3[tile+1]] -= 1
                        pairs3 += 1
                        tile += 2

            # Part 3b: Check sequences
            for tile in range(0, len(tempHand3)-2):

                if playerTilesDict3[tempHand3[tile]] == 0:
                    continue

                tilePlusOne = tempHand3[tile].getTileNumber() + 1
                tilePlusTwo = tempHand3[tile].getTileNumber() + 2
                tileSuit = tempHand3[tile].getTileSuit()

                passOne = 0
                firstTile = tempHand3[tile]
                secondTile = "" 
                thirdTile = ""

                for playerTileDictKeys in playerTilesDict3:
                    
                    if passOne == 0:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                            and playerTilesDict3[playerTileDictKeys] != 0:
                            passOne = 1
                            secondTile = playerTileDictKeys
                    
                    elif passOne == 1:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                            and playerTilesDict3[playerTileDictKeys] != 0:
                            thirdTile = playerTileDictKeys
                            playerTilesDict3[firstTile] -= 1
                            playerTilesDict3[secondTile] -= 1
                            playerTilesDict3[thirdTile] -= 1

                            melds3 += 1
                            passOne = 0

                            break

            # Part 3c: Check triplets
            for tile in range(0, len(tempHand3)-2):
                
                tileWind = tempHand3[tile].getTileWind()
                tileDragon = tempHand3[tile].getTileDragon()
                tileSuit = tempHand3[tile].getTileSuit()
                tileNumber = tempHand3[tile].getTileNumber()

                if playerTilesDict3[tempHand3[tile]] == 0:
                    continue

                if tempHand3[tile+1].getTileSuit() == tileSuit and tempHand3[tile+1].getTileNumber() == tileNumber \
                    and tempHand3[tile+1].getTileDragon() == tileDragon and tempHand3[tile+1].getTileWind() == tileWind:
                    if tempHand3[tile+2].getTileSuit() == tileSuit and tempHand3[tile+2].getTileNumber() == tileNumber \
                        and tempHand3[tile+2].getTileDragon() == tileDragon and tempHand3[tile+2].getTileWind() == tileWind:
                        playerTilesDict3[tempHand3[tile]] -= 1
                        playerTilesDict3[tempHand3[tile+1]] -= 1
                        playerTilesDict3[tempHand3[tile+2]] -= 1
                        melds3 += 1
                        tile += 3   

            # Part 4: Check pairs, triplets, then sequences
            # Part 4a: Check pairs
            for tile in range(0, len(tempHand4)-1):

                tileWind = tempHand4[tile].getTileWind()
                tileDragon = tempHand4[tile].getTileDragon()
                tileSuit = tempHand4[tile].getTileSuit()
                tileNumber = tempHand4[tile].getTileNumber()

                if playerTilesDict4[tempHand4[tile]] == 0:
                    continue

                if tempHand4[tile+1].getTileSuit() == tileSuit and tempHand4[tile+1].getTileNumber() == tileNumber \
                    and tempHand4[tile+1].getTileDragon() == tileDragon and tempHand4[tile+1].getTileWind() == tileWind:
                        playerTilesDict4[tempHand4[tile]] -= 1
                        playerTilesDict4[tempHand4[tile+1]] -= 1
                        pairs4 += 1
                        tile += 2

            # Part 4b: Check triplets
            for tile in range(0, len(tempHand4)-2):
                
                tileWind = tempHand4[tile].getTileWind()
                tileDragon = tempHand4[tile].getTileDragon()
                tileSuit = tempHand4[tile].getTileSuit()
                tileNumber = tempHand4[tile].getTileNumber()

                if playerTilesDict4[tempHand4[tile]] == 0:
                    continue

                if tempHand4[tile+1].getTileSuit() == tileSuit and tempHand4[tile+1].getTileNumber() == tileNumber \
                    and tempHand4[tile+1].getTileDragon() == tileDragon and tempHand4[tile+1].getTileWind() == tileWind:
                    if tempHand4[tile+2].getTileSuit() == tileSuit and tempHand4[tile+2].getTileNumber() == tileNumber \
                        and tempHand4[tile+2].getTileDragon() == tileDragon and tempHand4[tile+2].getTileWind() == tileWind:
                        playerTilesDict4[tempHand4[tile]] -= 1
                        playerTilesDict4[tempHand4[tile+1]] -= 1
                        playerTilesDict4[tempHand4[tile+2]] -= 1
                        melds4 += 1
                        tile += 3   

            # Part 4c: Check sequences
            for tile in range(0, len(tempHand4)-2):

                if playerTilesDict4[tempHand4[tile]] == 0:
                    continue

                tilePlusOne = tempHand4[tile].getTileNumber() + 1
                tilePlusTwo = tempHand4[tile].getTileNumber() + 2
                tileSuit = tempHand4[tile].getTileSuit()

                passOne = 0
                firstTile = tempHand4[tile]
                secondTile = "" 
                thirdTile = ""

                for playerTileDictKeys in playerTilesDict4:
                    
                    if passOne == 0:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                            and playerTilesDict4[playerTileDictKeys] != 0:
                            passOne = 1
                            secondTile = playerTileDictKeys
                    
                    elif passOne == 1:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                            and playerTilesDict4[playerTileDictKeys] != 0:
                            thirdTile = playerTileDictKeys
                            playerTilesDict4[firstTile] -= 1
                            playerTilesDict4[secondTile] -= 1
                            playerTilesDict4[thirdTile] -= 1

                            melds4 += 1
                            passOne = 0

                            break

            # Part 5: Check sequences, pairs, then triplets
            # Part 5a: Check sequences
            for tile in range(0, len(tempHand5)-2):

                if playerTilesDict5[tempHand5[tile]] == 0:
                    continue

                tilePlusOne = tempHand5[tile].getTileNumber() + 1
                tilePlusTwo = tempHand5[tile].getTileNumber() + 2
                tileSuit = tempHand5[tile].getTileSuit()

                passOne = 0
                firstTile = tempHand5[tile]
                secondTile = "" 
                thirdTile = ""

                for playerTileDictKeys in playerTilesDict5:
                    
                    if passOne == 0:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                            and playerTilesDict5[playerTileDictKeys] != 0:
                            passOne = 1
                            secondTile = playerTileDictKeys
                    
                    elif passOne == 1:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                            and playerTilesDict5[playerTileDictKeys] != 0:
                            thirdTile = playerTileDictKeys
                            playerTilesDict5[firstTile] -= 1
                            playerTilesDict5[secondTile] -= 1
                            playerTilesDict5[thirdTile] -= 1

                            melds5 += 1
                            passOne = 0

                            break

            # Part 5b: Check pairs
            for tile in range(0, len(tempHand5)-1):

                tileWind = tempHand5[tile].getTileWind()
                tileDragon = tempHand5[tile].getTileDragon()
                tileSuit = tempHand5[tile].getTileSuit()
                tileNumber = tempHand5[tile].getTileNumber()

                if playerTilesDict5[tempHand5[tile]] == 0:
                    continue

                if tempHand5[tile+1].getTileSuit() == tileSuit and tempHand5[tile+1].getTileNumber() == tileNumber \
                    and tempHand5[tile+1].getTileDragon() == tileDragon and tempHand5[tile+1].getTileWind() == tileWind:
                        playerTilesDict5[tempHand5[tile]] -= 1
                        playerTilesDict5[tempHand5[tile+1]] -= 1
                        pairs5 += 1
                        tile += 2

            # Part 5c: Check triplets
            for tile in range(0, len(tempHand5)-2):
                
                tileWind = tempHand5[tile].getTileWind()
                tileDragon = tempHand5[tile].getTileDragon()
                tileSuit = tempHand5[tile].getTileSuit()
                tileNumber = tempHand5[tile].getTileNumber()

                if playerTilesDict5[tempHand5[tile]] == 0:
                    continue

                if tempHand5[tile+1].getTileSuit() == tileSuit and tempHand5[tile+1].getTileNumber() == tileNumber \
                    and tempHand5[tile+1].getTileDragon() == tileDragon and tempHand5[tile+1].getTileWind() == tileWind:
                    if tempHand5[tile+2].getTileSuit() == tileSuit and tempHand5[tile+2].getTileNumber() == tileNumber \
                        and tempHand5[tile+2].getTileDragon() == tileDragon and tempHand5[tile+2].getTileWind() == tileWind:
                        playerTilesDict5[tempHand5[tile]] -= 1
                        playerTilesDict5[tempHand5[tile+1]] -= 1
                        playerTilesDict5[tempHand5[tile+2]] -= 1
                        melds5 += 1
                        tile += 3   

            # Part 6: Check triplets, pairs, then sequences
            # Part 6a: Check triplets
            for tile in range(0, len(tempHand6)-2):
                
                tileWind = tempHand6[tile].getTileWind()
                tileDragon = tempHand6[tile].getTileDragon()
                tileSuit = tempHand6[tile].getTileSuit()
                tileNumber = tempHand6[tile].getTileNumber()

                if playerTilesDict6[tempHand6[tile]] == 0:
                    continue

                if tempHand6[tile+1].getTileSuit() == tileSuit and tempHand6[tile+1].getTileNumber() == tileNumber \
                    and tempHand6[tile+1].getTileDragon() == tileDragon and tempHand6[tile+1].getTileWind() == tileWind:
                    if tempHand6[tile+2].getTileSuit() == tileSuit and tempHand6[tile+2].getTileNumber() == tileNumber \
                        and tempHand6[tile+2].getTileDragon() == tileDragon and tempHand6[tile+2].getTileWind() == tileWind:
                        playerTilesDict6[tempHand6[tile]] -= 1
                        playerTilesDict6[tempHand6[tile+1]] -= 1
                        playerTilesDict6[tempHand6[tile+2]] -= 1
                        melds6 += 1
                        tile += 3   

            # Part 6b: Check pairs
            for tile in range(0, len(tempHand6)-1):

                tileWind = tempHand6[tile].getTileWind()
                tileDragon = tempHand6[tile].getTileDragon()
                tileSuit = tempHand6[tile].getTileSuit()
                tileNumber = tempHand6[tile].getTileNumber()

                if playerTilesDict6[tempHand6[tile]] == 0:
                    continue

                if tempHand6[tile+1].getTileSuit() == tileSuit and tempHand6[tile+1].getTileNumber() == tileNumber \
                    and tempHand6[tile+1].getTileDragon() == tileDragon and tempHand6[tile+1].getTileWind() == tileWind:
                        playerTilesDict6[tempHand6[tile]] -= 1
                        playerTilesDict6[tempHand6[tile+1]] -= 1
                        pairs6 += 1
                        tile += 2

            # Part 5a: Check sequences
            for tile in range(0, len(tempHand6)-2):

                if playerTilesDict6[tempHand6[tile]] == 0:
                    continue

                tilePlusOne = tempHand6[tile].getTileNumber() + 1
                tilePlusTwo = tempHand6[tile].getTileNumber() + 2
                tileSuit = tempHand6[tile].getTileSuit()

                passOne = 0
                firstTile = tempHand6[tile]
                secondTile = "" 
                thirdTile = ""

                for playerTileDictKeys in playerTilesDict6:
                    
                    if passOne == 0:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusOne \
                            and playerTilesDict6[playerTileDictKeys] != 0:
                            passOne = 1
                            secondTile = playerTileDictKeys
                    
                    elif passOne == 1:
                        if playerTileDictKeys.getTileSuit() == tileSuit and playerTileDictKeys.getTileNumber() == tilePlusTwo \
                            and playerTilesDict6[playerTileDictKeys] != 0:
                            thirdTile = playerTileDictKeys
                            playerTilesDict6[firstTile] -= 1
                            playerTilesDict6[secondTile] -= 1
                            playerTilesDict6[thirdTile] -= 1

                            melds6 += 1
                            passOne = 0

                            break

            # Get best meld count based on order of obtaining the melds
            meldsList = [melds1, melds2, melds3, melds4, melds5, melds6]
            pairsList = [pairs1, pairs2, pairs3, pairs4, pairs5, pairs6]

            maxMelds = meldsList[0]
            pairs = pairsList[0]

            for i in range(0, len(meldsList)-1):
                if meldsList[i] > maxMelds:
                    maxMelds = meldsList[i]
                    pairs = pairsList[i]
                elif meldsList[i] == maxMelds and pairsList[i] > pairs:
                    pairs = pairsList[i]
            
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
