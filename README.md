# SimpleMahjong
A simplified version of Mahjong.

## Ruleset

I will list the points in 3 main groups:
1. Setup
2. Win Condition
3. Gameplay

### 2.1 Setup

1. The total number of tiles in play is 136, comprising of 4 sets of:
    - ![image](https://hackmd.io/_uploads/rJvgHNK9a.png)
    - ![image](https://hackmd.io/_uploads/HJaJB4F96.png)
    - ![image](https://hackmd.io/_uploads/rkHbBVK56.png)
2. There are no prevalent winds, unlike in regular Mahjong.
3. None of the players are assigned any winds to, unlike in regular Mahjong.
4. The first player to start a round is determined by a random dice roll between 3 and 18, with the highest-scoring player going first, then moving counter clockwise. If there are any ties, all players roll again.
5. At the beginning of a round, the tiles are randomized and placed into a draw pile.
6. The last 10 tiles from the draw pile are removed, with no knowledge to any player about what those 10 tiles are. These tiles will be placed in a Dead Wall.
7. Starting from the first player, each player takes turns to draw 4 tiles from the draw pile at a time, anti-clockwise, until they have 12 tiles each. Each player then draws 1 tile each to complete their starting hand.
8. The order of which player starts each round will rotate anti-clockwise.

### Win Condition

1. A player **must** have 4 melds and 1 pair.
2. A meld can either comprise of:
    - A correctly-ordered sequence of 3 tiles of the same suit.
    - A set of 3 of the same tiles.
3. The pair must be two of the same tiles.
4. The winning tile can either be self-drawn or taken from any other player's discards.
5. If more than one player wins on a discarded tile at the same time, only the player to the right of the player who discarded the winning tile gets the win.

### Gameplay

1. On a player's turn, they must draw one tile from the draw pile.
2. The player must discard one tile from their hand to end their turn.
3. The turn ends and the next player on the right may draw a tile from the draw pile.
4. This goes on until either there are no more tiles in the draw pile, or if a player reaches the winning condition.
5. To clarify, there will be no "Chi", "Pong", or "Kong" in this version of Mahjong.
