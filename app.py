import random
from src.principal import monopoly, tratamento_de_dados

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