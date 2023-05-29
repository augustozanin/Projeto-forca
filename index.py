import os

def trocaString():
    numeroletras = len(palavraChave)
    palavraOculta = palavraChave.replace(palavraChave, '*' * numeroletras)
    return print(palavraOculta, numeroletras)

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
    os.system("cls")
    trocaString()
    opcao = input("Digite Jogar ou Solicitar Dica, para o que preferir:")
    break




'''def solicitar():
    if()'''