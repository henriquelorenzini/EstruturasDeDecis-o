#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

print('Inteiro ou decimal')

num = float(input('Digite um número: '))

if num//1 == num:
    print('Número inteiro')
else:
    print('Número decimal')