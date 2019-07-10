# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes

print('Digite 3 valores para os lados e veja que tipo de triângulo é')

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

#Forma um triangulo
if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
    print('Não é possível formar um triângulo')

#Equilatero
elif lado1 == lado2 == lado3:
    print('É possível formar um triângulo equilátero')

#Isóceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('É possível formar um triângulo isóceles')

#Escaleno
else:
    print('É possível formar um triângulo escaleno')