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

    print("Tiles left in draw pile:", len(drawPile.tiles))
    print("Tiles in dead wall: ", len(deadWall.tiles))
    print("Number of tiles (Player 1):", len(players[0].hand))
    print("Number of tiles (Player 2):", len(players[1].hand))
    print("Number of tiles (Player 3):", len(players[2].hand))
    print("Number of tiles (Player 4):", len(players[3].hand))

    gameState.players = players
    gameState.drawPile = drawPile
    gameState.deadWall = deadWall
    gameState.discardPile = discardPile

    return gameState

def initializeTiles():

    tiles = []

    for _ in range(4):

        redDragon = Tile(0, 0, 1, 0)
        greenDragon = Tile(0, 0, 2, 0)
        whiteDragon = Tile(0, 0, 3, 0)

        east = Tile(0, 0, 0, 1)
        south = Tile(0, 0, 0, 2)
        west = Tile(0, 0, 0, 3)
        north = Tile(0, 0, 0, 4)
        
        oneDot = Tile(1, 1, 0, 0)
        twoDot = Tile(1, 2, 0, 0)
        threeDot = Tile(1, 3, 0, 0)
        fourDot = Tile(1, 4, 0, 0)
        fiveDot = Tile(1, 5, 0, 0)
        sixDot = Tile(1, 6, 0, 0)
        sevenDot = Tile(1, 7, 0, 0)
        eightDot = Tile(1, 8, 0, 0)
        nineDot = Tile(1, 9, 0, 0)

        oneBamb = Tile(2, 1, 0, 0)
        twoBamb = Tile(2, 2, 0, 0)
        threeBamb = Tile(2, 3, 0, 0)
        fourBamb = Tile(2, 4, 0, 0)
        fiveBamb = Tile(2, 5, 0, 0)
        sixBamb = Tile(2, 6, 0, 0)
        sevenBamb = Tile(2, 7, 0, 0)
        eightBamb = Tile(2, 8, 0, 0)
        nineBamb = Tile(2, 9, 0, 0)

        oneChara = Tile(3, 1, 0, 0)
        twoChara = Tile(3, 2, 0, 0)
        threeChara = Tile(3, 3, 0, 0)
        fourChara = Tile(3, 4, 0, 0)
        fiveChara = Tile(3, 5, 0, 0)
        sixChara = Tile(3, 6, 0, 0)
        sevenChara = Tile(3, 7, 0, 0)
        eightChara = Tile(3, 8, 0, 0)
        nineChara = Tile(3, 9, 0, 0)

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

        tiles.append(oneBamb)
        tiles.append(twoBamb)
        tiles.append(threeBamb)
        tiles.append(fourBamb)
        tiles.append(fiveBamb)
        tiles.append(sixBamb)
        tiles.append(sevenBamb)
        tiles.append(eightBamb)
        tiles.append(nineBamb)

        tiles.append(oneChara)
        tiles.append(twoChara)
        tiles.append(threeChara)
        tiles.append(fourChara)
        tiles.append(fiveChara)
        tiles.append(sixChara)
        tiles.append(sevenChara)
        tiles.append(eightChara)
        tiles.append(nineChara)

    return tiles

# Insert game logic here
def play(gameState):
    pass

if __name__=="__main__": 
    main() 