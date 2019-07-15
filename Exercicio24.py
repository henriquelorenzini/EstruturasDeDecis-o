# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")

def check():
    if ( resOper // 1 ==  resOper):
        print("Inteiro")
        if  resOper % 2 == 0:
            print("Par")
            if  resOper > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")

if operacao == '+':
    resOper = numero1 + numero2
    print("Resultado: ", resOper)
    check()
elif operacao == '-':
    resOper = numero1 - numero2
    print("Resultado: ", resOper)
    check()
elif operacao == '/':
    resOper = numero1 / numero2
    print("Resultado: ", resOper)
    check()
elif operacao == '*':
    resOper = numero1 * numero2
    print("Resultado: ", resOper)
    check()
else:
    print("Valor Invalido")