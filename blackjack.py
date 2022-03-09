# Importando módulos e definindo variáveis

import random

playing = True

suits = ('♥', '♦', '♣', '♠')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


# Classes
class Card:  # Criando as cartas

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit


class Hand:    # Criando as mãos de cartas do Jogador e Dealer

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0    # Acompanha os Aces

    def card_add(self, card):   # Adiciona cartas as mãos do Jogador e Dealer
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.ace += 1

    def adjust_ace(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


class Deck:    # Criando o baralho

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):    # Embaralha as cartas
        random.shuffle(self.deck)

    def deal(self):    # Escolhe UMA carta do baralho
        single_card = self.deck.pop()
        return single_card


class Bets:    # Para fazer apostas

    def __init__(self):
        self.total = 100
        self.bet = 0

    def bet_win(self):
        self.total += self.bet

    def bet_lose(self):
        self.total -= self.bet


# Funções
def make_bet(bets):   # Faz a aposta

    while True:
        try:
            bets.bet = int(input('How much do you want to bet? '))
        except ValueError:
            print('Sorry, please can you type in a number: ')
        else:
            if bets.bet > bets.total:
                print('Your bet has exceeded the value of your wallet.')
            else:
                break


def hit(deck, hand):
    hand.card_add(deck.deal())
    hand.adjust_ace()


def hit_stand(deck, hand):    # Hit ou Stand?
    global playing

    while True:
        ask = input("\nHit or Stand? Enter 'h' or 's': ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stand, Dealer is playing.")
            playing = False
        else:
            print("Sorry, i did not understand. Please, try again!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer hand: ")
    print(" <card hidden> ")
    print("", dealer.cards[1])
    print("\nPlayer hand:", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\nDealer hand: ", *dealer.cards, sep='\n')
    print("Hand value = ", dealer.value)
    print("\nPlayer hand:", *player.cards, sep='\n')
    print("Hand value = ", player.value)


# Final do jogo
def player_burst(player, dealer, bets):
    print("Player Burst!")
    bets.bet_lose()


def player_wins(player, dealer, bets):
    print("\n**** Player Wins! ****")
    bets.bet_win()


def dealer_burst(player, dealer, bets):
    print("\n**** Dealer Burst! ****")
    bets.bet_win()


def dealer_wins(player, dealer, bets):
    print("\n**** Dealer Wins! ****")
    bets.bet_lose()


def push(player, dealer):
    print("\n**** Player and Dealer tie!****")


# O jogo

while True:
    print(33*'-')
    print("***** Welcome to BlackJack *****")
    print(33*'-')

    # Embaralhando e distribuindo as cartas
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand = Hand()
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    # Definindo o valor da carteira do Jogador
    player_bets = Bets()

    # Pergunta a aposta
    make_bet(player_bets)

    # Mostrar as cartas
    show_some(player_hand, dealer_hand)

    while playing:

        hit_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_burst(player_hand, dealer_hand, player_bets)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_burst(player_hand, dealer_hand, player_bets)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_bets)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_bets)

        elif player_hand.value > 21:
            player_burst(player_hand, dealer_hand, player_bets)

        else:
            push(player_hand, dealer_hand)

    print("\nPlayer winnings stand at: ", player_bets.total)

    new_game = input("Play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print(20*'-')
        print("Thanks for playing!")
        print(20*'-')
        break
