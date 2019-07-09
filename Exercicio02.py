# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input('Digite um valor aleatório: '))

if numero >= 0:
    print('O número {:.1f} é positivo'.format(numero))

else:
    print('O número {:.1f} é negativo'.format(numero))