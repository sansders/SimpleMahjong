from Objects.Tile import Tile
from Objects.Player import Player
from Objects.GameState import GameState
from Objects.DrawPile import DrawPile
from Objects.DiscardPile import DiscardPile
from Objects.DeadWall import DeadWall

def main(): 
    print("Begin:") 
    mahjong = initializeGame()
    print("Game initialized.\nTime to play mahjong!")
    play(mahjong)

def initializeGame():
    
    gameState = GameState()
    gameState.rollDice()
    gameState.setOrderFirstRound()

    players = initializePlayers()
    round = initializeRound(gameState, players)
    
    return round

def initializePlayers():        
    player1 = Player(1, [], [])
    player2 = Player(2, [], [])
    player3 = Player(3, [], [])
    player4 = Player(4, [], [])
    
    playerList = [player1, player2, player3, player4]
    print("Players initialized")
    
    return playerList

def initializeRound(gameState, players):
    
    tiles = initializeTiles()
    print("Tiles Initialized")

    drawPile = DrawPile(tiles)
    deadWall = DeadWall(drawPile.putIntoDeadWall())
    print("Draw Pile & Dead Wall initialized")

    discardPile = DiscardPile()
    print("Discard Pile initialized")

    # Draws at the start of the round
    for drawRounds in range(3):
        for player in range(4):
            for tiles in range(4):
                players[gameState.order[player]-1].draw(drawPile)
    
    for player in range(4):
        players[gameState.order[player]-1].draw(drawPile)

    print("Tiles left in draw pile:", len(drawPile.tiles))
    print("Tiles in dead wall: ", len(deadWall.tiles))

    gameState.players = players
    gameState.drawPile = drawPile
    gameState.deadWall = deadWall
    gameState.discardPile = discardPile

    return gameState

def initializeTiles():

    tiles = []

    for _ in range(4):

        redDragon = Tile(0, 0, 1, 0, "Red")
        greenDragon = Tile(0, 0, 2, 0, "Green")
        whiteDragon = Tile(0, 0, 3, 0, "White")

        east = Tile(0, 0, 0, 1, "East")
        south = Tile(0, 0, 0, 2, "South")
        west = Tile(0, 0, 0, 3, "West")
        north = Tile(0, 0, 0, 4, "North")
        
        oneDot = Tile(1, 1, 0, 0, "1Dot")
        twoDot = Tile(1, 2, 0, 0, "2Dot")
        threeDot = Tile(1, 3, 0, 0, "3Dot")
        fourDot = Tile(1, 4, 0, 0, "4Dot")
        fiveDot = Tile(1, 5, 0, 0, "5Dot")
        sixDot = Tile(1, 6, 0, 0, "6Dot")
        sevenDot = Tile(1, 7, 0, 0, "7Dot")
        eightDot = Tile(1, 8, 0, 0, "8Dot")
        nineDot = Tile(1, 9, 0, 0, "9Dot")

        oneBam = Tile(2, 1, 0, 0, "1Bam")
        twoBam = Tile(2, 2, 0, 0, "2Bam")
        threeBam = Tile(2, 3, 0, 0, "3Bam")
        fourBam = Tile(2, 4, 0, 0, "4Bam")
        fiveBam = Tile(2, 5, 0, 0, "5Bam")
        sixBam = Tile(2, 6, 0, 0, "6Bam")
        sevenBam = Tile(2, 7, 0, 0, "7Bam")
        eightBam = Tile(2, 8, 0, 0, "8Bam")
        nineBam = Tile(2, 9, 0, 0, "9Bam")

        oneCha = Tile(3, 1, 0, 0, "1Cha")
        twoCha = Tile(3, 2, 0, 0, "2Cha")
        threeCha = Tile(3, 3, 0, 0, "3Cha")
        fourCha = Tile(3, 4, 0, 0, "4Cha")
        fiveCha = Tile(3, 5, 0, 0, "5Cha")
        sixCha = Tile(3, 6, 0, 0, "6Cha")
        sevenCha = Tile(3, 7, 0, 0, "7Cha")
        eightCha = Tile(3, 8, 0, 0, "8Cha")
        nineCha = Tile(3, 9, 0, 0, "9Cha")

        tiles.append(redDragon)
        tiles.append(greenDragon)
        tiles.append(whiteDragon)
        
        tiles.append(east)
        tiles.append(south)
        tiles.append(west)
        tiles.append(north)

        tiles.append(oneDot)
        tiles.append(twoDot)
        tiles.append(threeDot)
        tiles.append(fourDot)
        tiles.append(fiveDot)
        tiles.append(sixDot)
        tiles.append(sevenDot)
        tiles.append(eightDot)
        tiles.append(nineDot)

        tiles.append(oneBam)
        tiles.append(twoBam)
        tiles.append(threeBam)
        tiles.append(fourBam)
        tiles.append(fiveBam)
        tiles.append(sixBam)
        tiles.append(sevenBam)
        tiles.append(eightBam)
        tiles.append(nineBam)

        tiles.append(oneCha)
        tiles.append(twoCha)
        tiles.append(threeCha)
        tiles.append(fourCha)
        tiles.append(fiveCha)
        tiles.append(sixCha)
        tiles.append(sevenCha)
        tiles.append(eightCha)
        tiles.append(nineCha)

    return tiles

# Insert game logic here
def play(gameState):
    pass

if __name__=="__main__": 
    main() 