# trabajo con archivos de texto en python
# primero vamos a crear un archivo de texto llamado "my_notes.txt"
#vamos a escribir algunas notas dentro

with open("my_notes.txt", "w") as file:  #abrimos el archivo en modo escritura ("w")
    file.write("primera nota: estoy aprendiendo python. \n")
    file.write("segunda nota: hoy practicamos archivos de texto. \n")
    file.write("tecercera nota: el uso de Github es importante para guardar proyectos. \n ")

#cuando usamos "with open(...)" no hace falta cerrar el archivo, ya que python lo hace automaticamente.

#ahora vamos a abrir el archivo que acabamos de crear
#esta vez lo abriremos en modo lectura

with open("my_notes.txt", "r") as file:
    linea = file.readline()  #leemos la primera linea
    while linea:  #lineas por leer
        print(linea.strip()) #imprimimos la linea sin saltos de linea extra
        linea = file.readline() #pasamos a la siguiente linea

#aqui al igual que el paso anterior, el archivo se cierra solo al salir del bloque "with"

#y se muestra un mensaje final para confirmar que salio bien

print("\n El erchivo fue leido y cerrado correctamente")
