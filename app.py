#!/usr/bin/env python

""" Esta aplicação tem como objetivo simular o jogo banco imobiliário e retornar os dados
    resultantes conforme parâmetros de execução
    Data: 03 de Fevereiro de 2020
    Python 3.7.2
"""

import random
import sys
import os
from src.principal import executar_simulacoes, tratamento_de_dados
from src.comandos import opcoes_comando

nome_arquivo = os.path.basename(__file__)

if(__name__ == "__main__"):

    if opcoes_comando(sys.argv, nome_arquivo):

        # Paramêtros para simulação do jogo banco imobiliário
        perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        quantidade_posicoes_tabuleiro = 20
        numero_de_simulacoes = 300
        numero_maximo_rodadas = 1000

        # Ordem aleatorio de perfis para inicio do jogo
        random.shuffle(perfis)

        dados = executar_simulacoes(perfis,
                         quantidade_posicoes_tabuleiro,
                         numero_de_simulacoes,
                         numero_maximo_rodadas)

        resultado = tratamento_de_dados(dados, perfis, numero_de_simulacoes)
        print(f'\nResultado para {numero_de_simulacoes} simulacoes:\n')
        [print(f'{chave}: {valor}') for chave, valor in resultado.items()]

