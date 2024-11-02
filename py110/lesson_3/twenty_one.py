# P
# 1 Init deck
# 2 Deal cards to player + dealer
# 3 Player turn - hit or stay
#   repeat until bust or stay
# 4 If player bust, dealer wins
# 5 Dealer turn - hit or stay
#   repeat until total >= 17
# 6 if dealer bust, player wins
# 7 compare cards and declare winner

# Examples
# Possible play representation
# Dealer : +-----+ +-----+
#          |K    | |:::::|  Showing: 10
#          |♠️   ♠️| |:::::|
#          |    K| |:::::|  Dealer Stays
#          +-----+ +-----+
#
#
# Player:  +-----+ +-----+
#          |9    | |A    |
#          |  ♦️  | |  ♣️  |
#          |    9| |    A|
#          +-----+ +-----+
#
#           Total: 20
#           Player Stays
#
# This could require some fancy formatting. Maybe I store the names of the
# cards as dict keys with the ASCII art as the values, i.e.
# ... actually deck = {d_9: [9, ♦️]} could work well if I follow the 
# formatting in the Tic Tac Toe game, and do something like 
# def display_card(deck[card]):
#   print('+----+')
#   print(f'|{deck[card][0]}    |')
#   print(f'|  {deck[card][1]}  |')
#   print(f'|    {deck[card][0]}|')
#   print('+----+')
#
# Seems like it could be tricky to figure out how to get it all to display
# correctly in the terminal. Needs to be modular for 2 cards up to 5 or more.
# Will need to use dicts to rep the player and dealer hands, and then can
# print cards * length of dict i.e. 
# edge = '+-----+ '
# card_top = f'|{deck[card][0]}    | '
# card_mid = f'|  {deck[card][1]}  | '
# card_low = f'|    {deck[card][0]}| '
# --card = f'{edge}\ncard--
# print(edge * len(hand))
# print(card_top for card in hand)
# print(card_mid for card in hand)
# print(card_bot for card in hand)
# print(edge * len(hand))
#
# Maybe that is all contained in a display_hand function.
#
# Getting the total of a hand can be along the lines of 
# total += hand[card][0] for cards in hand, or hopefully just sum(hand).
#
# Oooh, maybe instead of ASCII lines I can use codes for white backgrounds
# black or red text on cards as befitting the suit.

# D
# I was pretty set on using dicts for the deck and hands with list values for 
# the card values, but I see LS recommends nested lists. Maybe that's better -
# Since cards are drawn randomly, we really have no need of keys. Actually,
# maybe a set of lists for the deck is even better since the deck is meant to
# be randomly shuffled anyway. So a set of lists for the deck and lists of
# lists for the hands (since hands should retain order).

# A
# 1 Welcome and set up
#   - clear screen
#   - welcome message
#   - initialize deck
# 2 Start a round
#   - display deck?
#   - deal animation?
#   - shuffle and remove cards from deck and add same to player hand
#   - definitely display hands, player and dealer
#   - display hand values
#   - use chips (maybe), to control game length
# 3 Ask player to hit or stay
#   - if hit, deal player another card
#       - display hand with new card
#       - ask again to hit or stay, repeat until stay or bust
#       - if bust, player loses
#   - if stay, stop asking
# 4 Dealer turn
#   - if dealer hand < 17 hit, else stay
#   - display hand with new card
#   - if bust, player wins
# 5 Compare hands
#   - if player total is higher than dealer total, player wins
#   - if hands are even and not bust, push (no win)
#   - else, dealer wins
# 6 Play again, but for how long? Should there be chips?
#   Or just ask player after each hand if they want to continue?
#
# Include math for Ace to equal 11 or 1, depending on hand total.
# Is 11 unless that makes hand bust 21, else 1

# C
"""
Get it working without chips, but keep the 'chips feature' in mind. 
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
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♣️', '♠️', '♦️', '♥️']
RED_SUITS = ['♦️', '♥️']

def prompt(message):
    print(f'♣️♠️~🃏~♦️♥️ {message}')

def wait():
    input("(Enter/Return)")

def welcome():
    os.system('clear')
    print("The gate opens. You step into a strange dimension.")
    wait()
    os.system('clear')
    input(f"""
********************************************************************************
*                                                                              *
*                                                                              *
*                           WELCOME TO HUMAN CA$INO                            *
*                                                                              *
*                     {BOW}╭──────────────────────────────────╮{RESET}                     *
*                     {BOW}│                                  │{RESET}                     *
*                     {BOW}│         ★ Human Casino ★         │{RESET}                     *
*                     {BOW}│                                  │{RESET}                     *
*                     {BOW}╰──────────────────────────────────╯{RESET}                     *
*                                                                              *
*                                                                              *
*                           ╭───────────────────────╮                          *
*                          ╱                         ╲                         *
*                         ╱   .---.    .---.          ╲                        *
*                        ╱   (  @  )  (  @  )          ╲                       *
*                       │      `-'      `-'            │                       *
*                       │                              │                       *
*                       │      ╔════════════╗          │                       *
*                       │      ║  PLAY NOW  ║          │                       *
*                       │      ╚V^^^^^^^^^^V╝          │                       *
*                        ╲_____________________________/                       *
*                                                                              *
*                The casino hums with a strange, electric energy...            *
*                                                                              *
*        Shadows flicker on the walls, where eerie portraits seem to watch     *
*         your every move. The air is thick with mystery and anticipation.     *
*                                                                              *
*                          What are you waiting for?                           *
*                                                                              *
*                       PRESS ENTER TO BEGIN PLAYING                           *
*                                                                              *
********************************************************************************

    """)
    print("A small piece of paper depicting a jester flits into view.")
    prompt("Welcome to Human Casino, traveler! It's time to play some 21!")
    prompt("I am your host, friend, fiend, and dealer. I'd tell you my name"
           " if only I could remember it.")
    prompt("For now, just call me Dealer. Well, let's get to it!")
    wait()

def shuffle(deck):
    random.shuffle(deck)

def bet(chips):
    '''
    Chips not currently implemented, but would be used to lengthen game.
    Winning all the dealer's chips would reward a good ending (i.e. dealer
    reveals who he is, or just turns into a regular joker card or something).
    Losing all chips would give a bad ending, (i.e. lose soul or have to
    stay in this weird place forever or something else Twilight Zone-y).
    '''
    prompt(f"You have {chips} in chips.")
    prompt("How much will you bet?")
    # offer options, from $5 to $100, move chips from the player stack
    # to the pot. bets pay 1:1, (i.e. winning a 5 chip bet gets your 5
    # chips back plus 5 more from the dealer

def deal(deck):
    '''
    Deals the hands. Use `hit` for additional cards.
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
    if hand_value > 10:
        return 1
    else:
        return 11

def calc_hand_total(hand):
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
    if calc_hand_total(hand) not in NOT_BUSTED:
        return True
    
    return False

def who_won(player_hand, dealer_hand):
    # show dealer hole card
    winner = None
    if (calc_hand_total(player_hand) > calc_hand_total(dealer_hand) \
        and not busted(player_hand)) or busted(dealer_hand):
        winner = 'player'
    elif (calc_hand_total(dealer_hand) > calc_hand_total(player_hand) \
        and not busted(dealer_hand)) or busted(player_hand):
        winner = 'dealer'
    
    return winner

def display_result(player_hand, dealer_hand, winner):
    prompt(f"You have {calc_hand_total(player_hand)}.")
    prompt(f"I have {calc_hand_total(dealer_hand)}.")
    if winner == 'player':
        prompt("Hmm ... looks like you beat me this time.")
    elif winner == 'dealer':
        prompt("Dealer wins! Everything you've wagered is now mine!")
    else:
        prompt("A tie. How dull! New hand! New hand, I say!")

def color_card_face(value, suit):
    """Return the card face in the appropriate color based on suit."""
    if suit in RED_SUITS:
        color = ROW
    else:
        color = BOW

    return color

def display_hand(hand):
    card_top = "╭───────╮"
    card_upper = "│{}      │"
    card_middle_10 = "│  {}   │"
    card_middle_other = "│   {}   │"
    card_lower = "│      {}│"
    card_bottom = "╰───────╯"

    face_down_top = "╭───────╮"
    face_down_middle = f"{BOW}│▒▒▒▒▒▒▒│{RESET}"
    face_down_bottom = "╰───────╯"

    if len(hand) == 1:
        hand.append(['▒', '▒']) # dealer hole card

    top_row = "   ".join([color_card_face(card[0], card[1]) + card_top + RESET for card in hand])
    upper_row = "   ".join([
        color_card_face(card[0], card[1]) + card_upper.format(card[1]) + RESET if card[1] != '▒' else face_down_middle for card in hand
    ])
    middle_row = "   ".join([
        color_card_face(card[0], card[1]) + card_middle_10.format(card[0]) + RESET if card[0] == '10'
        else color_card_face(card[0], card[1]) + card_middle_other.format(card[0]) + RESET if card[0] != '▒'
        else face_down_middle for card in hand
    ])
    lower_row = "   ".join([
        color_card_face(card[0], card[1]) + card_lower.format(card[1]) + RESET if card[1] != '▒' else face_down_middle for card in hand
    ])
    bottom_row = "   ".join([color_card_face(card[0], card[1]) + card_bottom + RESET for card in hand])

    print(top_row)
    print(upper_row)
    print(middle_row)
    print(lower_row)
    print(bottom_row)

def display_game(player_hand, dealer_hand):
    # string representation of cards, hand totals, maybe more
    # display card back for dealer hole card, add deck?
    os.system('clear')
    
    print("┌──────────────────────────────────────────────────────────────┐")
    print(f"│                     {BOLD}~ Human Blackjack ~{RESET}                      │")
    print("└──────────────────────────────────────────────────────────────┘")
    print(f"      {BOLD}Dealer Hand                 Dealer Showing: {calc_hand_total(dealer_hand)}{RESET}")
    display_hand(dealer_hand)
    print(" ")
    print(f"        {GREEN}Player Hand               Player Total: {calc_hand_total(player_hand)}{RESET}")
    display_hand(player_hand)

def display_rules():
    pass # print simple rules for the game
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
    # `if chips:` check when chips implemented
    # when chips implemented, probably need to change logic
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
    while calc_hand_total(dealer_hand) < 17:
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
        prompt("Busted!") # I'll be taking those chips now.")
    else:
        prompt('You chose to stay!')

def play_hand(deck):
    # bet()
    player_hand, dealer_hand = deal(deck)
    player_turn(player_hand, dealer_hand, deck)#, chips)
    if busted(player_hand):
        winner = who_won(player_hand, dealer_hand)
        display_result(player_hand, dealer_hand, winner)
        return

    dealer_turn(player_hand, dealer_hand, deck)#, chips)
    winner = who_won(player_hand, dealer_hand)
    display_result(player_hand, dealer_hand, winner)

def main():
    welcome()
    # player_chips = 100
    # dealer_chips = 100
    while True:
        # pot = 0
        player_hand, dealer_hand = [], []
        deck = [
            [value, suit] for value in VALUES for suit in SUITS
        ]

        shuffle(deck)

        play_hand(deck)

        if not play_again():
            break

main()
