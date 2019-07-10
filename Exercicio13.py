#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

print('Descubra o dia da semana')

dia = int(input('Digite um número que equivale a um dia da semana: '))

if dia == 1:
    print('É domingo!')

elif dia == 2:
    print('É segunda-feira!')

elif dia == 3:
    print('É terça-feira!')

elif dia == 4:
    print('É quarta-feira!')

elif dia == 5:
    print('É quinta-feira!')

elif dia == 6:
    print('É sexta-feira!')

elif dia == 7:
    print('É sábado!')

else:
    print('Esse valor não equivale a um dia da semana')