"""
Dinosaur-themed Rock, Paper, Scissors game.
Includes "best of 5" gameplay, flavor text, single-button inputs,
basic sound (with randomization to avoid monotony), and
a single ASCII graphic. Fully Pylint compliant.
"""
import os
import random
import cowsay
import pygame

pygame.mixer.init()

VALID_CHOICES = {'1': 'Raptor', '2': 'Pterodactyl', '3': 'Stegosaurus'}
SFX = [pygame.mixer.Sound("dinosaur-4.mp3"),
       pygame.mixer.Sound("dinosaur-growl.mp3"),
       pygame.mixer.Sound("dinosaur-roar-with-growls.mp3"),
       pygame.mixer.Sound("dinosaur.mp3"),]
MUSIC = pygame.mixer.music.load("music-21217.mp3")

def prompt(message):
    """
    Output formatter.
    """
    print(f"=> {message} <=")

def get_player_choice():
    """
    Prompt user for choice and returns choice.
    """
    prompt("Use 1, 2, or 3 to choose your monstrous lizard!")
    choice = input('(1) Raptor \n(2) Pterodactyl \n(3) Stegosaurus\n')

    while choice not in VALID_CHOICES:
        prompt('Dino discrepancy!')
        return get_player_choice()

    return VALID_CHOICES[choice]

def get_computer_choice():
    """
    Randomly assign and return computer choice.
    """
    return VALID_CHOICES[random.choice(list(VALID_CHOICES.keys()))]

def flavor_text(choice1, choice2):
    """
    Fight description for fun.
    """
    match (choice1, choice2):
        case ('Raptor', 'Stegosaurus'):
            prompt("The raptor charges in fast and low!"
                " The slow stegosaurus can't react quickly"
                 " enough to defend against the onslaught.")
        case ('Stegosaurus', 'Raptor'):
            prompt("The raptor charges in fast and low!"
                " The slow stegosaurus can't react quickly"
                 " enough to defend against the onslaught.")
        case ('Stegosaurus', 'Pterodactyl'):
            prompt("The pterodactyl swoops down, but can't"
                   " pierce the stegosaurus' armored hide."
                " The stegosaurus swings its tail and knocks"
                " the pterodactyl to the ground!")
        case ('Pterodactyl', 'Stegosaurus'):
            prompt("The pterodactyl swoops down, but can't"
                   " pierce the stegosaurus' armored hide."
                " The stegosaurus swings its tail and knocks"
                " the pterodactyl to the ground!")
        case ('Pterodactyl', 'Raptor'):
            prompt("The raptor rushes in, but the winged"
                   " pterodactyl takes flight."
                " With the raptor exhausted, the pterodactyl"
                " swoops in for the kill!")
        case ('Raptor', 'Pterodactyl'):
            prompt("The raptor rushes in, but the winged"
                   " pterodactyl takes flight."
                " With the raptor exhausted, the pterodactyl"
                " swoops in for the kill!")
        case _:
            prompt("The terrible creatures roar and bellow at one another. ")


def do_battle(player, opponent):
    """
    Compares choices to determine and return winner.
    Includes call to flavor_text() for fun.
    """
    flavor_text(player, opponent)

    winning_pairs = (
        ('Raptor', 'Stegosaurus'),
        ('Pterodactyl', 'Raptor'),
        ('Stegosaurus', 'Pterodactyl')
    )

    if (player, opponent) in winning_pairs:
        return 'You are'

    if player == opponent:
        return 'A fierce battle ensues, but neither combatant emerges'

    return 'Your opponent is'

def score_board(winner1):
    """
    Display score.
    """

    score_keeper(winner1)
    prompt(f'Your score: {score[0]} \n Opponent score: {score[1]}')

def score_keeper(winner2):
    if winner2 == 'You are':
        score[0] += 1
    elif winner2 == 'Your opponent is':
        score[1] += 1

def final_score(score_):

    if score_[0] == 3:
        cowsay.trex('Congratulations, champion! You are our new leige!') # pylint: disable=E1101
    elif score[1] == 3:
        prompt('You have not proven yourself worthy. You must try again!')

def another_battle():
    """
    Prompts the user to play again or not.
    """
    prompt('Another battle? (y/n)')
    restart = input()

    while restart and restart.lower() not in ('y', 'n', 'yes', 'no'):
        prompt('You cannot be heard over the roaring beasts. Speak up! (y/n)')
        restart = input()

    if restart and restart.lower() in ('n', 'no'):
        prompt('Farewell, dino warrior!')
        return False

    if restart and restart[0].lower() in ('y', 'yes'):
        return True

    return False

# Start
os.system('clear')
pygame.mixer.music.play(loops = -1)
score = [0, 0]
cowsay.trex('Welcome to Raptor, Pterodactyl, Stegosaurus!') # pylint: disable=E1101
prompt('A dino-themed "Rock, Paper, Scissors" game')
prompt('Score 3 wins to be crowned ruler of the dinosaurs!')

while True:
    player_choice = get_player_choice()
    prompt(f'You have chosen {player_choice}!')

    computer_choice = get_computer_choice()
    prompt(f'Your opponent chooses {computer_choice}!')

    input('Press a key to fight!')
    battle_sound = random.choice(SFX)
    battle_sound.play()
    pygame.time.delay(1800)

    winner = do_battle(player_choice, computer_choice)      # pylint: disable=C0103

    prompt(f'{winner} victorious!')
    score_board(winner)

    if (score[0] != 3) and (score[1] != 3):
        continue

    final_score(score)
    score = [0, 0]

    if not another_battle():
        break
