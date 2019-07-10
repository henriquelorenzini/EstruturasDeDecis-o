#Faça um Programa que leia três números e mostre-os em ordem decrescente

print('Escolha três números e os veja em ordem decrescente')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

print(num1,', ',num2,', ',num3)

if num3 > num2:
    maior = num3
    num3 = num2
    num2 = maior

if num2 > num1:
    maior = num2
    num2 = num1
    num1 = maior

if num3 > num2:
    maior = num3
    num3 = num2
    num2 = maior

print(num1,', ',num2,', ',num3)