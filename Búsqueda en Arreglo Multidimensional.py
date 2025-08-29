def busca_valor (matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz [i][j]== valor:
                return True,(i, j)
    return False, None

matriz = [
    [5, 8, 3],
    [1, 9, 4],
    [6, 2, 7],
]
valor_a_buscar = int(input("por favor ingresa el valor a buscar: "))
encontrado, posicion= busca_valor(matriz, valor_a_buscar)
if encontrado:
    print(f"valor { valor_a_buscar} encontrado en la posicion {posicion}. ")
else:
    print(f"valor { valor_a_buscar} no se pudo encontrar el valor en la matriz.")