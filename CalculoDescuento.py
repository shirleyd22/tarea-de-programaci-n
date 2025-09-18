def calcular_descuento(monto, porcentaje=10):
    """
    se calcula y se devuelve el monto del descuento
    parametros:
    monto: es el total de la compra ya sea en numero entero o decimal
    porcentaje: porcentaje de descuento que es el 10%
    """

    descuento= monto * porcentaje/100
    return descuento

if __name__ == '__main__':
    #primer llamada: solo el monto el cual usa el 10% por defecto
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print("compra 1")
    print(f"monto: { monto1:.2f}")
    print(f"descuento: { descuento1:.2f}")
    print(f"total: { total1:.2f}")
    print("-"*30)

    #se hace el segundo llamado: monto mas el porcentaje
    monto2 = 200.0
    descuento2 = calcular_descuento(monto2, 15)
    total2 = monto2 - descuento2
    print("compra 2")
    print(f"monto: { monto2:.2f}")
    print(f"descuento: { descuento2:.2f}")
    print(f"total: { total2:.2f}")