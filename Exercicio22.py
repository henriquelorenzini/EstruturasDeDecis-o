#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

print('Número par ou impar')

num = int(input('Digite um número: '))

if (num%2) == 0 :
    print('é par')

else:
    print('é impar')