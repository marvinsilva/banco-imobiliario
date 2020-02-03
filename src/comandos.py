import sys
import getopt

__author__ = "[marvinsilva] Marcus Vinicius Laurindo da Silva"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0.0"
__status__ = "Production"


def opcoes_comando(argument, nome_arquivo):
    """ Função responsável por tratar os parâmetros do comando de entrada
    """

    mensagem_ajuda = f'\nUso: python {nome_arquivo} [opções] ... \
                        \n[-e --exec | -v --version | -h --help]\
                        \nopçoes e argumentoss:\
                        \n-e   :   executa as simulações do jogo banco imobiliário \
                        \n-v   :   versão do software\
                        \n-h   :   mensagem de ajuda sobre o software\n\
                        \nPara testar use o seguinte comando no diretório raiz deste projeto:\
                        \n$ python -m unittest discover'

    try:
        opts, args = getopt.getopt(argument[1:], "evh", ["exec=", "version", "help"])
        if len(argument) < 2 or not opts:
            print(f'Erro: uso python {nome_arquivo} <opcoes -e -h -v>')
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
        print(f'Error: {err}')
        sys.exit(2)

