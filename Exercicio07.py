#Faça um Programa que leia três números e mostre o maior e o menor deles.

print('Veja qual dos três números é maior e qual é o menor')

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print('O maior número é {:.1f}'.format(maior))

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('O menor número é {:.1f}'.format(menor))