from Jogador import Jogador, cadastro
from aposta import aposta

dados = cadastro()

if dados is not None:
    nome, idade, valor = dados
    player = Jogador(nome, idade, valor)
    aposta(valor)
else:
    print("Encerrando o programa.")