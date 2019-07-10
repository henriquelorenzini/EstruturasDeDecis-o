#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('Veja aqui quanto de aumento você terá no seu salário')

salario = float(input('Qual é seu salário? '))

if salario <= 280.00:
    aumento = salario * 0.2
    novoSalario = salario + aumento

    print('Seu salario era de R$ {:.2f} e você teve um aumento de 20%'.format(salario))
    print('Você teve um aumento de R$ {:.2f}'.format(aumento))
    print('Seu novo salario é de R$ {:.2f}'.format(novoSalario))

elif salario > 280.00 and salario < 700.00:
    aumento = salario + 0.15
    novoSalario = salario + aumento
    print('Seu salario era de R$ {:.2f} e você teve um aumento de 15%'.format(salario))
    print('Você teve um aumento de R$ {:.2f}'.format(aumento))
    print('Seu novo salario é de R$ {:.2f}'.format(novoSalario))

elif salario >= 700.00 and salario < 1500.00:
    aumento = salario * 0.1
    novoSalario = salario + aumento

    print('Seu salario era de R$ {:.2f} e você teve um aumento de 10%'.format(salario))
    print('Você teve um aumento de R$ {:.2f}'.format(aumento))
    print('Seu novo salario é de R$ {:.2f}'.format(novoSalario))

elif salario >= 1500.00:
    aumento = salario * 0.05
    novoSalario = salario + aumento

    print('Seu salario era de R$ {:.2f} e você teve um aumento de 5%'.format(salario))
    print('Você teve um aumento de R$ {:.2f}'.format(aumento))
    print('Seu novo salario é de R$ {:.2f}'.format(novoSalario))
