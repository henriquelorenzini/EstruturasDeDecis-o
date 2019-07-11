# #Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = input('Digite um número menor que 1000: ')
numStr = str(num)
tamanho = len(numStr)

if tamanho == 3:
    centena = numStr [0:1]
    dezena = numStr [1:2]
    unidade = numStr [2:3]

    print('O número {} é dividio em: {} centenas, {} dezenas e {} unidades'.format(numStr,centena,dezena,unidade))

if tamanho == 2:
    dezena = numStr [0:1]
    unidade = numStr [1:2]
    print('O número {} é dividido em: {} dezenas e {} unidades'.format(numStr,dezena,unidade))

if tamanho == 1:
    unidade =  numStr [0:1]
    print('O número {} é dividido em: {} unidades'.format(numStr,unidade))

