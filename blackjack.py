# Embaralhar cartas
import random

jogando = False
carteira = 100

aposta = 1

jogar_novamente = "Aperte ENTER para jogar navamente e SPACE para sair!"

naipes = ('E', 'C', 'O', 'P')
ordens = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
valores = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Carta:

    def __init__(self, naipe, ordem):
        self.naipe = naipe
        self.ordem = ordem

    def __str__(self):
        return self.naipe + self.ordem

    def grab_naipe(self):
        return self.naipe

    def grab_ordem(self):
        return self.ordem

    def draw(self):
        print(self.naipe + self.ordem)


class Mão:

    def __init__(self):
        self.carta = []
        self.valor = 0
        self.ace = False

    def __str__(self):
        maoComp = ""

        for carta in self.carta:
            carta.nome = carta.__str__()
            maoComp += " " + carta.nome

        return "Sua mão é: {}".format(carta.nome)

    def cartaAdicionar(self, carta):
        self.carta.append(carta)

        if carta.ordem == 'A':
            self.ace = True
        self.valor += valores[carta.ordem]

    def calculoValor(self):
        if(self.ace == 'True' and self.valor < 12):
            return self.valor + 10
        else:
            return self.valor

    def draw(self, oculta):
        if oculta is True and jogando is True:
            cartaInicio = 1
        else:
            cartaInicio = 0
        for x in range(cartaInicio, len(self.carta)):
            self.carta[x].draw()


class Baralho:

    def __init__(self):
        self.baralho = []
        for naipe in naipes:
            for ordem in ordens:
                self.baralho.append(Carta(naipe, ordem))

    def embaralhar(self):
        random.embaralhar(self.baralho)

    def pedirCarta(self):
        umaCarta = self.baralho.pop()
        return umaCarta

    def __str__(self):
        baralhoComp = ""
        for carta in self.baralho:
            baralhoComp += " " + carta.__str__()
        return "O baralho tem " + baralhoComp


def fazerAposta():
    global aposta
    aposta = 0

    print("Qual o valor da sua aposta?")

    while aposta == 0:
        apostaComp = input()
        apostaComp = int(apostaComp)

        if apostaComp >= 1 and apostaComp <= carteira:
            aposta = apostaComp
        else:
            print("Aposta Inválida!")


def distribuirCartas():
    global resultado, jogando, baralho, maoJogador, maoCrupie, carteira, aposta

    baralho = baralho()
    baralho.embaralhar()

    fazerAposta()

    maoJogador = mao()
    maoCrupie = mao()

    # 2 cartas para o Jogador
    maoJogador.cartaAdicionar(baralho.pedirCarta())
    maoJogador.cartaAdicionar(baralho.pedirCarta())

    # 2 cartas para o Crupiê
    maoCrupie.cartaAdicionar(baralho.pedirCarta())
    maoCrupie.cartaAdicionar(baralho.pedirCarta())

    resultado = "Pedir ou ficar? Aperte 'p' ou 'f':"
 
    carteira -= aposta
    jogando = True
    primeiroPasso()