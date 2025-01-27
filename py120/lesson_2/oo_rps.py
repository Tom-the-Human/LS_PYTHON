import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        # implement name?
        self._player_type = player_type.lower()
        self.move = None

    def _is_human(self):
        return self._player_type == 'human'
    
    def choose(self):
        if self._is_human():
            self.move = self._human_choice()
            #human choose move
        else:
            #cpu chooses move
            self.move = random.choice(Player.CHOICES)

    def _human_choice(): #FIXME imported from other RPS, needs more tailoring
        """
        Prompt user for choice and returns choice.
        """
        while True:
            prompt(f'Use {BOLD}1, 2, or 3{RESET} to choose your move!\n'
                f'(Or use {BOLD}(R){RESET} to read the rules)')
            choice = input('(1) Rock\n(2) Paper\n'
                        '(3) Scissors\n(R) Rules\n')
            choice = choice.strip().lower()

            if choice == 'r':
                display_rules()
                continue  # Restart the loop after displaying rules

            if choice in Player.CHOICES:
                return Player.CHOICES.get(choice) #FIXME CHOICES not dictionary

            prompt(f'{YELLOW}Please pick a valid option!{RESET}')

class Move:
    def __init__(self):
        pass

class Rule:
    def __init__(self):
        pass

    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player("human")
        self._cpu = Player("cpu")

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("Thanks for playing! Goodbye!")

    def play(self):
        self._display_welcome_message()
        self._human.choose()
        self._cpu.choose()
        display_winner()
        self._display_goodbye_message()

RPSGame().play()