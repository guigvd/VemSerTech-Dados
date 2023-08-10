# CRIANDO LISTAS

notas = [7, 9, 8]
lista1 = []
lista2 = list()
lista3 = [10, 'Daniel', False]
listaDeListas = [10, [1, 2, 3]]

print(lista3[1])
print(listaDeListas[1])

for elemento in notas:
    print(elemento)


# FUNÇÕES

# LEN
print(len(notas))

# SUM
print(sum(notas))

# MIN
print(min(notas))

# MAX
print(max(notas))

# MÉTODOS DE LISTA

exemplo = [1, 3, 12, 8, 2]
print(exemplo)

# APPEND
exemplo.append(3)
print(exemplo)

# INSERT
exemplo.insert(0, 10)
print(exemplo)

exemplo2 = [9, 8, 7]

# EXTEND
exemplo.extend(exemplo2)
print(exemplo)

# POP
exemplo.pop(0)
print(exemplo)

# REMOVE
exemplo.remove(2)
print(exemplo)

# COUNT
print(exemplo.count(3))

# INDEX
print(exemplo.index(12))

# SORT
exemplo.sort(reverse=True)
print(exemplo)
