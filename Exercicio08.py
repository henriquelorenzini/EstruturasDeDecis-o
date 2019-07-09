#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print('Descubra qual o melhor produto para comprar')

produto1 = float(input('Qual o valor do primeiro produto? '))
produto2 = float(input('Qual o valor do segundo produto? '))
produto3 = float(input('Qual o valor do terceiro produto? '))


if produto1 < produto2 and produto3:
    print('R$'+str(produto1))
    print('R$'+str(produto2))
    print('R$'+str(produto3))

    print('O produto mais em conta para comprar é o primeiro produto')

elif produto2 < produto1 and produto3:
    print('R$' + str(produto1))
    print('R$' + str(produto2))
    print('R$' + str(produto3))

    print('O produto mais em conta para comprar é o segundo produto')

elif produto3 < produto2 and produto1:
    print('R$' + str(produto1))
    print('R$' + str(produto2))
    print('R$' + str(produto3))

    print('O produto mais em conta para comprar é o terceiro produto')

elif produto1 == produto2 and produto1 and produto2 < produto3:
    print('R$' + str(produto1))
    print('R$' + str(produto2))
    print('R$' + str(produto3))

    print('O produto 1 e o produto 2 tem o mesmo valor, são os mais baratos')

elif produto1 == produto3 and produto1 and produto3 < produto2:
    print('R$' + str(produto1))
    print('R$' + str(produto2))
    print('R$' + str(produto3))

    print('O produto 1 e o produto 3 tem o mesmo valor, são os mais baratos')

elif produto2 == produto3 and produto2 and produto3 < produto1:
        print('R$' + str(produto1))
        print('R$' + str(produto2))
        print('R$' + str(produto3))

        print('O produto 2 e o produto 3 tem o mesmo valor, são os mais baratos')

else:
    print('Todos os valores são iguais')
