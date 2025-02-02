"""
To Do:

Implement flavor text - i.e. "Rock crushes scissors"
Possibly extract helpers for display_winner and for game end logic
Reset score and pick new opponent if _play_again
"""

from random import choice
from os import system

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'

class Player:
    MOVES = {'1': 'rock', '2': 'paper', '3': 'scissors',}
    NAMES = ('Amy', 'Beefcake', 'Curly', 'Doc', 'Eeyore', 'Fireball', 'Gunther',
             'Hot Stuff', 'Ignatius', 'Jerry', 'Karl', 'Louise', 'Monkey', 'Nerd',
             'Old Top', 'Poindexter', 'Quincy', 'Ripley', 'Sweetheart', 'Trashcat',
             'Uncle', 'Venus', 'Weirdo', 'Xavier', 'Yoko', 'Zorro',)

    def __init__(self):
        self.name = None
        self.move = None

class Computer(Player):
    BOTS = ('CatGPT', 'Crushinator', 'GLaDOS',
            'Data', 'Clippy', 'B-MO', 'Ameca',)

    def __init__(self, game):
        super().__init__()
        self._game =  game      # ref to game instance
        self._bot = choice(Computer.BOTS)
        self.name = f"{RED}{self._bot}{RESET}"

    def choose(self):
        match self._bot:
            case 'B-MO':
                # truely random
                self.move = Player.MOVES.get(str(choice(range(1, 4))))
            case 'CatGPT':
                # usually paper (because cats like sitting on paper),
                #   rarely rock (because they also like a warm rock)
                probs = (1, 2, 2, 2, 2, 2)
                self.move = Player.MOVES.get(str(choice(probs)))
            case 'Crushinator':
                # always rock
                self.move = 'rock'
            case 'GLaDOS':
                # usually scissors, sometimes rock, ocassionally paper
                probs = (1, 1, 1, 2, 3, 3, 3, 3, 3)
                self.move = Player.MOVES.get(str(choice(probs)))
            case 'Clippy':
                # 66% paper, 33% scissors
                probs = (2, 2, 2, 2, 3, 3)
                self.move = Player.MOVES.get(str(choice(probs)))
            case 'Data':
                # always picks in order - first rock, then paper, then scissors
                if self._game.move_history.get('cpu') == []:
                    self.move = 'rock'
                else:
                    match self._game.move_history['cpu'][-1]:
                        case 'rock':
                            self.move = 'paper'
                        case 'paper':
                            self.move = 'scissors'
                        case 'scissors':
                            self.move = 'rock'
            case 'Ameca':
                # copies the player's previous move
                if self._game.move_history.get('human') == []:
                    self.move = 'scissors'
                else:
                    match self._game.move_history['human'][-1]:
                        case 'rock':
                            self.move = 'rock'
                        case 'paper':
                            self.move = 'paper'
                        case 'scissors':
                            self.move = 'scissors'

class Human(Player):
    def __init__(self, game):
        super().__init__()
        self._game =  game      # ref to game instance
        self.name = input("What's your first name?\n")
        if self.name.strip().isalpha():
            self.name = f"{GREEN}{self.name.strip()}{RESET}"
        else:
            self.name = f"{GREEN}{choice(Player.NAMES)}{RESET}"

    def choose(self):
        while True:
            self._game._score.display_scoreboard()
            print(f"It's your turn, {self.name}!")
            print(f'Use {YELLOW}1, 2, or 3{RESET} to choose your move!\n'
                f'(Or use {YELLOW}(R){RESET} to read the rules)')
            move = input('(1) Rock\n(2) Paper\n'
                        '(3) Scissors\n(R) Rules\n').strip().lower()

            if move == 'r':
                RPSGame.display_rules()
                continue  # Restart the loop after displaying rules

            if move in Player.MOVES:
                self.move = Player.MOVES.get(move)
                break

            print(f'{YELLOW}Please pick a valid option!{RESET}')

class Score:
    def __init__(self, game):
        self._human = 0
        self._cpu = 0
        self._game = game
    
    def display_scoreboard(self):
        system('clear')
        print(f"{self._game._human.name}: {self.human}")
        print(f"{self._game._cpu.name}: {self.cpu}")

    @property
    def human(self):
        return self._human
    
    @human.setter
    def human(self, points):
        self._human = points

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, points):
        self._cpu = points

class RPSGame:
    # Game "engine" / flow control object
    def __init__(self):
        self._human = Human(self)
        self._cpu = Computer(self)
        self._score = Score(self)
        self.move_history = {'human': [], 'cpu': []}

    def _display_welcome_message(self):
        print(f"Welcome to Rock Paper Scissors, {self._human.name}!")
        print(f"Your opponent is {self._cpu.name}.")
        input('\nEnter/Return to continue')

    def _display_goodbye_message(self):
        system('clear')
        print(f"Thanks for playing! Goodbye, {self._human.name}!")

    def display_rules():
        system('clear')
        print(f"{BOLD}Rules of Rock, Paper, Scissors{RESET}\n")
        print("Rock beats scissors.")
        print("Paper beats rock.")
        print("Scissors beats paper.\n")
        print("First player to score 5 points wins the game!\n")
        input("Enter/Return to continue")

    def _human_wins(self):
        human_move = self._human.move
        cpu_move = self._cpu.move

        return ((human_move == 'rock' and cpu_move == 'scissors') or
                (human_move == 'scissors' and cpu_move == 'paper') or
                (human_move == 'paper' and cpu_move == 'rock'))

    def _cpu_wins(self):
        human_move = self._human.move
        cpu_move = self._cpu.move

        return ((cpu_move == 'rock' and human_move == 'scissors') or
                (cpu_move == 'scissors' and human_move == 'paper') or
                (cpu_move == 'paper' and human_move == 'rock'))
    
    # def _display_round_info(self): #FIXME

    def _display_winner(self):
        human_move = self._human.move
        cpu_move = self._cpu.move

        print(f'You chose: {human_move}.')
        self.move_history['human'].append(human_move)

        print(f'The computer chooses: {cpu_move}.')
        self.move_history['cpu'].append(cpu_move)

        # display_winner also updates scores. should this be changed? 
        # yes, try to extract round info, score updates, and move history updates
        # how to structure that?
        if self._human_wins():
            self._score.human += 1
            print(f'You win this round, {self._human.name}! You score a point!')
        elif self._cpu_wins():
            self._score.cpu += 1
            print(f'Oh no, you lost this round! {self._cpu.name} scores a point!')
        else:
            print("It's a tie.")
        
        input('\nEnter/Return to continue')

    def _play_again(self):
        print(f'So {self._human.name}, do you want to play again? (y/n)')
        restart = input().lower()

        while restart not in ('y', 'n', 'yes', 'no'):
            print("I didn't understand. Would you like to play again? (y/n)")
            restart = input().lower()

        return restart in ('y', 'yes')

    def play(self):
        self._display_welcome_message()

        while True:
            self._score.display_scoreboard()
            self._human.choose()
            self._cpu.choose()
            self._display_winner()
            self._score.display_scoreboard()
            # possible helper needed for game end
            if self._score.human == 5:
                print(f"You scored 5 points! You win the game, {self._human.name}!")
                if self._play_again():
                    self._cpu = Computer(self)
                    self._score = Score(self)
                    self.move_history = {'human': [], 'cpu': []}
                else:
                    break
            elif self._score.cpu == 5:
                print(f"{self._cpu.name} was first to score 5 points.")
                print("What a dark day for humanity!")
                if self._play_again():
                    self._cpu = Computer(self)
                    self._score = Score(self)
                    self.move_history = {'human': [], 'cpu': [],}
                else:
                    break

        self._display_goodbye_message()

system('clear')
RPSGame().play()