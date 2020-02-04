import sys
from unittest import TestCase
from src.comandos import opcoes_comando

class TestComandos(TestCase):

    def test_entrada_sem_opcao_deve_sair_e_exibir_mensagem_erro_com_uso(self):
        with self.assertRaises(SystemExit):
            opcoes_comando('', 'nome_arquivo')

    def test_entrada_sem_nome_do_arquivo_deve_lancar_type_error(self):
        with self.assertRaises(TypeError):
            opcoes_comando('python app -e')

    def test_entrada_com_opcao_nao_reconhecida_deve_sair_e_exibir_mensagem_erro(self):
        arg = ['app.py', '-d']
        with self.assertRaises(SystemExit):
            opcoes_comando(arg, 'nome_arquivo')

    def test_entrada_com_opcao_help_deve_sair_e_exibir_mensagem_de_ajuda_sobre_o_software(self):
        arg = ['app.py', '-h']
        with self.assertRaises(SystemExit):
            opcoes_comando(arg, 'nome_arquivo')

    def test_entrada_com_opcao_version_deve_sair_e_exibir_mensagem_de_versao_do_software(self):
        arg = ['app.py', '-v']
        with self.assertRaises(SystemExit):
            opcoes_comando(arg, 'nome_arquivo')

