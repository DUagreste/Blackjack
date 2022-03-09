# Embaralhar as cartas
import random

playing = False
wallet = 100
bet = 1

restart = "Press 's' to shuffle again or press 'l' to leave."

suits = ('♥', '♦', '♣', '♠')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return "The hand has {}".format(hand_comp)

    def card_add(self, card):
        self.card.append(card)

        if card.rank == 'A':
            self.ace = True

        self.value += card_value[card.rank]

    def calc_value(self):
        if (self.ace is True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden is True and playing is True:
            starting_card = 1
        else:
            starting_card = 0

        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += " " + card.__str__()

        return "The deck has " + deck_comp


def make_bet():
    global bet
    bet = 0

    print("How much do you want to bet? ")

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >= 1 and bet_comp <= wallet:
            bet = bet_comp
        else:
            print("Invalid bet. Enter a whole number or check your balance.")


def deal_cards():
    global result, playing, deck, player_Hand, dealer_Hand, wallet, bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_Hand = Hand()
    dealer_Hand = Hand()

    # Adicionando 2 cartas para o jogador
    player_Hand.card_add(deck.deal())
    player_Hand.card_add(deck.deal())

    # Adicionando 2 cartas para o dealer
    dealer_Hand.card_add(deck.deal())
    dealer_Hand.card_add(deck.deal())

    result = "Hit or Stand? Press 'h' or 's': "

    playing = True

    game_step()


def hit():
    global playing, wallet, deck, player_Hand, dealer_Hand, result, bet

    if playing:
        if player_Hand.calc_value() <= 21:
            player_Hand.card_add(deck.deal())
        print("Player hand is {}".format(player_Hand))

        if player_Hand.calc_value() > 21:
            result = "Busted! " + restart
            wallet -= bet
            playing = False
        print("Player hand is {}".format(player_Hand))

    else:
        result = "Sorry, can't hit!" + restart

    game_step()


def stand():
    global playing, wallet, deck, player_Hand, dealer_Hand, result, bet

    if playing is False:
        if player_Hand.calc_value() > 0:
            result = "Sorry, you can't stand!"

    else:
        while dealer_Hand.calc_value() < 17:
            dealer_Hand.card_add(deck.deal())

        if dealer_Hand.calc_value() > 21:
            result = "Dealer busts! You win! " + restart
            wallet += bet
            playing = False

        elif dealer_Hand.calc_value() < player_Hand.calc_value():
            result = "You beat the dealer! You win! " + restart
            wallet += bet
            playing = False

        elif dealer_Hand.calc_value() == player_Hand.calc_value():
            result = "It was a draw! " + restart
            playing = False

        else:
            result = "Dealer wins! " + restart
            wallet -= bet

    game_step()
  
