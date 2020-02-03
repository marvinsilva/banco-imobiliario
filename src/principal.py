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