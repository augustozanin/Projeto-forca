import os
import random
respostascertas = []
respostaserradas = []

def trocaString():
    numeroletras = len(palavraChave)
    palavraOculta = palavraChave.replace(palavraChave, '*' * numeroletras)
    return print(palavraOculta, numeroletras)

# Problemas, 1 incrementação da respostaDesafiante,


def solicitar():
    if (opcao == "Solicitar Dica"):
        if (len(dicas) == 3):
            print("dica :", dica1)
            respostaDesafiante = input("arrisque uma letra:")
            del dicas[0]

        elif (len(dicas) == 2):
            print("dica :", dica2)
            respostaDesafiante = input("arrisque uma letra:")
            del dicas[1]

        elif (len(dicas) == 1):
            print("dica :", dica3)
            respostaDesafiante = input("arrisque uma letra:")
            del dicas[2]
            
        else:
            print("Acabou suas dicas")

    elif opcao == "Jogar":
        for i, letra in enumerate(palavraChave):
            if respostaDesafiante == letra:
                respostascertas.append(letra)
            else:
                respostaserradas.append(letra)
        print("Letras corretas: ", respostascertas)
        print("Letras erradas: ", respostaserradas)

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
    break
