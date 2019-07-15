# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input('Qual tipo de combustível deseja colocar [A-Alcool, G-Gasolina]? ')
litros = int(input('Quantos litros deseja que seja colocado? '))

valorLiAlc = float(1.90)
valorLiGas = float(2.50)

desc1A = valorLiAlc * 0.03
desc2A = valorLiAlc * 0.05
valorComDesc1A = valorLiAlc - desc1A
valorComDesc2A = valorLiAlc - desc2A

desc1G = valorLiGas * 0.04
desc2G = valorLiGas * 0.06
valorComDesc1G = valorLiGas - desc1G
valorComDesc2G = valorLiGas - desc2G

def alcool():
    if litros < 20:
        valorTotal =  litros * valorComDesc1A
        print('Tipo de combustível: Alcool')
        print('Total enchido: {} '.format(litros))
        print('Valor total: R$ {:.2f} '.format(valorTotal))

    elif litros >= 20:
        valorTotal = litros * valorComDesc2A
        print('Tipo de combustível: Alcool')
        print('Total enchido: {} '.format(litros))
        print('Valor total: R$ {:.2f} '.format(valorTotal))

    else:
        print('Valor inválido')

def gasolina():
    if litros < 20:
        valorTotal = litros * valorComDesc1G
        print('Tipo de combustível: Gasolina')
        print('Total enchido: {} '.format(litros))
        print('Valor total: R$ {:.2f} '.format(valorTotal))

    elif litros >= 20:
        valorTotal = litros * valorComDesc2G
        print('Tipo de combustível: Gasolina')
        print('Total enchido: {} '.format(litros))
        print('Valor total: R$ {:.2f} '.format(valorTotal))

    else:
        print('Valor inválido')



if combustivel == 'A':
    alcool()
elif combustivel == 'G':
    gasolina()
else:
    print('Combustível inválido')