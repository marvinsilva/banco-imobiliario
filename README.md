# Banco Imobiliário

Este projeto tem como objetivo simular o jogo banco imobiliário e retornar os dados resultantes conforme parâmetros de execução.
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes às execuções. 
Tendo como resultado as seguintes informações:
- Quantas partidas terminam portime out (1000 rodadas);
- Quantos turnos em média demora uma partida;
- Qual a porcentagem de vitórias por comportamento dos jogadores;
- Qual o comportamento que mais vence.
___

## Requisitos de software

Para executar este programa é necessário apenas ter o Python 3.7 instalado
___

## Desenvolvimento do sistema

O software foi desenvolvido utilizando a linguagem Python na versão 3.7.2 apenas com bibliotecas nativas da linguagem.
A documentação do [Python](https://docs.python.org/3.7/) fornece mais informações sobre a linguagem e suas funções [buit-in](https://docs.python.org/3.7/library/functions.html).
___

## Como utilizar

Clone este repositório e crie o ambiente virtual (env)

Acesse o diretório raiz e execute o seguinte comando:
```
$ python app.py -e
```
Este app aceita os seguintes argumentos:
```
$ python app.py [opções: -e --exec | -v --version | -h --help]

-e   :   executa as simulações do jogo banco imobiliário
-v   :   versão do software
-h   :   mensagem de ajuda sobre o software
```
Para executar os testes de software utilizar o seguinte comando a partir do diretório raiz do projeto:
```
$ python -m unittest discover
```
O resultado da execução deve ser exibido no Console conforme exemplo:
```
Resultado para 300 simulacoes:

partidas terminadas timeout: 243
partidas terminadas regular: 57
media de turnos por partida: 841
perfil mais vitorioso: cauteloso (120 vitorias)
vitorias por perfil: {'impulsivo': '37.0%', 'cauteloso': '40.0%', 'aleatorio': '13.67%', 'exigente': '9.33%'}
```

* Caso esteja utilizando uma IDE, como Pycharm, rodar o arquivo 'principal.py' disponível no diretório 'src' do projeto.

Mais informações sobre este software e descrição do desafio podem ser encontradas no repositório 'docs' deste projeto.
