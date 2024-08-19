"""
Dinosaur-themed Rock, Paper, Scissors game.
Includes "best of 5" gameplay, flavor text, single-button inputs,
basic sound (with randomization to avoid monotony), and
a couple ASCII graphics. Sound and music credits in README.
Fully Pylint compliant.
"""
import os
import json
import random
import cowsay
import pygame

pygame.mixer.init()

with open('rps_messages.json', 'r', encoding='utf-8') as file:
    OUTPUT = json.load(file)

VALID_CHOICES = {'1': 'Raptor', '2': 'Pterodactyl', '3': 'Stegosaurus'}
SFX = [pygame.mixer.Sound(f"dinosaur-{i}.mp3") for i in range(1, 5)]
MUSIC = pygame.mixer.music.load("music-21217.mp3")
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BOLD = '\033[1m'
RESET = '\033[0m'

def prompt(message):
    """
    Output formatter.
    """
    print(f"🦕 {message} 🦖")

def messages(outer_key, inner_key):
    """
    Accesses and returns message value from OUTPUT dictionary.
    For now, only battle_text is in json, but formatted so that
    other text could be moved if desired.
    """
    return OUTPUT[outer_key][inner_key]

def startup():
    os.system('clear')
    pygame.mixer.music.play(loops = -1)
    cowsay.trex(f'{YELLOW}Welcome to Raptor, Pterodactyl, Stegosaurus!{RESET}') # pylint: disable=E1101
                            # Pylint muffled, Cowsay does have trex member ^
    prompt('A dino-themed "Rock, Paper, Scissors" battle')
    prompt('Score 3 wins to be crowned ruler of the dinosaurs!')

def get_player_choice():
    """
    Prompt user for choice and returns choice.
    """
    prompt(f'Use {BOLD}1, 2, or 3{RESET} to choose your champion!')
    choice = input('(1) Raptor \n(2) Pterodactyl \n(3) Stegosaurus\n')

    while choice not in VALID_CHOICES:
        prompt(f'{YELLOW}Dino discrepancy!{RESET}')
        return get_player_choice()

    return VALID_CHOICES[choice]

def get_computer_choice():
    """
    Randomly assign and return computer choice.
    """
    return VALID_CHOICES[random.choice(list(VALID_CHOICES.keys()))]

def roar():
    """
    Play sound effect at round start.
    """
    random.choice(SFX).play()

def battle_text(player_, opponent_):
    """
    Fight description for fun. Strings extracted to json
    due to length.
    """
    match (player_, opponent_):
        case ('Raptor', 'Stegosaurus') | ('Stegosaurus', 'Raptor'):
            prompt(messages('battle_text', 'r_vs_s'))
        case ('Stegosaurus', 'Pterodactyl') | ('Pterodactyl', 'Stegosaurus'):
            prompt(messages('battle_text', 'p_vs_s'))
        case ('Pterodactyl', 'Raptor') | ('Raptor', 'Pterodactyl'):
            prompt(messages('battle_text', 'r_vs_p'))
        case _:
            prompt(messages('battle_text', 'tie'))


def determine_round_result(player, opponent):
    """
    Compares choices to determine and return winner.
    """
    battle_text(player, opponent)

    winning_pairs = (
        ('Raptor', 'Stegosaurus'),
        ('Pterodactyl', 'Raptor'),
        ('Stegosaurus', 'Pterodactyl')
    )

    if (player, opponent) in winning_pairs:
        return 'player'

    if player == opponent:
        return None

    return 'opponent'

def display_winner(winner1):
    """
    Print round winner. Input statement to allow user
    to read at own pace.
    """
    round_over = {
        'player': f'{GREEN}You are victorious!{RESET}',
        'opponent': f'{RED}Your opponent is victorious!{RESET}',
        None: f'{YELLOW}A fierce battle ensues,'
         f' but neither combatant emerges victorious.{RESET}'
    }

    prompt(round_over[winner1])
    input(f'\n{BOLD}Enter/Return{RESET} to continue')

def score_keeper(winner2):
    """
    Updates score after each round.
    """
    if winner2 == 'player':
        score[0] += 1
    elif winner2 == 'opponent':
        score[1] += 1

def score_board(winner1):
    """
    Display score on ASCII art score board.
    Clears screen to keep scoreboard at top.
    """
    os.system('clear')
    score_keeper(winner1)
    print(f"""         |                 |
        =X=================X=
         |Your score:     {BOLD}{score[0]}{RESET}| 
         |Opponent score: {BOLD}{score[1]}{RESET}| 
        =X=================X=
         |                 | """)

def display_result(score_):
    """
    Displays final outcome upon 3 rounds won or lost.
    Graphic only shown if player wins. The "good ending".
    """
    roar()  # Additional roar on completion
    if score_[0] == 3:
        cowsay.trex(f'''{GREEN}Congratulations, conqueror!
                     You are our new leige!{RESET}''') # pylint: disable=E1101
    elif score[1] == 3:
        prompt(f'{RED}You have not proven yourself worthy.'
               f' You must try again!{RESET}')

def another_battle():
    """
    Prompts the user to play again or not.
    """
    prompt('Will you fight again? (y/n)')
    restart = input().lower()

    while restart not in ('y', 'n', 'yes', 'no'):
        prompt('You cannot be heard over the roaring beasts. Speak up! (y/n)')
        restart = input().lower()

    if restart in ('n', 'no'):
        prompt('Farewell, dino warrior!')
        return False

    return restart in ('y', 'yes')

# Start
startup()
score = [0, 0]  # Initialize score at global scope

while True:
    player_choice = get_player_choice()
    prompt(f'You have chosen {player_choice}!')

    computer_choice = get_computer_choice()
    prompt(f'Your opponent chooses {computer_choice}!')
    print()     # Blank line to break up output

    roar()
    pygame.time.delay(1000)     # Suspense! ;)

    winner = determine_round_result(player_choice, computer_choice)  # pylint: disable=C0103
    # ^ Pylint muffled because winner is not a constant. Should it be?
    pygame.time.delay(1000)
    display_winner(winner)
    score_board(winner)

    if (score[0] != 3) and (score[1] != 3):
        continue

    display_result(score)
    score = [0, 0]

    if not another_battle():
        break
