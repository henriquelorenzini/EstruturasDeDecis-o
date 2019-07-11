#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print('Descubra se o ano é bissexto ou não')

ano = int(input('Digite um ano: '))

if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
    print('O ano {} é bissexto'.format(ano))

else:
    print('O ano {} não é bissexto'.format(ano))