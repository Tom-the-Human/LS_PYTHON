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
#   - use set.pop() to remove cards from deck and add same to player hand
#   - definitely display hands, player and dealer
#   - display hand values
# 3 Ask player to hit or stay
#   - if hit, deal player another card
#       - display hand with new card
#       - ask again to hit or stay, repeat until stay or bust
#       - if bust, player loses
#   - if stay, stop asking
# 4 Dealer turn
#   - if dealer hand > 16 hit, else stay
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
import random

BLACK_ON_WHITE = '\033[0;30;47m'
RED_ON_WHITE = '\033[0;31;47m'
RED = '\033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'
BOW = BLACK_ON_WHITE
ROW = RED_ON_WHITE

def prompt(message):
    print(f'♣️♠️🃏♦️♥️ {message}')

def shuffle(deck):
    random.shuffle(deck)

def hit():
    pass # get a card

def dealer_turn(dealer_hand):
    while dealer_hand < 17:
        prompt('The dealer takes a card.')
        hit()

def player_turn():
    while True:
        player_choice = input('hit or stay')
        if (player_choice == 'stay') or busted():
            break

    if busted():
        pass # loss, maybe ask to replay, lose chips if implemented
    else:
        prompt('You chose to stay!')

