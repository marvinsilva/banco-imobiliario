class Propriedade:
    """ Classe de modelos de propriedades do jogo banco imobiliário
    """


    def __init__(self, posicao, venda, aluguel, proprietario):
        self.posicao = posicao
        self.venda = venda
        self.aluguel = aluguel
        self.proprietario = proprietario


class Jogador:
    """ Classe de modelos de jogadores do jogo banco imobiliário
    """


    def __init__(self, perfil):
        self.perfil = perfil
        self.saldo = 300
        self.posicao = 0
        self.propriedades = []


    def compra_propriedade(self, propriedade):
        self.saldo -= propriedade.venda
        self.propriedades.append(propriedade.posicao)


    def recebe_aluguel(self, aluguel):
        self.saldo += aluguel

