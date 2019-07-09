#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

print('Veja se você foi aprovado ou não')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7.00 and media < 10:
    print('Sua média foi {:.1f} e você está aprovado!'.format(media))

elif media < 7:
    print('Sua média foi {:.1f} e você está reprovado!'.format(media))

elif media == 10:
    print('Sua media foi {:.1f} e você foi aprovado com distinção'.format(media))

