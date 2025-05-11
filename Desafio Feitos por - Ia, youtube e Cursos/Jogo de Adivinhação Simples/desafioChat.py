# Aqui e o Projeto do chat Gpt, ele falou que o meu codigo seria melhor se fosse assim

import random

print("-----------Jogo Adivinha Simples-----------\n")

num_aleatorio = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Qual o seu palpite (1 a 20)? "))
    tentativas += 1

    if palpite == num_aleatorio:
        print("\n-----------Parabéns-----------")
        print("Palpite CORRETO!")
        print(f"Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite < num_aleatorio:
        print("\n----------DICA----------")
        print("O palpite está MENOR que o número.")
        print("-------------------------")
    else:
        print("\n----------DICA----------")
        print("O palpite está MAIOR que o número.")
        print("-------------------------")
