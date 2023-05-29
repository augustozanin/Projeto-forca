# Trabalho de Augusto Castanho Zanin
# LMI - 1
import os
import random
respostascertas = []
respostaserradas = []


def trocaString():
    global asteriscos
    asteriscos = ''
    for i in range(len(palavraChave)):
        asteriscos += '*' * len(palavraChave[i])
    print(asteriscos, end='')
    print()


def solicitar():
    global opcao
    opcao = input(
        "Digite Jogar ou Solicitar Dica, para o que preferir:").lower().title()
    global respostaDesafiante, respostascertas, respostaserradas
    if (opcao == "Solicitar Dica"):
        if (len(dicas) == 3):
            print("dica :", dica1)
            del dicas[0]
            jogar()
        elif (len(dicas) == 2):
            print("dica :", dica2)
            del dicas[0]
            jogar()
        elif (len(dicas) == 1):
            print("dica :", dica3)
            del dicas[0]
            jogar()
        elif (len(dicas) == 0):
            print("Acabou suas dicas")
    elif (opcao == "Jogar"):
        jogar()


def jogar():
    global asteriscos
    respostaDesafiante = input("arrisque uma letra:")
    encontrada = False
    for i, letra in enumerate(palavraChave):
        if (palavraChave[i] == respostaDesafiante):
            encontrada = True
            respostascertas.append(letra)
            asteriscos = asteriscos[:i] + letra + asteriscos[i+1:]
    if not encontrada:
        respostaserradas.append(respostaDesafiante)
        print("são respostas erradas:", respostaserradas,
              "numero de respostas erradas:", len(respostaserradas))
    print(asteriscos)


def geral():
    global palavraChave, opcao, dicas, dica1, dica2, dica3, arrayPalavraChave, nomeDesafiante, nomeCompetidor
    # Pede nomes desafiante e competidor
    nomeDesafiante = input("Nome do desafiante: ")
    nomeCompetidor = input("Nome do competidor: ")
    # Limpa a tela
    os.system("cls")
    palavraChave = input("Palavra-chave: ").lower()
    arrayPalavraChave = list(palavraChave)
    print(arrayPalavraChave)
    dica1 = input("dica 1: ")
    dica2 = input("dica 2: ")
    dica3 = input("dica 3: ")
    dicas = [dica1, dica2, dica3]
    os.system("cls")
    trocaString()


geral()
while (len(respostaserradas) < 6) and (len(arrayPalavraChave) != len(respostascertas)):
    solicitar()
if len(respostaserradas) == 6:
    print(nomeDesafiante, " ganhou e ", nomeCompetidor, " perdeu!!!")
else:
    print(nomeDesafiante, " perdeu e ", nomeCompetidor, "ganhou!!!")
final = input("deseja sair(0) ou jogar novamente(1)??")
if (final == "1"):
    os.system("cls")
    geral()
elif (final == "0"):
    print("acabou")
