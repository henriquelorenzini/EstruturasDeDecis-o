# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Responda as perguntas apenas com Sim e Não, será verificado o quão suspeito você é em relação ao assassinato')

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]
resposta = 0
for qual in perguntas:
    resposta += (input(qual) == "Sim")

if resposta == 5:
    print("Você é o Assassino")
elif resposta >= 3:
    print("Você é Cúmplice")
elif resposta == 2:
    print("Você é Suspeito")
else:
    print("Você é Inocente")