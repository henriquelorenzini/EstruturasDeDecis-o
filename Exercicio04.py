#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('Verifique se a letra é uma vogal ou uma consoante')

letra = input('Digite uma letra: ')

vogal = ['a','e','i','o','u']

if letra == vogal:
    print('A letra {} é uma vogal'.format(letra))

else:
    print('A letra {} é uma consoante'.format(letra))