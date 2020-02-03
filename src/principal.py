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


def tratamento_de_dados(dados, perfis, numero_de_simulacoes):
    dict_auxiliar = {}
    numero_rodadas_total = 0
    for item in dados:
        numero_rodadas_total += item.get('rodada')
        for valor in item.values():
            if isinstance(valor, str):
                contagem = dict_auxiliar.get(valor, 0) + 1
                dict_auxiliar[valor] = contagem

    maior_numero_vitorias = 0
    perfil_mais_vitorioso = str()
    porcent_vitorias_por_perfil = {}
    for item in dict_auxiliar.keys():
        if item in perfis:
            # Porcentagem de vitorias por comportamento dos jogadores
            porcent_vitorias_por_perfil[item] = f'{round((dict_auxiliar.get(item) / numero_de_simulacoes) * 100, 2)}%'
            if dict_auxiliar.get(item) > maior_numero_vitorias:
                maior_numero_vitorias = dict_auxiliar.get(item)
                perfil_mais_vitorioso = item

    media_de_rodadas = round(numero_rodadas_total / numero_de_simulacoes)
    partidas_terminam_timeout = dict_auxiliar.get('timeout')
    partidas_terminam_regular = dict_auxiliar.get('regular')

    resultado = {
        'partidas terminadas timeout': partidas_terminam_timeout,
        'partidas terminadas regular': partidas_terminam_regular,
        'media de turnos por partida': media_de_rodadas,
        'perfil mais vitorioso': f'{perfil_mais_vitorioso} ({maior_numero_vitorias} vitorias)',
        'vitorias por perfil': porcent_vitorias_por_perfil
    }

    return resultado


if __name__ == '__main__':
    perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
    quantidade_posicoes_tabuleiro = 20
    numero_de_simulacoes = 300
    numero_maximo_rodadas = 1000

    # Ordem aleatorio de perfis para inicio do jogo
    random.shuffle(perfis)

    dados = monopoly(perfis,
                     quantidade_posicoes_tabuleiro,
                     numero_de_simulacoes,
                     numero_maximo_rodadas)

    resultado = tratamento_de_dados(dados, perfis, numero_de_simulacoes)
    print(f'\nResultado para {numero_de_simulacoes} simulacoes:\n')
    [print(f'{chave}: {valor}') for chave, valor in resultado.items()]
