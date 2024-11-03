"""
Twenty-One game with some bonus features. Instead of a best-of-5 feature,
I planned to implement chips instead and elaborate on the spoopy/Twilight Zone
"flavor". I may implement these things later, but got it to a state that I
am happy with for now and feel that I need to keep moving forward. I deleted
the code and comments relating to chips, but left the flavor/atmosphere alone.
"""
import random
import os

BLACK_ON_WHITE = '\033[0;30;47m'
RED_ON_WHITE = '\033[0;31;47m'
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'
BOW = BLACK_ON_WHITE
ROW = RED_ON_WHITE
NOT_BUSTED = range(22)
DEALER_STAY = 17
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♣️', '♠️', '♦️', '♥️']
RED_SUITS = ['♦️', '♥️']

def prompt(message):
    print(f"♣️♠️'🃏'♦️♥️: {message}")

def wait():
    input("(Enter/Return)")

def welcome():
    os.system('clear')
    print("The gate opens. You step into a strange dimension.")
    wait()
    os.system('clear')
    input(f"""
******************************************************************************
*                                                                            *
*                                                                            *
*                          WELCOME TO HUMAN CA$INO                           *
*                                                                            *
*                    ╭──────────────────────────────────╮                    *
*                    │                                  │                    *
*                    │         ★ Human Ca$ino ★         │                    *
*                    │                                  │                    *
*                    ╰──────────────────────────────────╯                    *
*                                                                            *
*                                                                            *
*                          ╭───────────────────────╮                         *
*                         ╱                         ╲                        *
*                        ╱   .---.    .---.          ╲                       *
*                       ╱   (  @  )  (  @  )          ╲                      *
*                      │      `-'      `-'            │                      *
*                      │                              │                      *
*                      │      ╔════════════╗          │                      *
*                      │      ║  PLAY NOW  ║          │                      *
*                      │      ╚V^^^^^^^^^^V╝          │                      *
*                       ╲_____________________________/                      *
*                                                                            *
*               The casino hums with a strange, electric energy...           *
*                                                                            *
*       Shadows flicker on the walls, where eerie portraits seem to watch    *
*        your every move. The air is thick with mystery and anticipation.    *
*                                                                            *
*                         What are you waiting for?                          *
*                                                                            *
*                      PRESS ENTER TO BEGIN PLAYING                          *
*                                                                            *
******************************************************************************

    """)
    print("A small piece of paper depicting a jester flits into view.")
    prompt("Welcome to Human Casino, traveler! It's time to play some 21!")
    prompt("I am your host, friend, fiend, and dealer. I'd tell you my name"
           " if only I could remember it.")
    prompt("For now, just call me Dealer. Well, let's get to it!")
    wait()

def shuffle(deck):
    random.shuffle(deck)

def deal(deck):
    '''
    Deals the hands, alternating between player and dealer the way cards
    are supposed to be dealt. Use `hit` for additional cards.
    '''
    player_hand = []
    dealer_hand = []
    
    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    
    return player_hand, dealer_hand

def hit(hand, deck):
    '''
    Deals a single card during play. Use `deal` when starting the game.
    '''
    hand.append(deck.pop())

def one_or_eleven(hand_value):
    twenty_one_minus_eleven = 10
    if hand_value > twenty_one_minus_eleven:
        return 1
    else:
        return 11

def hand_total(hand):
    '''
    Calculate and return the hand value.
    '''
    hand_value = 0
    for card in hand:
        try:
            hand_value += int(card[0])
        except ValueError:
            if card[0] != 'A':
                hand_value += 10
            if card[0] == 'A':
                hand_value += one_or_eleven(hand_value)

    return hand_value
        

def busted(hand):
    if hand_total(hand) not in NOT_BUSTED:
        return True
    
    return False

def who_won(player_hand, dealer_hand):
    winner = None
    if (hand_total(player_hand) > hand_total(dealer_hand) \
        and not busted(player_hand)) or busted(dealer_hand):
        winner = 'player'
    elif (hand_total(dealer_hand) > hand_total(player_hand) \
        and not busted(dealer_hand)) or busted(player_hand):
        winner = 'dealer'
    
    return winner

def display_result(player_hand, dealer_hand, winner):
    prompt(f"You have {hand_total(player_hand)}.")
    prompt(f"I have {hand_total(dealer_hand)}.")
    if winner == 'player':
        prompt("Hmm ... looks like you beat me this time.")
    elif winner == 'dealer':
        prompt("Dealer wins! Everything you've wagered is mine!")
    else:
        prompt("A tie. How dull! New hand! New hand, I say!")

def color_card(suit):
    """Return the card face in the appropriate color based on suit."""
    if suit in RED_SUITS:
        color = ROW
    else:
        color = BOW

    return color

def display_hand(hand):
    card_top = "╭──────╮"
    card_upper = "│{}     │"
    card_middle_10 = "│  {}  │"
    card_middle_other = "│  {}   │"
    card_lower = "│     {}│"
    card_bottom = "╰──────╯"

    face_down_middle = f"{BOW}│▒▒▒▒▒▒│{RESET}" # Card back always BOW

    if len(hand) == 1:
        hand.append(['▒', '▒']) # Dealer hole card

    top_row = "   ".join([color_card(card[1]) +
                           card_top + RESET for card in hand])
    upper_row = "   ".join([
        color_card(card[1]) + card_upper.format(card[1]) +
          RESET if card[1] != '▒' else face_down_middle for card in hand
    ])
    middle_row = "   ".join([
        color_card(card[1]) + card_middle_10.format(card[0]) +
          RESET if card[0] == '10'
        else color_card(card[1]) +
          card_middle_other.format(card[0]) + RESET if card[0] != '▒'
        else face_down_middle for card in hand
    ])
    lower_row = "   ".join([
        color_card(card[1]) + card_lower.format(card[1]) +
          RESET if card[1] != '▒' else face_down_middle for card in hand
    ])
    bottom_row = "   ".join([color_card(card[1]) +
                              card_bottom + RESET for card in hand])

    print(top_row)
    print(upper_row)
    print(middle_row)
    print(lower_row)
    print(bottom_row)

def display_game(player_hand, dealer_hand):
    os.system('clear')
    
    print("┌──────────────────────────────────────────────────────────────┐")
    print(f"│                     {BOLD}~ Human Blackjack ~{RESET}" +
          "                      │")
    print("└──────────────────────────────────────────────────────────────┘")
    print(f"      {BOLD}Dealer Hand                 " +
          f"Dealer Showing: {hand_total(dealer_hand)}{RESET}")
    display_hand(dealer_hand)
    print(" ")
    print(f"        {GREEN}Player Hand               " +
          f"Player Total: {hand_total(player_hand)}{RESET}")
    display_hand(player_hand)

def display_rules():
    prompt("""
            The goal of 21 is to get as close to 21 as possible without
            going over. Going over 21 is called going bust, and it means
            you automatically lose. The player and dealer are each dealt
            two cards. Both player cards are face up, and the dealer has
            one card face up and one face down (the hole card). Numbered
            cards are worth their number value, face cards (King, Queen,
            and Jack) are worth 10, and A (Ace) is worth either 1 or 11.
            Ace is worth 11 unless that would cause the hand to bust (go
            over 21), in which case it is worth 1. After cards are dealt,
            the player may hit (take another card) or stay (end the turn).
            The player may hit as many times as they like before staying
            or busting.
           """)

def play_again():
    prompt("How about another round?")
    answer = input('"Yes" to continue, "No" to quit.\n').strip().lower()
    while answer not in ['yes', 'y', 'no', 'n']:
        prompt("Oh, come now! Wouldn't you like another chance?")
        answer = input('"Yes" to continue, "No" to quit.\n').strip().lower()

    if answer in ['yes', 'y']:
        return True
    
    return False

def dealer_turn(player_hand, dealer_hand, deck):
    display_game(player_hand, dealer_hand)
    while hand_total(dealer_hand) < DEALER_STAY:
        prompt('The dealer takes a card.')
        hit(dealer_hand, deck)
        display_game(player_hand, dealer_hand)

    if busted(dealer_hand):
        prompt("Damnation! Dealer goes bust.")
    else:
        prompt("Dealer stays.")
        

def player_turn(player_hand, dealer_hand, deck):
    while True:
        display_game(player_hand, [dealer_hand[0]]) 
        # display only one dealer card before dealer turn ^
        prompt('Enter "1" to hit, "2" to stay, "3" to see the rules.')
        player_choice = input().strip()

        while player_choice not in ['1', '2', '3']:
            prompt("Come on, be a sport! Pick 1, 2, or 3.")
            prompt('Enter "1" to hit, "2" to stay, "3" to see the rules.')
            player_choice = input().strip()

        if player_choice == '1':
            print('"Hit me!"')
            hit(player_hand, deck)
        if (player_choice == '2') or busted(player_hand):
            break
        if player_choice == '3':
            display_rules()
        wait()


    if busted(player_hand):
        prompt("Busted!")
    else:
        prompt('You chose to stay!')

def play_hand(deck):
    shuffle(deck)
    player_hand, dealer_hand = deal(deck)

    player_turn(player_hand, dealer_hand, deck)
    if busted(player_hand):
        winner = who_won(player_hand, dealer_hand)
        display_result(player_hand, dealer_hand, winner)
        return

    dealer_turn(player_hand, dealer_hand, deck)

    winner = who_won(player_hand, dealer_hand)
    display_result(player_hand, dealer_hand, winner)

def main():
    welcome()
    while True:
        player_hand, dealer_hand = [], []
        deck = [
            [value, suit] for value in VALUES for suit in SUITS
        ]

        play_hand(deck)

        if not play_again():
            break

main()
