# Embaralhar cartas
import random

playing = False
chip_pool = 100

bet = 1

jogar_novamente = "Aperte ENTER para jogar navamente e SPACE para sair!"

naipe = ('E', 'C', 'O', 'P')
ordem = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
valor = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Carta:

    def __init__(self, naipe, ordem):
        self.naipe = naipe
        self.ordem = ordem

    def __str__(self):
        return self.naipe + self.ordem

    def grab_naipe(self):
        return self.suit

    def grab_ordem(self):
        return self.ordem

    def draw(self):
        print(self.suit + self.rank)
