import random
from src.modelos import Jogador, Propriedade

def jogada(jogadores, jogador, tabuleiro):
    if jogador.saldo > 0:
        numero_sorteado_dado = random.randrange(1, 7)
        jogador.posicao += numero_sorteado_dado
        if jogador.posicao > 20:
            jogador.posicao -= 20
            jogador.saldo += 100
        elif jogador.posicao == 20:
            jogador.posicao = 1
            jogador.saldo += 100
        propriedade = tabuleiro[jogador.posicao]

        # Se a propriedade não possui proprietario
        if not propriedade.proprietario:
            if jogador.perfil == 'impulsivo':
                if jogador.saldo >= propriedade.venda:
                    jogador.compra_propriedade(propriedade)
                    propriedade.proprietario = jogador.perfil
            elif jogador.perfil == 'exigente':
                if jogador.saldo >= propriedade.venda and propriedade.aluguel > 50:
                    jogador.compra_propriedade(propriedade)
                    propriedade.proprietario = jogador.perfil
            elif jogador.perfil == 'cauteloso':
                if jogador.saldo >= propriedade.venda + 80:
                    jogador.compra_propriedade(propriedade)
                    propriedade.proprietario = jogador.perfil
            elif jogador.perfil == 'aleatorio':
                probabilidade = random.randrange(1, 101)
                if jogador.saldo >= propriedade.venda and probabilidade > 50:
                    jogador.compra_propriedade(propriedade)
                    propriedade.proprietario = jogador.perfil
        # Se possui proprietario verifica se não é o mesmo jogador
        else:
            if jogador.perfil != propriedade.proprietario:
                jogador.saldo -= propriedade.aluguel
                for pos in range(len(jogadores)):
                    if jogadores[pos].perfil == propriedade.proprietario:
                        jogadores[pos].saldo += propriedade.aluguel
            # Valida se jogador possui saldo para continuar na partida
            if jogador.saldo <= 0:
                if jogador.propriedades:
                    for item in jogador.propriedades:
                        tabuleiro[item].proprietario = None
                jogador.propriedades = []

def monopoly(perfis, quantidade_posicoes_tabuleiro=20, numero_de_simulacoes=10, numero_maximo_rodadas=1000):
    dados = []
    # Inicio das simulacoes
    for simulacao in range(1, numero_de_simulacoes + 1):
        eliminados = []
        # instanciando jogadores e propriedades
        jogadores = [Jogador(perfil) for perfil in perfis]
        tabuleiro = [Propriedade(posicao=pos,
                                 venda=random.randrange(90, 180),
                                 aluguel=random.randrange(60),
                                 proprietario=None) for pos in range(quantidade_posicoes_tabuleiro)]
        # Inicio das rodadas na simulacao
        for rodada in range(1, numero_maximo_rodadas):
            for pos in range(len(jogadores)):
                if jogadores[pos].saldo <= 0 and jogadores[pos].perfil not in eliminados:
                    eliminados.append(jogadores[pos].perfil)
                # Inicio da jogada na rodada
                jogada(jogadores, jogadores[pos], tabuleiro)
            # Partida encerrada com mais de 2 jogadores eliminados
            if len(eliminados) > 2:
                vencedor = [perfil for perfil in perfis if perfil not in eliminados]
                vencedor = "".join(vencedor)
                dados.append({
                    'vencedor': vencedor,
                    'tipo': 'regular',
                    'rodada': rodada
                })
                break
        # Partida encerrada por time out
        if rodada == numero_maximo_rodadas - 1:
            vencedor = jogadores[0].perfil
            saldo_vencedor = jogadores[0].saldo
            for index in range(len(jogadores)):
                if jogadores[index].saldo >= saldo_vencedor:
                    saldo_vencedor = jogadores[index].saldo
                    vencedor = jogadores[index].perfil
            dados.append({
                'vencedor': vencedor,
                'tipo': 'timeout',
                'rodada': rodada
            })

    return dados