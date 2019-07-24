# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


def calcula_preco_carne(kg_carne, forma_pagamento, tipo_carne):
    preco_menor = 0
    preco_maior = 0
    tipo_carne_texto = ''
    if tipo_carne == 'F':
        tipo_carne_texto = 'Filé Duplo'
        preco_menor = 4.90
        preco_maior = 5.80
    elif tipo_carne == 'A':
        tipo_carne_texto = 'Alcatra'
        preco_menor = 5.90
        preco_maior = 6.80
    elif tipo_carne == 'P':
        tipo_carne_texto = 'Picanha'
        preco_menor = 6.90
        preco_maior = 7.80

    desconto = 0
    if kg_carne < 5 and forma_pagamento == 0:
        valor_carne = kg_carne * preco_menor
        valor_total = valor_carne

    elif kg_carne < 5 and forma_pagamento == 1:
        valor_carne = kg_carne * preco_menor
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

    elif kg_carne > 5 and forma_pagamento == 1:
        valor_carne = kg_carne * preco_maior
        desconto = valor_carne * 0.05
        valor_total = valor_carne - desconto

    else:
        valor_carne = kg_carne * preco_maior
        valor_total = valor_carne

    return {
        'tipo_carne_texto': tipo_carne_texto,
        'desconto': desconto,
        'valor_carne': valor_carne,
        'valor_total': valor_total
    }


if __name__ == '__main__':
    tipo_carne = input('Qual tipo de carne você deseja comprar[[A]lcatra, [F]ilé Duplo, [P]icanha] ? ')
    kg_carne = float(input('Quantos kilos de carne você deseja ? '))
    forma_pagamento = int(input('Qual a forma de pagamento [Cartão tabajara = 1, outro = 0] ? '))

    retorno = calcula_preco_carne(kg_carne, forma_pagamento, tipo_carne)
    desconto_texto = 'Sem Desconto' if retorno['desconto'] == 0 else '{:.2f}'.format(retorno['desconto'])
    forma_pagamento_texto = 'Cartão tabajara' if forma_pagamento == 1 else 'Outro'

    print('***************CUPOM FISCAL***************')
    print('Tipo da carne******************* {}'.format(retorno['tipo_carne_texto']))
    print('Kilos de carne****************** {}'.format(kg_carne))
    print('Preço total*********************R${:.2f}'.format(retorno['valor_carne']))
    print('Forma de pagamento************** {}'.format(forma_pagamento_texto))
    print('Desconto************************ {}'.format(desconto_texto))
    print('Valor a pagar*******************R${:.2f}'.format(retorno['valor_total']))
