#
# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


print('Folha de pagamento')

hora = float(input('Quantas horas você trabalhou esse mês? '))
valorHora = float(input('Qual valor da sua hora de trabalho? '))

salarioBruto = valorHora * hora

if salarioBruto <= 900.00:
    sindicato = salarioBruto * 0.03
    fgts = salarioBruto * 0.11 #não é descontado
    impostoRenda = 0
    descontos = impostoRenda + sindicato
    salarioLiquido = salarioBruto - descontos

    print('Seu salário bruto é de R$ {:.2f}'.format(salarioBruto))
    print('O imposto de renda equivale à R$ 0.00, é isento')
    print('O valor pago pela empresa ao FGTS é de 11% do seu salário bruto, equivale  à R$ {:.2f}'.format(fgts))
    print('Você teve um total de R$ {:.2f} de descontos'.format(descontos))
    print('Seu salário liqueido é de R$ {:.2f}'.format(salarioLiquido))

elif salarioBruto > 900.00 and salarioBruto <= 1500.00:
    sindicato = salarioBruto * 0.03
    fgts = salarioBruto * 0.11  # não é descontado
    impostoRenda = salarioBruto * 0.05
    descontos = impostoRenda + sindicato
    salarioLiquido = salarioBruto - descontos

    print('Seu salário bruto é de R$ {:.2f}'.format(salarioBruto))
    print('O desconto do imposto de renda equivale à R$ {:.2f}'.format(impostoRenda))
    print('O valor pago pela empresa ao FGTS é de 11% do seu salário bruto, equivale  à R$ {:.2f}'.format(fgts))
    print('Você teve um total de R$ {:.2f} de descontos'.format(descontos))
    print('Seu salário liqueido é de R$ {:.2f}'.format(salarioLiquido))


elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:
    sindicato = salarioBruto * 0.03
    fgts = salarioBruto * 0.11  # não é descontado
    impostoRenda = salarioBruto * 0.1
    descontos = impostoRenda + sindicato
    salarioLiquido = salarioBruto - descontos

    print('Seu salário bruto é de R$ {:.2f}'.format(salarioBruto))
    print('O desconto do imposto de renda equivale à R$ {:.2f}'.format(impostoRenda))
    print('0 valor pago pela empresa ao FGTS é de 11% do seu salário bruto, equivale  à R$ {:.2f}'.format(fgts))
    print('Você teve um total de R$ {:.2f} de descontos'.format(descontos))
    print('Seu salário liqueido é de R$ {:.2f}'.format(salarioLiquido))


elif salarioBruto > 2500.00:
    sindicato = salarioBruto * 0.03
    fgts = salarioBruto * 0.11  # não é descontado
    impostoRenda = salarioBruto * 0.2
    descontos = impostoRenda + sindicato
    salarioLiquido = salarioBruto - descontos

    print('Seu salário bruto é de R$ {:.2f}'.format(salarioBruto))
    print('O desconto do imposto de renda equivale à R$ {:.2f}'.format(impostoRenda))
    print('O valor pago pela empresa ao FGTS é de 11% do seu salário bruto, equivale  à R$ {:.2f}'.format(fgts))
    print('Você teve um total de R$ {:.2f} de descontos'.format(descontos))
    print('Seu salário liqueido é de R$ {:.2f}'.format(salarioLiquido))

else:
    print('erro')