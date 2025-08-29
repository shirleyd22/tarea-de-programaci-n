def ordena_fila(fila):
    longitud = len(fila)
    for i in range (longitud):
        for j in range (0, longitud - i - 1):
            if fila[j + i] > fila[j + i + 1]:

                fila[j],fila[j + 1] = fila[j + 1], fila[j]
    return fila

matriz = [
    [9, 6, 8],
    [2, 1, 7],
    [3, 5, 4]
]
numero_de_fila = int(input("¿que fila desea ordenar? (0, 1 o 2): "))
print("matriz antes de ordenar la fila: ")
for fila in matriz:
    print(fila)
if 0 <= numero_de_fila < len(matriz):
    matriz[numero_de_fila]=ordena_fila(matriz[numero_de_fila])
    print("\nMatriz después de ordenar la fila: ")
    for fila in matriz:
        print(fila)
else:
    print("No existe la matriz de ordenada.")

