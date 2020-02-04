from unittest import TestCase
from src.principal import executar_simulacoes

class TestExecutarSimulacoes(TestCase):


    def test_executa_simulacoes_deve_retornar_lista_com_tamanho_do_numero_de_simulacoes(self):
        perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        retorno = executar_simulacoes(perfis=perfis, numero_de_simulacoes=30)
        self.assertEqual(len(retorno), 30)

    def test_executa_simulacoes_deve_retornar_dicionario_com_as_chaves_especificadas(self):
        perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        retorno = executar_simulacoes(perfis=perfis, numero_de_simulacoes=30)
        self.assertEqual(retorno[0].keys(), {'vencedor', 'tipo', 'rodada'})
