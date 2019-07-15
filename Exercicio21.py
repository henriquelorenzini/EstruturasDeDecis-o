# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


print('ATM, saques de 10 até 600 reais')

num = int(input('Digite o valor a ser sacado: R$'))

cem = int(num/100)
num = num % 100

cinquenta = int(num/50)
num = num % 50

dez = int(num/10)
num = num % 10

cinco = int(num/5)
num = num % 5

um = num

print('Notas de R$100,00: {:.0f}', cem)
print('Notas de R$50,00: {:.0f}',cinquenta)
print('Notas de R$10,00: {:.0f}',dez)
print('Notas de R$5,00: {:.0f}',cinco)
print('Notas de R$1,00: {:.0f}',um)