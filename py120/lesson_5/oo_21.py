"""
P
Card game w dealer and player (participants)
Participants try to get as close to 21 points as possible without going over
Uses a deck of 52 card with 4 suits of 13 ranks each
Each participant is dealt 2 cards:
-   the dealer has a hidden "hole" card that is played face-down
-   player can see both cards in his hand
        (and I think other players' hands, if there are other players)

Player goes first, and can hit or stand
-   if player hits, gets another card, and can hit again or stand
-   if player's hand value exceeds 21, she busts (loses)
-   if player stands, it's the dealers turn to play

If player didn't bust, dealer plays next
-   dealer reveals his hole card
-   if dealer's points are < 17, must hit until points >= 17
-   if dealer's hand value goes over 21, he busts
-   if dealer's hand value >= 17, must stand

Winner is determined by comparing hands:
-   the participant closest to 21 (inclusive) without going over wins

Numbered cards are worth face value
Face cards are worth 10
Ace is worth 11 unless that would cause a bust, in which case Ace is worth 1

Nouns
[game, player, dealer, participant, turn, deck, hand,
    card, suit, rank, score, points, hole card, chips, ]

Verbs
[start, deal, hit, stand, bust, win, lose, tie, hide, reveal, compare, bet, ]

Game
-   start

Deck
-   deal (maybe, probably should be in dealer)

Card
Rank
Suit

Participant
-   hit
-   stand
-   bust (state)
-   Score (state)
Player
Dealer
-   deal (probably, but maybe in deck)

Additional Requirements
-   Welcome the player to the game, and say good bye when they quit.

-   Each time the player has an opportunity to hit or stay:

    Display the computer's hand; one card should remain hidden.
    Display the player's hand and her point total.

    For the dealer's turn:
-   The dealer doesn't play at all if the player busts.
-   Display the dealer's hand, including the hidden card, 
    and report his point total.
-   Redisplay the dealer's hand and point total and each time he hits.
-   Display the results when the dealer stays.
-   After each game is over, ask the player if they want to play again. 
    Start a new game if they say yes, else end the game.

-   When the program starts, give the player 5 dollars with which to bet. 
    Deduct 1 dollar each time she loses, and add 1 dollar each time she wins. 
    The program should quit when she is broke (0 dollars) or rich (has a 
    total of 10 dollars). (I'll probably call these chips.)

-   Be prepared to run out of cards. You can either create a new deck for each
    game, or keep track of how many cards remain
    and create a new deck as needed.
"""
import random
from os import system

BLACK_ON_WHITE = '\033[0;30;47m'
RED_ON_WHITE = '\033[0;31;47m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BOW = BLACK_ON_WHITE
ROW = RED_ON_WHITE

RED_SUITS = ['♦️', '♥️']

class Card:
    FACE_CARDS = 'JQK'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face = (rank, suit)

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['♣️', '♠️', '♦️', '♥️']

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Participant:
    def __init__(self):
        self._hand = []
        self._hand_value = 0

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    @property
    def hand_value(self):
        return self.calculate_hand_value(self.hand)

    def calculate_hand_value(self, hand):
        """
        Calculate highest valid value of hand accounting for aces.
        """
        value = 0

        for card in hand:
            try:
                value += int(card.rank)
            except ValueError:
                if card.rank in Card.FACE_CARDS:
                    value += 10
                if card.rank == 'A':
                    if (value + 11) < TwentyOneGame.BUSTED:
                        value += 11
                    else:
                        value += 1

        return value

    def hit(self):
        """Handles hitting (drawing an additional card). Currently relies on
        the game instance variable being named 'game'. Might be better to
        change this and avoid the dependency on the global variable."""
        if game.deck.cards:
            self.hand.append(game.deck.cards.pop(0))
        else:
            game.deck = Deck() # if deck is empty, open a new one
            self.hand.append(game.deck.cards.pop(0))

class Player(Participant):
    STARTING_CHIPS = 5
    # ^ this can be changed to alter the length/difficulty of the game

    def __init__(self):
        self.chips = Player.STARTING_CHIPS
        super().__init__()

    @property
    def chips(self):
        return self._chips

    @chips.setter
    def chips(self, chips):
        self._chips = chips

    def place_bet(self):
        """
        The player must bet a minimum of 1 chip up to a maximum of
        all owned chips in order to play each hand.
        """
        valid_bet = range(1, self.chips + 1)

        while True:
            print(f"You have {YELLOW}{self.chips}{RESET} chips.")
            print("How many chips will you bet on the next hand?")
            bet = (input(f"(1 - {self.chips}): ")).strip()
            try:
                bet = int(bet)
            except ValueError:
                print("That's not a valid bet.")
                continue

            if bet not in valid_bet:
                print("That's not a valid bet.")
                continue

            game.bet = bet
            self.chips -= bet
            break

class Dealer(Participant):
    STAND = 17
    def __init__(self):
        super().__init__()
        self._hole_revealed = False

    @property
    def hole_revealed(self):
        return self._hole_revealed

    def reveal_hole(self):
        """
        Reveals the hole card for the dealer's turn.
        """
        self._hole_revealed = True

    def hide_hole(self):
        """
        Hides the hole card for a new hand.
        """
        self._hole_revealed = False

    @property
    def hand_value(self):
        """
        Calculate displayed score based on whether hole card is shown.
        """
        if self._hole_revealed:
            return (self.calculate_hand_value(self.hand))

        return self.calculate_hand_value([self.hand[0]])

    def deal(self, player, dealer):
        """
        Deal two cards to the player
        and two to the dealer in alternating order.
        """
        if len(game.deck.cards) < 4:  # ensure there are enough cards
            game.deck = Deck()  # open new deck if needed

        for _ in range(2):
            player.hand.append(game.deck.cards.pop(0))
            dealer.hand.append(game.deck.cards.pop(0))

class TwentyOneGame:
    BUSTED = 22

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.winner = None
        self.bet = 0

    def start(self):
        """
        Main game driver.
        """
        self.display_welcome_message()

        while True:
            while self.player.chips > 0 \
            and self.player.chips < (2 * Player.STARTING_CHIPS):
                self.player.place_bet()
                self.dealer.deal(self.player, self.dealer)
                self.show_cards()
                self.player_turn()
                if self.winner: # In event of player bust
                    self.display_hand_result()
                    self.reset_for_next_hand()
                    continue
                self.dealer_turn()
                self.determine_winner()
                self.display_hand_result()
                self.reset_for_next_hand()

            self.display_game_result()
            if not self.play_again():
                break

            self.__init__()

        self.display_goodbye_message()

    def player_turn(self):
        """
        Ask player to hit or stand, or view rules. 
        If hitting or viewing rules, can hit again or stand, or view rules.
        If stand, player turn is over.
        """
        g = GREEN   # just to shorten a couple print lines
        while True:
            if self.bust(self.player.hand_value):
                self.winner = self.dealer
                self.show_cards()
                print(f"Bust! You went over {self.BUSTED - 1}.")
                break

            print(f"Your hand is worth {g}{self.player.hand_value}{RESET}.")
            print(f"Dealer is showing {RED}{self.dealer.hand_value}{RESET}.")
            print("Would you like to hit or stand?")
            print("(1) Hit\n(2) Stand\n(3) See Rules")
            choice = input().strip().casefold()

            if choice in ('1', 'hit', 'h'):
                self.player.hit()
                self.show_cards()
                print(f"{g}You hit ...{RESET}")
                continue

            if choice in ('2', 'stand', 's'):
                print("You stand. Your turn ends.")
                break

            if choice in ('3', 'rules', 'r'):
                self.display_rules()
                continue


            print(f"{YELLOW}That's not a valid choice.{RESET}")
            continue

    def dealer_turn(self):
        """
        Dealer shows hole card at start of turn.
        If hand value is less than 17, dealer hits until it's 17 or more. 
        If 17 or more, dealer stands.
        """

        self.dealer.reveal_hole()
        self.show_cards()
        print("Dealer's turn.")
        print(f"You have {GREEN}{self.player.hand_value}{RESET}.")
        print(f"The dealer has {RED}{self.dealer.hand_value}{RESET}.")

        while self.dealer.hand_value < self.dealer.STAND:
            self.dealer.hit()
            self.show_cards()
            print(f'{RED}Dealer hits ...{RESET}')

            if self.bust(self.dealer.hand_value):
                print(f"{GREEN}The dealer busted!{RESET}")
                self.winner = self.player
                return

        print(f"{RED}Dealer stands at {self.dealer.hand_value}.{RESET}")

    def determine_winner(self):
        """
        Find the winning participant and set self.winner.
        """
        # if a participant already bust, self.winner will already be set
        if self.winner:
            if self.winner == self.player:
                self.player.chips += self.bet * 2 # player awarded 2x the bet
                return

        player_score = self.player.hand_value
        dealer_score = self.dealer.hand_value

        if player_score == dealer_score:
            # If tie/push, return player's bet
            self.player.chips += self.bet
            self.winner = None # this should already be true
        elif player_score > dealer_score:
            self.player.chips += self.bet * 2 # player awarded 2x the bet
            self.winner = self.player
        else:
            self.winner = self.dealer

    def show_cards(self):
        """
        Formats and displays cards as well as other basic info.
        """
        def format_card(card):
            return card.face if isinstance(card, Card) else ('▒', '▒')

        def color_card(suit):
            """
            Apply red on white if red suit, else black on white
            """
            return ROW if suit in RED_SUITS else BOW

        card_top = "╭──────╮"
        card_upper = "│{}     │"
        card_middle_10 = "│  {}  │"
        card_middle_other = "│  {}   │"
        card_lower = "│     {}│"
        card_bottom = "╰──────╯"

        face_down_middle = f"{BOW}│▒▒▒▒▒▒│{RESET}" # Card back always BOW

        player_hand = [format_card(card) for card in self.player.hand]
        dealer_hand = [format_card(card) for card in self.dealer.hand]

        if not self.dealer.hole_revealed:
            dealer_hand[1] = ('▒', '▒') # Dealer hole card

        def format_hand(hand):
            """ASCII card representations for given hand."""
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

            return "\n".join([top_row,
                              upper_row,
                              middle_row,
                              lower_row,
                              bottom_row])

        system('clear')
        print(f"Dealer's Hand:{' '*17}Dealer Total: {self.dealer.hand_value}")
        print(format_hand(dealer_hand))
        print()
        spacing = 19 - len(str(self.player.chips))
        print(f"Your Chips: {self.player.chips}{' ' * spacing}"\
              f"Your Total: {self.player.hand_value}")
        print("Your Hand:")
        print(format_hand(player_hand))

    def update_chip_display(self):
        """
        Moves the cursor to row 8, column 13 and updates the chip count.
        Assumes that the chip display begins at that position.
        Adjust the format (e.g., width) as needed.
        Currently supports up to 4-digit chip count
        """
        # save cursor position
        print("\033[s", end="")
        # move the cursor to row 8, column 13 ("Your Chips: ")
        print("\033[8;13H", end="")  
        # overwrite the old chip count
        # assuming the chip value is at most 4 digits; 
        # pad with spaces to clear previous content
        print(f"{self.player.chips:4d}", end="")
        # restore cursor to saved position
        print("\033[u", end="")

    def display_welcome_message(self):
        system('clear')
        print(f"{YELLOW}Welcome to Twenty-One!{RESET}")

        while True:
            print("Would you like to see the rules before we begin?")
            view_rules = input("(y/n) ").strip().casefold()

            if view_rules in ("y", "yes"):
                self.display_rules()
                break

            if view_rules in ("n", "no"):
                break

            print(f"{RED}Invalid choice. Please enter 'y' or 'n'.{RESET}")

    def display_goodbye_message(self):
        print(f"{YELLOW}Thanks for playing! Goodbye!{RESET}")

    def display_rules(self):
        print("""
            The goal of 21 is to get as close to 21 as possible without
            going over. Going over 21 is called going bust, and it means
            you automatically lose the hand.
              
            The player ultimately wins in this game by doubling their
            starting chips. See betting rules below.
            
            Betting:
            The player must place a bet at the start of each hand. If the
            player loses the hand, they also lose the chips they've bet.
            If the player wins the hand, they receive twice their bet back.
            In 21, a tie is known as a "push", and the player's bet is
            returned in this case (no chips won or lost).
              
            If the player runs out of chips, they lose and the game ends.
            If the player bets and plays well, they can win by doubling
            the chips they started with!
            
            Hands:
            The player and dealer are each dealt two cards. Both player
            cards are face up, and the dealer has one card face up and
            one face down (the hole card).
              
            Numbered cards are worth their number value, face cards (King,
            Queen, and Jack) are worth 10. A (Ace) is worth either 1 or 11.
            Ace is worth 11 unless that would cause the hand to bust (go
            over 21), in which case it is worth 1. 
            
            After cards are dealt, the player may hit (take another card)
            or stay (end the turn). The player may hit as many times as
            they like before staying or busting.
              
            At the start of the dealer's turn, the hole card will be
            revealed, and the dealer will take their turn, hitting or
            standing as necessary. The dealer must hit if their hand value
            is less than 17, and stand if their hand is worth 17 or more.
            """)

        input("\nEnter/Return to continue")

    def display_hand_result(self):
        """
        Display who won the hand, and how many chips the player won or lost.
        """
        if self.winner == self.player:
            print(f"{GREEN}Success!{RESET}")
            print(f"{GREEN}You won {YELLOW}{self.bet*2}{GREEN} chips!{RESET}")
        elif self.winner == self.dealer:
            print(f"{RED}The dealer won.{RESET}")
            print(f"{RED}You lost your bet of {self.bet} chips.{RESET}")
        else:
            print(f"{YELLOW}Push! You get your bet back.{RESET}")
            print(f"{YELLOW}You didn't gain or lose any chips.{RESET}")

        self.update_chip_display()

    def display_game_result(self):
        """
        If the player is out of chips, the result is a player loss.
        If the player reaches twice the chips started with, the result is a
        player win.
        """
        if self.player.chips <= 0:
            print(f"{RED}You've lost all your chips!{RESET}")
            print(f"{RED}Seems like the house always wins... ")
            print(f"but maybe you'll be luckier next time!{RESET}")
        elif self.player.chips >= 10:
            print(f"    💰 {GREEN}Congratulations!{RESET} 🎉")
            print(f"🏆 {GREEN}You've beaten the house!{RESET} ✨")

    def bust(self, hand_value):
        """
        Determine if a hand has busted.
        """
        if hand_value >= TwentyOneGame.BUSTED:
            return True

        return False

    def reset_for_next_hand(self):
        """
        Reset state for new hand.
        """
        self.player.hand = []
        self.dealer.hand = []
        self.winner = None
        self.bet = 0
        self.dealer.hide_hole()

    def play_again(self):
        """
        Ask if player wants to play again. If so, reset and start new game.
        """
        while True:
            choice = input("\nWill you play again? (y/n): ").strip().lower()

            if choice in ("y", "yes"):
                print(f"{GREEN}Resetting the game... Good luck! 🃏✨{RESET}")
                input("\nEnter/Return to continue")
                return True

            if choice in ("n", "no"):
                return False

            print(f"{RED}Invalid choice. Please enter 'y' or 'n'.{RESET}")

game = TwentyOneGame()
game.start()
