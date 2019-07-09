#Faça um Programa que leia três números e mostre o maior deles.

print('Veja qual dos três números é maior')

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print('O número {:.2f} é maior'.format(num1))

elif num2 > num1 and num2 > num3:
    print('O número {:.2f} é maior'.format(num2))

elif num3 > num1 and num3 > num1:
    print('O número {:.2f} é maior'.format(num3))

elif num1 == num2 == num3:
    print('Os números são iguais')
