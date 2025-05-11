#                       Desafios:
# 1. Exiba os números de 1 a 10 usando um loop WHILE
# 2. Escreva um programa que conta quantas vogais existem na string que o usuário digita
# 3. Escreve um programa onde o sistema exibe uma tabuada de 1 a 100

def chama01():
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1

def chama02():
    palavra = input("Escreva E contamos as Vogais: ")
    vogais = "aeiouAEIOU"
    contador = 0
    for n in palavra:
        if n in vogais:
            contador += 1 
    print(f"A palavra {palavra} tem {contador} Vogais")

def chamar03():
    num = int(input("Qual o Numero desejado da tabuada? : "))
    a = int(input("Até qual Tabuada vc quer? (1 a 100) : "))
    a += 1
    for n in range(1, a):
        resultado = num * n
        print(f"{n} X {num} = {resultado}")
        
# --------------------------------------------------------------------------------------------------------------------------------------


