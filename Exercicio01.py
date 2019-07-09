# Faça um Programa que peça dois números e imprima o maior deles.

print('Veja qual dos dois números é maior')

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 > num2:
    print('O número {:.2f} é maior'.format(num1))

elif num2 > num1:
    print('O número {:.2f} é maior'.format(num2))

elif num1 == num2:
    print('Os números são iguais')

else:
    print('Insira dois valores')