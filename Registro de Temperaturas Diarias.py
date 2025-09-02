ciudades = [ "Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
num_semanas = 2

temperaturas = [
    [
        [15.5, 14.8],
        [16.0, 15,6],
        [14.8, 16.3],
        [17.1, 16.2],
        [15.2, 15.8],
        [14.9, 15.4],
        [17.0, 16.7]
    ],
    [
        [28.2, 27.5],
        [29.5, 28.2],
        [30.1, 29.5],
        [28.6, 27.9],
        [29.0, 29.3],
        [30.5, 30.1],
        [31.3, 29.9]
    ],
    [
        [18.0, 17,6],
        [19.0, 18.4],
        [18.8, 18.7],
        [17.9, 18.3],
        [18.3, 18.2],
        [17.5, 18.0],
        [18.9, 18.7]
    ]
]

for i, ciudad in enumerate(ciudades):
    print(f"\n Promedios de temperatura para {ciudad}: ")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += temperaturas[i][dia][semana]
        promedio = suma / len(dias)
        print(f" semana {semana + 1}: {promedio: .1f} °C")