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

Nouns - game, board, square, grid, token(marker), line (row, column)
        turn, player, human, computer,
Verbs - play, mark, win, choose,

Player (has a token)
- play
- choose
- mark
- win
- Computer(Player)
- Human(Player)

Board (has squares and rows, may contain markers/tokens,
        all of these elements require visual representation)
Square (may be marked by either player or not)
Game (has a board and 2 players)
Row (has squares, use term to include columns and diagonals)
Token (LS calling it a marker, same diff, X or O)
- X(Token)
- O(Token)
"""
import random
import sys
from os import system

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
GRAY = '\033[1;30m'
BOLD = '\033[1m'
RESET = '\033[0m'
NO_MARKER = ' '
P1_MARKER = f'{BOLD}X{RESET}'
P2_MARKER = f'{BOLD}O{RESET}'

class Square:
    def __init__(self, marker=NO_MARKER):
        self._marker = marker

    def is_unused(self):
        return self.marker == NO_MARKER

    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __str__(self):
        return self.marker

class Board:
    def __init__(self):
        self.squares = {square: Square() for square in range(1, 10)}

    def display(self):
        s = self.squares
        system('clear')
        if all(square.is_unused() for square in s.values()) and \
            TTTGame.games_started == 1:
            TTTGame.display_welcome(self)
        else:
            print(f"Player 1 is {P1_MARKER}. Player 2 is {P2_MARKER}.")
        
        print('')
        print('+-----+-----+-----+')
        print(f'|{GRAY}  1  {RESET}|'
              f'{GRAY}  2  {RESET}|'
              f'{GRAY}  3  {RESET}|')
        print(f"|  {s[1]}  |  {s[2]}  |  {s[3]}  |")
        print('|     |     |     |')
        print(f'|-----+-----+-----|    Player 1 score: {game.p1.points}')
        print(f'|{GRAY}  4  {RESET}|'
              f'{GRAY}  5  {RESET}|'
              f'{GRAY}  6  {RESET}|')
        print(f"|  {s[4]}  |  {s[5]}  |  {s[6]}  |")
        print('|     |     |     |')
        print(f'|-----+-----+-----|    Player 2 score: {game.p2.points}')
        print(f'|{GRAY}  7  {RESET}|'
              f'{GRAY}  8  {RESET}|'
              f'{GRAY}  9  {RESET}|')
        print(f"|  {s[7]}  |  {s[8]}  |  {s[9]}  |")
        print('|     |     |     |')
        print('+-----+-----+-----+')
        print('')
        print('3 in a row wins a point. 3 points wins the game!')

    def mark_square(self, square, marker):
        self.squares[square].marker = marker

    def unused_squares(self):
        return [key for key, square in self.squares.items()
                 if square.is_unused()]

    def count_markers_for(self, player, keys):
        markers = [self.squares[square].marker for square in keys]
        return markers.count(player.marker)

    def is_full(self):
        return len(self.unused_squares()) == 0

class Player:
    def __init__(self, marker):
        self._marker = marker
        self._points = 0

    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self, points):
        self._points = points
        

    def __str__(self):
        return self.marker

    def play(self):
        # STUB
        # We need a way for each player to play the game.
        # Do we need access to the board?
        pass

class Human(Player):
    def __init__(self, marker):
        # STUB
        # What does a human player need to do? How does it
        #   differ from the basic Player or a Computer?
        super().__init__(marker)

    def move(self):
        # STUB
        # get move logic from TTTGame.player1_moves()
        pass

class Computer(Player):
    def __init__(self, marker):
        super().__init__(marker)

    @staticmethod
    def find_two_in_row(board, marker):
        for line in TTTGame.WINNING_LINES:
            markers = [board.squares[square].marker for square in line]
            if markers.count(marker) == 2 and NO_MARKER in markers:
                return line
            
        return None

    def find_at_risk_square(self, board):
        center = 5

        for marker in [P2_MARKER, P1_MARKER]:
            line = self.find_two_in_row(board, marker)
            if line:
                return next((square for square in line if 
                            board.squares[square].marker == NO_MARKER), None)

        if board.squares[center].marker == NO_MARKER:
            return center

        return None

class TTTGame:
    WINNING_SCORE = 3
    WINNING_LINES = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
        )
    
    games_started = 0

    def __init__(self):
        # STUB
        # We need a board and two players.
        # For now, p1 is human, p2 is computer, but update to allow 2 humans,
        #   and to allow p1 to be computer and p2 to be human,
        #   and maybe to allow the user to watch 2 computers play.
        #   If they wanted to. For some reason or other.
        self.board = Board()
        self.p1 = Human(P1_MARKER) #FIXME allow user to decide Player classes
        self.p2 = Computer(P2_MARKER)
        self.winner = None
        TTTGame.games_started += 1

    def play(self):
        while True:
            self.board.display()

            self.player1_moves()
            if self.is_game_over():
                break

            self.player2_moves()
            if self.is_game_over():
                break

        if self.winner:
            self.award_point(self.winner)
        self.board.display()
        self.display_results()
        if self.p1.points < self.WINNING_SCORE and \
            self.p2.points < self.WINNING_SCORE:
            self.board = Board()
            self.winner = None
            self.play()

        for player in (self.p1, self.p2):
            if player.points >= self.WINNING_SCORE:
                self.display_game_over(player)
                play_again = self.play_again()
                if play_again:
                    self.board = Board()
                    self.p1.points = 0
                    self.p2.points = 0
                    self.winner = None
                    self.play()
                else:
                    self.display_goodbye()

    def display_welcome(self):
        system('clear')
        print('Welcome to Tic Tac Toe!')

    def display_results(self):
        if self.is_winner(self.p1):
            print("Player 1 scores! Congratulations!")
        elif self.is_winner(self.p2):
            print("Player 2 scores! Bad news for Player 1.")
        else:
            print("A tie. Womp womp.")

        input("\nEnter/Return to continue")

    def display_game_over(self, player):
        player_name = "Player 1" if player is self.p1 else "Player 2"
        print(f'{player_name} has 3 points! Good game!')

    def display_goodbye(self):
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def award_point(self, player):
        player.points += 1

    @staticmethod
    def _join_or(iterable, delimiter=', ', conjunction=' or '):
        output = ''
        if len(iterable) == 0:
            pass
        elif len(iterable) == 1:
            output = str(iterable[0])
        elif len(iterable) == 2:
            output = f"{iterable[0]}{conjunction}{iterable[1]}"
        else:
            output = delimiter.join(str(item) for item in iterable[:-1]) \
                + f"{conjunction}{iterable[-1]}"

        return output

    def player1_moves(self):    # human player by default
        # probably belongs in Player class
        # FIXME change to a call to self.p1.move() so that the player object's class determines move behavior
        valid_choices = self.board.unused_squares()
        while True:
            choices = self._join_or(valid_choices)
            choice = input(f"Choose a square ({choices}): ")

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.\n")

        self.board.mark_square(choice, P1_MARKER)

    def player2_moves(self):    # computer by default
        # probably belongs in Player class
        # FIXME change to a call to self.p2.move() so that the player object's
        #   class determines move behavior
        valid_choices = self.board.unused_squares()
        choice = self.p2.find_at_risk_square(self.board)
        if not choice:
            choice = random.choice(valid_choices)
        self.board.mark_square(choice, P2_MARKER)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def someone_won(self):
        return (self.is_winner(self.p1) or
                self.is_winner(self.p2))
    
    def is_winner(self, player):
        for line in TTTGame.WINNING_LINES:
            if self.three_in_a_line(player, line):
                self.winner = player
                return True

        return False

    def three_in_a_line(self, player, line):
        return self.board.count_markers_for(player, line) == 3
    
    def play_again(self):
        answer = input("Would you like to play again? (y/n)\n")
        while answer.casefold() not in ('y', 'n', 'yes', 'no'):
            print("What?")
            answer = input("Would you like to play again? (y/n)\n")

        if answer.casefold() in ('y', 'yes'):
            return True
        
        return False


game = TTTGame()
game.display_welcome()
game.play()