# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print('Descubra se você foi aprovado ou não')

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

if media >= 9.00 and media <= 10:
    print('Sua primeira nota foi {:.1f}'.format(nota1))
    print('Sua segunda nota foi {:.1f}'.format(nota2))
    print('Você foi aprovado com nota {:.1f} e seu conceito foi A'.format(media))

elif media >= 7.50 and media < 9:
    print('Sua primeira nota foi {:.1f}'.format(nota1))
    print('Sua segunda nota foi {:.1f}'.format(nota2))
    print('Você foi aprovado com nota {:.1f} e seu conceito foi B'.format(media))

elif media >= 6.00 and media < 7.50:
    print('Sua primeira nota foi {:.1f}'.format(nota1))
    print('Sua segunda nota foi {:.1f}'.format(nota2))
    print('Você foi aprovado com nota {:.1f} e seu conceito foi C'.format(media))

elif media >= 4.00 and media < 6.00 :
    print('Sua primeira nota foi {:.1f}'.format(nota1))
    print('Sua segunda nota foi {:.1f}'.format(nota2))
    print('Você foi reprovado com nota {:.1f} e seu conceito foi D'.format(media))

elif media >= 0.00 and media < 4.00 :
    print('Sua primeira nota foi {:.1f}'.format(nota1))
    print('Sua segunda nota foi {:.1f}'.format(nota2))
    print('Você foi reprovado com nota {:.1f} e seu conceito foi E'.format(media))

else:
    print('Digite uma nota')