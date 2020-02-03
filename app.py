#!/usr/bin/env python

""" Esta aplicação tem como objetivo simular o jogo banco imobiliário e retornar os dados
    resultantes conforme parâmetros de execução
    Data: 03 de Fevereiro de 2020
    Python 3.7.2
"""

import random
import os
import sys
import getopt
from src.principal import executar_simulacoes, tratamento_de_dados

__author__ = "[marvinsilva] Marcus Vinicius Laurindo da Silva"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__status__ = "Production"
file_name = os.path.basename(__file__)

mensagem_ajuda = f'\nUso: python {file_name} [opções] ... \
                    \n[-e --exec | -v --version | -h --help]\
                    \nopçoes e argumentoss:\
                    \n-e   :   executa as simulações do jogo banco imobiliário \
                    \n-v   :   versão do software\
                    \n-h   :   mensagem de ajuda sobre o software\n\
                    \nPara testar use o seguinte comando no diretório raiz deste projeto:\
                    \n$ python -m unittest discover'

def opcoes_comando(argument):
    """ Parses the command line options and the parameter list
    """
    try:
        opts, args = getopt.getopt(argument[1:], "evh", ["exec=", "version", "help"])

        if len(argument) < 2 or not opts:
            print(f'Erro: uso {file_name} <opcoes -e -h -v>')
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-e", "--exec"):
                return True
            elif opt in ("-h", "--help"):
                print(mensagem_ajuda)
                sys.exit()
            elif opt in ("-v", "--version"):
                print(f'Version: {__version__}\n'
                      f'Author: {__author__}\n'
                      f'License: {__license__}\n'
                      f'Status: {__status__}')
                sys.exit()
            else:
                assert False, "Comando não reconhecido"

    except getopt.GetoptError as err:
        print(f'Erro: {err}')
        sys.exit(2)


if(__name__ == "__main__"):

    if opcoes_comando(sys.argv):

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

