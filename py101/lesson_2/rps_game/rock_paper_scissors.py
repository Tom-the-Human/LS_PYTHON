'''
Dinosaur-themed RPS.
1    If player a chooses rock and player b chooses scissors, player a wins.
2    If player a chooses paper and player b chooses rock, player a wins.
3    If player a chooses scissors and player b chooses paper, player a wins.
4    If both players choose the same item, neither player wins. It's a tie.

Our version of the game lets the user play against the computer.
The game flow should go like this:

1    The user makes a choice.
2    The computer makes a choice.
3    The winner is displayed.
'''

import os
import random
import cowsay

VALID_CHOICES = {'1': 'Raptor', '2': 'Pterodactyl', '3': 'Stegosaurus'}

def prompt(message):
    """
    Output formatter.
    """
    print(f"=> {message} <=")

def get_player_choice():
    '''Prompt user for choice and returns choice.'''
    prompt("Use 1, 2, or 3 to choose your monstrous lizard!")
    choice = input('(1) Raptor \n(2) Pterodactyl \n(3) Stegosaurus\n')

    while choice not in VALID_CHOICES:
        prompt('Dino discrepancy!')
        return get_player_choice()

    return VALID_CHOICES[choice]

def get_computer_choice():
    '''Randomly assign and return computer choice.'''
    return VALID_CHOICES[random.choice(list(VALID_CHOICES.keys()))]

def flavor_text(choice1, choice2):
    '''Fight description for fun.'''
    match (choice1, choice2):
        case ('Raptor', 'Stegosaurus'):
            prompt("The raptor charges in fast and low!"
                " The slow stegosaurus can't react quickly enough to defend against the onslaught.")
        case ('Stegosaurus', 'Raptor'):
            prompt("The raptor charges in fast and low!"
                " The slow stegosaurus can't react quickly enough to defend against the onslaught.")
        case ('Stegosaurus', 'Pterodactyl'):
            prompt("The pterodactyl swoops down, but can't pierce the stegosaurus' armored hide."
                " The stegosaurus swings its tail and knocks the pterodactyl to the ground!")
        case ('Pterodactyl', 'Stegosaurus'):
            prompt("The pterodactyl swoops down, but can't pierce the stegosaurus' armored hide."
                " The stegosaurus swings its tail and knocks the pterodactyl to the ground!")
        case ('Pterodactyl', 'Raptor'):
            prompt("The raptor rushes in, but the winged pterodactyl takes flight."
                " With the raptor exhausted, the pterodactyl swoops in for the kill!")
        case ('Raptor', 'Pterodactyl'):
            prompt("The raptor rushes in, but the winged pterodactyl takes flight."
                " With the raptor exhausted, the pterodactyl swoops in for the kill!")
        case _:
            prompt("The terrible creatures roar and bellow at one another. ")


def do_battle(player, opponent):
    '''Compares choices to determine and return winner.
    Includes call to flavor_text() for fun.'''

    flavor_text(player, opponent)

    if ((player == 'Raptor' and opponent == 'Stegosaurus') or
        (player == 'Pterodactyl' and opponent == 'Raptor') or
        (player == 'Stegosaurus' and opponent == 'Pterodactyl')):
        return 'You are'

    if player == opponent:
        return 'A fierce battle ensues, but neither combatant emerges'

    return 'Your opponent is'

def another_battle():
    '''Prompts the user to play again or not.'''
    prompt('Well faught! Another battle? (y/n)')
    restart = input()

    while restart and restart[0].lower() not in ('y', 'n'):
        prompt('You cannot be heard over the roaring beasts. Speak up! (y/n)')
        restart = input()

    if restart and restart[0].lower() == 'n':
        prompt('Farewell, dino warrior!')
        return False

    return True

#Start
os.system('clear')
cowsay.trex('Welcome to Raptor, Pterodactyl, Stegosaurus!') # pylint: disable=E1101
prompt('A dino-themed "Rock, Paper, Scissors" game')

while True:
    player_choice = get_player_choice()
    prompt(f'You have chosen {player_choice}!')

    computer_choice = get_computer_choice()
    prompt(f'Your opponent chooses {computer_choice}!')

    input('Press a key to fight!')
    winner = do_battle(player_choice, computer_choice)      # pylint: disable=C0103

    prompt(f'{winner} victorious!')

    if not another_battle():
        break
