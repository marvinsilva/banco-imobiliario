from unittest import TestCase
from src.principal import tratamento_de_dados


class TestTratamentoDeDados(TestCase):


    def test_tratamento_de_dados_deve_retornar_dicionario_com_tamanho_cinco(self):
        perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        numero_de_simulacoes = 30
        dados = [
            {'vencedor': 'cauteloso', 'tipo': 'regular', 'rodada': 104},
            {'vencedor': 'impulsivo', 'tipo': 'regular', 'rodada': 18},
            {'vencedor': 'aleatorio', 'tipo': 'timeout', 'rodada': 999},
            {'vencedor': 'exigente', 'tipo': 'timeout', 'rodada': 999},
            {'vencedor': 'cauteloso', 'tipo': 'timeout', 'rodada': 999},
        ]
        retorno = tratamento_de_dados(dados, perfis, numero_de_simulacoes)
        self.assertEqual(len(retorno), 5)

    def test_tratamento_de_dados_deve_retornar_dicionario_com_as_chaves_especificadas(self):
        perfis = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        numero_de_simulacoes = 30
        dados = [
            {'vencedor': 'cauteloso', 'tipo': 'regular', 'rodada': 104},
            {'vencedor': 'impulsivo', 'tipo': 'regular', 'rodada': 18},
            {'vencedor': 'aleatorio', 'tipo': 'timeout', 'rodada': 999},
            {'vencedor': 'exigente', 'tipo': 'timeout', 'rodada': 999},
            {'vencedor': 'cauteloso', 'tipo': 'timeout', 'rodada': 999},
        ]
        retorno = tratamento_de_dados(dados, perfis, numero_de_simulacoes)
        self.assertEqual(retorno.keys(), {
            'partidas terminadas timeout',
            'partidas terminadas regular',
            'media de turnos por partida',
            'perfil mais vitorioso',
            'vitorias por perfil'
        })

