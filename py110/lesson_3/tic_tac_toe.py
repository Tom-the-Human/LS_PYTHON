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
WINNING_SCORE = 3
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

def prompt(message):
    print(f'<#> {message} <#>')

def join_or(iterable, delimiter=', ', final_option=' or '):
    output = ''
    if len(iterable) == 0:
        pass
    elif len(iterable) == 1:
        output = str(iterable[0])
    elif len(iterable) == 2:
        output = f"{iterable[0]}{final_option}{iterable[1]}"
    else:
        output = delimiter.join(str(item) for item in iterable[:-1]) \
            + f"{final_option}{iterable[-1]}"

    return output

def display_board(board, score):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {CPU_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print(f'-----+-----+-----      Your score: {score[0]}')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print(f'-----+-----+-----    Computer score: {score[1]}')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items()
            if value == INITIAL_MARKER]

def find_at_risk_square(line, board):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(CPU_MARKER) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    elif markers_in_line.count(HUMAN_MARKER) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    elif board[5] == INITIAL_MARKER:
        return 5

    return None

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

    for line in WINNING_LINES:
        square = find_at_risk_square(line, board)
        if square:
            board[square] = CPU_MARKER
            return

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = CPU_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winner = None
    for line in WINNING_LINES:
        if all(board[sq] == HUMAN_MARKER for sq in line):
            winner = 'You'
        elif all(board[sq]== CPU_MARKER for sq in line):
            winner = 'The computer'

    return winner

def who_goes_first():
    prompt('Who will go first? Enter 1, 2, or 3')
    prompt('1. Player')
    prompt('2. Computer')
    prompt('3. Coin toss')
    prompt('Any other entry will result in a coin toss.')
    selection = input().strip()

    if selection not in {'1', '2'}:
        selection = random.choice(['1', '2'])

    return selection

def play_round(board, score):
    first = who_goes_first()
    while first == '1':
        display_board(board, score)
        prompt('You go first.')

        player_chooses_square(board)
        display_board(board, score)
        if someone_won(board) or board_full(board):
            break

        computer_chooses_square(board)
        display_board(board, score)
        if someone_won(board) or board_full(board):
            break

    while first == '2':
        display_board(board, score)
        prompt('Computer goes first.')

        computer_chooses_square(board)
        display_board(board, score)
        if someone_won(board) or board_full(board):
            break

        player_chooses_square(board)
        display_board(board, score)
        if someone_won(board) or board_full(board):
            break

    winner = detect_winner(board)
    if winner == 'You':
        score[0] += 1
    elif winner == 'The computer':
        score[1] += 1

def play_again():
    prompt('Play again? (y/n)')
    answer = input().lower().strip()

    while answer not in {'y', 'yes', 'n', 'no'}:
        prompt("It's a yes or no question o_O")
        prompt('Play again? (y/n)')
        answer = input().lower().strip()

    return answer in {'y', 'yes'}

def main():
    os.system('clear')
    prompt("Welcome to Tic-Tac-Toe! 3-in-a-row wins a point.")
    prompt("First to score 3 points wins the game!")
    print('')
    while True:
        score = [0, 0]
        while True:
            board = initialize_board()

            play_round(board, score)

            winner = detect_winner(board)
            if winner:
                prompt(f"{winner} scored a point!")
                input('Enter/Return to continue')
            else:
                prompt("It's a tie! Let's go again!")
                input('Enter/Return to continue')

            display_board(board, score)

            if score[0] == WINNING_SCORE:
                prompt("🎉Congratulations! You win!🎊")
                break
            if score[1] == WINNING_SCORE:
                prompt("The computer won the game. Better luck next time!")
                break

        if not play_again():
            break

    prompt("Thanks for playing!")

main()