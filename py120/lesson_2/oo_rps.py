class Player:
    def __init__(self, player_type):
        self._player_type = player_type.lower()

    def choose(self):
        pass

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