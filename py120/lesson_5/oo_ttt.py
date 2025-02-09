"""
P
Tic Tac Toe
- 2-player board game
    - can be 2 humans or human & computer
    - board is 3 * 3 grid
- players take turns choosing a square on the grid 
    - and then marking it with their token (X or O)
- first player to mark 3 in sequence wins (i.e. column, row, or diagonal)
- player taking first turn uses X, other player uses O
- human will move first in initial version of game, but will update later

Nouns - game, board, square, grid, token(marker), row, column
        turn, player, human, computer,
Verbs - play, mark, win, choose,

Player (has a token)
- play
- choose
- mark
- win
- Computer(Player)
- Human(Player)

Board (has squares and rows, may contain tokens/markers,
        all of these elements require visual representation)
Square (may be marked by either player or not)
Game (has a board)
Row (has squares, use term to include columns and diagonals)
Token (LS calling it a marker, same diff, X or O)
- X(Token)
- O(Token)
"""