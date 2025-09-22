#creacion del diccionario con la informacion inicial

print("\n se muestra la informacion personal: ")
informacion_personal = {

    "nombre": "Emily",
    "apellido": "Robles",
    "edad": "22",
    "ciudad": "Guayaquil",
    "profesion": "Estudiante",

}

# se accede al valor asociado con ciudad y modificarlo

print("ciudad original: ", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Daule"  #cambiamos la ciudad
print ("ciudad modificada: ", informacion_personal["ciudad"])

 #agregamos o modificamos la clave profesion
 #en caso que la clave exista, al asignarla de nuevo estamos actualizando su valor

informacion_personal["profesion"] = "fotografa"
print("profesion actual: ", informacion_personal["profesion"])

 # verifiamo si la clave telefono existe; si esta no existe, lo agregamos

if "telefono" not in informacion_personal:
     informacion_personal["telefono"] = "0954672314"  #numero de telefono ficticio
     print("telefono agregado: ", informacion_personal["telefono"])
else:
     print("telefono ya existente: ", informacion_personal["telefono"])

#eliminar la clave edad ya que no es necesaria
#usamos .pop con segundo argumento para asi evitar error si no existe

informacion_personal.pop("edad", None)
print("clave 'edad' eliminada (en caso que existiera).")
#impriminos el diccionario final

print("\n Diccionario final: ")
print(informacion_personal)