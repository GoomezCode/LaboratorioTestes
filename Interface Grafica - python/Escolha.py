# for n in range(1, 11):
#     print(f"{n} X 10 = ")


def tabuada():
    num = int(input("Qual o numero dejesado? "))

    for n in range(1, 11):
        resultado = n * num
        print(f"{n} X {num} = {resultado}")

def calculadora():
    operacao = input("Qual a operação? | + | - | X | / | : ")

    num1 = int(input("Qual o primeiro num? : "))
    num2 = int(input("Qual o segundo num? : "))
    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "X":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("ERROR: 404")
        print("Não temos essa operação")
    print(f"O Calculo é: {resultado}")




pergunta = input("Oque vc que? | Calculadora | tabuada | ")

if pergunta == "calculadora":
    calculadora()
elif pergunta == "tabuada":
    tabuada()
else:
    print("Você tem apenas duas escolhas")
