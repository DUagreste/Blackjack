# Embaralhar cartas
import random

jogando = False
carteira = 100

aposta = 1

jogar_novamente = "Deseja jogar novamente? Aperte 's' para sim e 'n' para sair!"

naipes = ('E', 'C', 'O', 'P')
ordens = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
valores = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Carta:

    def __init__(self, naipe, ordem):
        self.naipe = naipe
        self.ordem = ordem

    def __str__(self):
        return self.naipe + self.ordem

    def pegar_naipe(self):
        return self.naipe

    def pegar_ordem(self):
        return self.ordem

    def draw(self):
        print(self.naipe + self.ordem)


class Mao:

    def __init__(self):
        self.carta = []
        self.valor = 0
        self.ace = False

    def __str__(self):
        maoComp = ""

        for carta in self.carta:
            cartaNome = carta.__str__()
            maoComp += " " + cartaNome

        return "Sua mão é: {}".format(maoComp)

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
        random.shuffle(self.baralho)

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

    baralho = Baralho()
    baralho.embaralhar()

    fazerAposta()

    maoJogador = Mao()
    maoCrupie = Mao()

    # 2 cartas para o Jogador
    maoJogador.cartaAdicionar(baralho.pedirCarta())
    maoJogador.cartaAdicionar(baralho.pedirCarta())

    # 2 cartas para o Crupiê
    maoCrupie.cartaAdicionar(baralho.pedirCarta())
    maoCrupie.cartaAdicionar(baralho.pedirCarta())

    resultado = "Pedir ou ficar? Aperte 'p' ou 'f':"

    jogando = True

    primeiroPasso()


def puxarCarta():
    global jogando, carteira, baralho, maoCrupie, maoJogador, resultado, aposta

    if jogando:
        if maoJogador.calculoValor() <= 21:
            maoJogador.cartaAdicionar(baralho.pedirCarta())
        print(f"A mão do jogador é: {maoJogador}")

        if maoJogador.valor() > 21:
            resultado = "Estourou!" + jogar_novamente
            carteira -= aposta
            jogando = False

    else:
        resultado = "Desculpa, não conseguiu!" + jogar_novamente

    primeiroPasso()


def ficar():
    global jogando, carteira, baralho, maoJogador, maoCrupie, resultado, aposta

    if jogando is False:
        if maoJogador.calculoValor() > 0:
            resultado = "Desculpa, você não pode ficar" + jogar_novamente

        else:
            while maoCrupie.calculoValor() < 17:
                maoCrupie.cartaAdicionar(baralho.pedirCarta())

            if maoCrupie.calculoValor() > 21:
                resultado = "O crupiê estourou! Você ganhou!" + jogar_novamente
                carteira += aposta
                jogando = False

            elif maoCrupie.calculoValor() < maoJogador.calculoValor():
                resultado = "Sua mão é melhor! Você ganhou!" + jogar_novamente
                carteira += aposta
                jogando = False

            elif maoCrupie.calculoValor() == maoJogador.calculoValor():
                resultado = "Jogo empatado!" + jogar_novamente
                carteira += aposta
                jogando = False

            else:
                resultado = "Você perdeu!" + jogar_novamente
        primeiroPasso()


def primeiroPasso():
    print("")
    print("Mão do jogador é:")
    maoJogador.draw(hidden=False)
    print("Valor: " + str(maoJogador.calculoValor()))

    print("")
    print("Mão do crupiê é:")
    maoCrupie.draw(hidden=True)
    print("Valor: " + str(maoCrupie.calculoValor()))

    if jogando is False:
        print("Carteira: R$"+str(carteira))

    print(resultado)

    jogadorDecisao()


def saida():
    print("Obrigado por jogar!")
    exit()


def jogadorDecisao():
    plin = input().lower()

    if plin == "p":
        puxarCarta()
    elif plin == "f":
        ficar()
    elif plin == "d":
        distribuirCartas()
    elif plin == "q":
        saida()
    else:
        print("Digito errado. Aperte 'p', 'f', 'd' ou 'q': ")
        jogadorDecisao()


def introducao():
    statement = "Seja bem-vindo ao BlackJack!"
    print(statement)


baralho = Baralho()
baralho.embaralhar()

maoJogador = Mao()
maoCrupie = Mao()

introducao()
distribuirCartas()
