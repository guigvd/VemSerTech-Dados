
# CRIANDO DICIONÁRIOS
dicionario = []
dicionario = dict()
dicionario = { 'nome': 'Daniel', 'idade': 26, 'altura': '1.77'}

print(dicionario)

# ADICIONANDO ELEMENTOS
dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# ITERANDO UM DICIONARIO
for chave in dicionario:
    print(chave, dicionario[chave])

# VERIFICA SE TEM UMA CHAVE
print('peso' in dicionario)
print('altura' in dicionario)