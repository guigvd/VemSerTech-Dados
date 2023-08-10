numeroSorteado = 6
contador = 0

numeroEscolhido = int(input("Informe um número entre 1 e 10: "))

while numeroEscolhido != numeroSorteado:

    if contador < 5:
        print("Errou :/\nTente novamente...")
        numeroEscolhido = int(input("Informe um número entre 1 e 10: "))
        contador = contador + 1

    else:
        print("Acabaram as tentativas")
        break

if numeroEscolhido == numeroSorteado:
    print('Acertou!!')
