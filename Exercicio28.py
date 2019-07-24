# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo_carne = input('Qual tipo de carne você deseja comprar[[A]lcatra, [F]ilé Duplo, [P]icanha] ? ')
kg_carne = float(input('Quantos kilos de carne você deseja ? '))
forma_pagamento = int(input('Qual a forma de pagamento [Cartão tabajara = 1, outro = 0] ? '))

def fileDuplo():
    if kg_carne < 5 and forma_pagamento == 0:
        valor_carne = kg_carne * 4.90
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne < 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 4.90
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne > 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 5.80
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    else:
        valor_carne = kg_carne * 5.80
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))


def Alcatra():
    if kg_carne < 5 and forma_pagamento == 0:
        valor_carne = kg_carne * 5.90
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne < 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 5.90
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne > 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 6.80
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    else:
        valor_carne = kg_carne * 6.80
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

def Picanha():
    if kg_carne < 5 and forma_pagamento == 0:
        valor_carne = kg_carne * 6.90
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne < 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 6.90
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    elif kg_carne > 5 and forma_pagamento == 1:
        valor_carne = kg_carne * 7.80
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço da carne******************R${:.2f}'.format(valor_carne))
        print('Forma de pagamento**************Cartão tabajara')
        print('Desconto************************ R${:.2f}'.format(desconto))
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

    else:
        valor_carne = kg_carne * 7.80
        valor_total = valor_carne

        print('***************CUPOM FISCAL***************')
        print('Tipo da carne*******************Filé Duplo')
        print('Kilos de carne****************** {}'.format(kg_carne))
        print('Preço total*********************R${:.2f}'.format(valor_total))
        print('Forma de pagamento**************Outro')
        print('Desconto************************ Sem desconto')
        print('Valor a pagar*******************R${:.2f}'.format(valor_total))

if tipo_carne == 'F':
    fileDuplo()
if tipo_carne == 'A':
    Alcatra()
if tipo_carne == 'P':
    Picanha()
else:
    print('Valor inválido')
