# P
# 1 Display the initial empty 3x3 board.
    # 1 perhaps a list of lists
    # 2 but how to represent an empty square???
    # 3 board should be persistent, so best to
    #   clear screen and keep it at the top
# 2 Ask the user to mark a square.
    # 1 input selection will require a catalogue of squares
    #   or other way to target the desired square
    # 2 the board must be updated
# 3 Computer marks a square.
    # 1 how will the computer choose? randomly?
    # 2 the board must be updated
# 4 Display the updated board state.
    # 1 determine board representation including
    #    empty, marked by player, or marked by CPU
# 5 If it's a winning board, display the winner.
    # 1 print below board
# 6 If the board is full, display tie.
    # 1 print below poard
# 7 If neither player won and the board is not full, go to #2
# 8 Play again?
# 9 If yes, go to #1
# 10 Goodbye!
# You can see from the above sequence that there are two main loops:
# An outer loop between steps #1 and #9 that repeats as 
# long as the player wants to keep playing.
# An inner loop between steps #2 and #7 that repeats as 
# long as there is no winner and the board isn't full.

# E
#  _A__B__C_
# 1|__|_X|__|    A possible representation
# 2|__|_O|__|
# 3|_O|__|__|
# Other options will likely come to mind while working on it. 

# D
# I think a list of lists for the board, with strings for board rep
# Maybe a dict for acceptable board coords

# A



# C
import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
CPU_MARKER = 'O'

def prompt(message):
    print(f'<#> {message} <#>')

def join_or(iterable, delimiter=', ', final_option=' or '):
    if len(iterable) == 0:
        return ''
    elif len(iterable) == 1:
        return str(iterable[0])
    elif len(iterable) == 2:
        return f"{iterable[0]}{final_option}{iterable[1]}"
    else:
        return delimiter.join(str(item) for item in iterable[:-1]) \
            + f"{final_option}{iterable[-1]}"


def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {CPU_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items()
            if value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        prompt(f"Choose a square ({join_or(empty_squares(board))}):")
        square = input().strip()
        try:
            square = int(square)
        except ValueError:
            pass

        if square in empty_squares(board):
            break
        
        prompt("Sorry, that's not a valid choice.")

    board[square] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = CPU_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
        if all(board[sq] == HUMAN_MARKER for sq in line):
                return 'You'
        elif all(board[sq]== CPU_MARKER for sq in line):
                return 'Computer'
        
    return None

def play_again():
    prompt('Play again? (y/n)')
    answer = input().lower().strip()

    while answer not in {'y', 'yes', 'n', 'no'}:
        prompt("It's a yes or no question o_O")
        prompt('Play again? (y/n)')
        answer = input().lower().strip()

    return answer in {'y', 'yes'}

def main():
    while True:
        board = initialize_board()

        while True:
            display_board(board)

            player_chooses_square(board)
            display_board(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            display_board(board)
            if someone_won(board) or board_full(board):
                break

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        if not play_again():
            break
    
    prompt("Thanks for playing!")

main()