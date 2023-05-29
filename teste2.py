import os
import random
respostascertas = []
respostaserradas = []
erros = 0
achou_letra = False


def trocaString():
    numeroletras = len(palavraChave)
    palavraOculta = palavraChave.replace(palavraChave, '*' * numeroletras)
    return print(palavraOculta, numeroletras)


def solicitar():
    global respostaDesafiante, respostascertas, respostaserradas, achou_letra
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
    respostaDesafiante = input("arrisque uma letra:")
    encontrada = False
    for i, letra in enumerate(palavraChave):
        if (palavraChave[i] == respostaDesafiante):
            encontrada = True
            respostascertas.append(letra)
            print("são respostas certas:", respostascertas)
    if not encontrada:
        respostaserradas.append(respostaDesafiante)
        print("são respostas erradas:", respostaserradas)



while True:
    # Pede nomes desafiante e competidor
    nomeDesafiante = input("Nome do desafiante: ")
    nomeCompetidor = input("Nome do competidor: ")
    # Limpa a tela
    os.system("cls")
    palavraChave = input("Palavra-chave: ")
    dica1 = input("dica 1: ")
    dica2 = input("dica 2: ")
    dica3 = input("dica 3: ")
    dicas = [dica1, dica2, dica3]
    os.system("cls")
    trocaString()
    opcao = input(
        "Digite Jogar ou Solicitar Dica, para o que preferir:").lower().title()
    solicitar()
    opcao = input(
        "Digite Jogar ou Solicitar Dica, para o que preferir:").lower().title()
    solicitar()
    opcao = input(
        "Digite Jogar ou Solicitar Dica, para o que preferir:").lower().title()
    solicitar()
    opcao = input(
        "Digite Jogar ou Solicitar Dica, para o que preferir:").lower().title()
    solicitar()
    break
