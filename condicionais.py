# CONDICIONAIS

idade = 20

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

###########

media = float(input("Digite a média: "))
presenca = float(input('Digite a presença: '))

if media >= 7 and presenca >= 70:
    print('Aprovado')
elif media >= 5 and presenca >= 70:
    print('Recuperação')
else:
    print('Reprovado')