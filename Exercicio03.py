#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print('Programa para explicar o que significa as letras informadas para definir um sexo')

letra = input('Digite uma letra: ')

if letra == 'f':
    print('O sexo é feminino')

elif letra == 'm':
    print('O sexo é masculino')

else:
    print('Sexo inválido')