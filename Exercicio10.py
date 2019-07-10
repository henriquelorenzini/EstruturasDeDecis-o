#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

letra = input('Em que turno você estuda? Digite apenas a primeira letra  ')

if letra == 'm':
    print('Bom dia!!')

elif letra == 'v':
    print('Boa tarde!!')

elif letra == 'n':
    print('Boa noite!!')

else:
    print('Valor inválido')