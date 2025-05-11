# Objetivo: Criar um programa onde o computador escolhe um número aleatório entre 1 e 20, e o jogador precisa adivinhar qual é esse número.

# Requisitos: 
    # 1. O programa deve gerar número aleatório entre 1 e 20.
    # 2. O usuário deve digitar um palpite.
    # 3. O programa deve informar se o palpite está certo, muito alto ou muito baixo
    # 4. O usuário pode tentar várias vezes até acertar.
    # 5. Ao acertar, o programa mostra quantas tentativas foram necessárias.

import random


print("-----------Jogo Adivinha Simples-----------")
print()

numAleatorio = random.randint(1, 20)
contador = -1

def chamada():
    global contador
    contador += 1

    print()
    numResposta = int(input("Qual o Palpite: "))
    
    while numResposta == numAleatorio:
        print
        print("-----------Parabéns-----------")
        print("Palpite CORRETO")
        print()
        print("-----------Tentativas-----------")
        print(f"Você teve {contador} tentativas")
        break
    while numResposta < numAleatorio:
        print("----------DICA----------")
        print("O Palpite está MENOR")
        print("----------Novo Palpite----------")

        chamada()
        break
    while numResposta > numAleatorio:
        print("----------DICA----------")
        print("O Palpite está MAIOR")
        print("----------Novo Palpite----------")

        chamada()
        break

chamada()
