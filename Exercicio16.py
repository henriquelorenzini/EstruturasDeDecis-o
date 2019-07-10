# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print ('Digite os valores A,B e C, para calcularmos uma equação de segundo grau (ax^2 + bx + c)')

a = float(input('Digite um valor para A: '))
if a == 0:
    print('Não é uma equação de segundo grau')
else:
    b = float(input('Digite um valor para B: '))
    c = float(input('Digite um valor para C: '))

    delta = (math.pow(b,2) - (4*a*c))

if delta < 0:
    print('O delta é igual à {:.1f} e não possui raizes'.format(delta))

if delta == 0:
    print('O delta é igual à {:.1f} e possui uma raiz'.format(delta))
    raiz = ((-1)*b + math.sqrt(delta))/(2*a)
    print('A raiz da equação é {:.1f}'.format(raiz))

if delta > 0:
     print('O delta é igual à {:.1f} e possui duas raizes'.format(delta))
     raiz1 = ((-1)*b + math.sqrt(delta))/(2*a)
     raiz2 = ((-1)*b - math.sqrt(delta))/(2*a)

     print('Raiz 1: {:.1f} '.format(raiz1))
     print('Raiz 2: {:.1f} '.format(raiz2))