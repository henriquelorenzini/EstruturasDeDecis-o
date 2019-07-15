# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kiloMorango = float(input('Quantos kilos de morango você quer? '))
kiloMaca = float(input('Quantos kilos de mação você quer? '))



def morango():
    if kiloMorango <= 5:
        valorMorango = kiloMorango * 2.50
        descontoMorango = valorMorango * 0.1
        print('Kilos de morango: {} '.format(kiloMorango))
        print('Preço do morango: R$ {:.2f}'.format(valorMorango))

    elif kiloMorango >= 8 or valorMorango >= 25:

    else:
        valorMorango = kiloMorango * 2.20
        print('Kilos de morango: {} '.format(kiloMorango))
        print('Preço do morango: R$ {:.2f}'.format(valorMorango))

def maca():
    if kiloMaca <=5:
        valorMaca = kiloMaca * 1.80
        print('Kilos de maçã: {} '.format(kiloMaca))
        print('Preço da maçã: R$ {:.2f}'.format(valorMaca))
    else:
        valorMaca = kiloMaca * 1.50
        print('Kilos de maçã: {} '.format(kiloMaca))
        print('Preço da maçã: R$ {:.2f}'.format(valorMaca))

def morangoMaca():
    if kiloMorango != 0 and kiloMaca !=0 and kiloMorango <= 5 and kiloMaca <= 5:
        valorMorango = kiloMorango * 2.50
        valorMaca = kiloMaca * 1.80
        valorTotal = valorMorango + valorMaca
        print('Kilos de morango: {} '.format(kiloMorango))
        print('Preço do morango: R$ {:.2f}'.format(valorMorango))
        print('Kilos de maçã: {} '.format(kiloMaca))
        print('Preço da maçã: R$ {:.2f}'.format(valorMaca))
        print('Valor total: R$ {:.2f} '.format(valorTotal))
    else:
        valorMorango = kiloMorango * 2.20
        valorMaca = kiloMaca * 1.50
        valorTotal = valorMaca + valorMorango
        print('Kilos de morango: {} '.format(kiloMorango))
        print('Preço do morango: R$ {:.2f}'.format(valorMorango))
        print('Kilos de maçã: {} '.format(kiloMaca))
        print('Preço da maçã: R$ {:.2f}'.format(valorMaca))
        print('Valor total: R$ {:.2f} '.format(valorTotal))

    if

if kiloMorango != 0 and kiloMaca == 0:
    morango()
elif kiloMaca !=0 and kiloMorango == 0:
    maca()
elif kiloMorango != 0 and kiloMaca != 0:
    morangoMaca()
else:
    print('Valor inválido')