# Banco Imobiliário

Este projeto tem como objetivo simular o jogo banco imobiliário e retornar os dados resultantes conforme parâmetros de execução.
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes às execuções. 
Tendo como resultado as seguintes informações:
- Quantas partidas terminam portime out (1000 rodadas);
- Quantos turnos em média demora uma partida;
- Qual a porcentagem de vitórias por comportamento dos jogadores;
- Qual o comportamento que mais vence.

## Requisitos de software

Para executar este programa é necessário apenas ter o Python 3.7 instalado

## Desenvolvimento do sistema

O software foi desenvolvido utilizando a linguagem Python na versão 3.7.2 apenas com bibliotecas nativas da linguagem (built in).
A documentação do Python pode ser encontrada em: https://docs.python.org/3.7/ e suas funções buit-in: https://docs.python.org/3.7/library/functions.html

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
Mais informações sobre este software e descrição do desafio podem ser encontradas no repositório 'docs' deste projeto.
