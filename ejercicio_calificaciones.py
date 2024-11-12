"""
Mariana Izquierdo Preciado
8 de noviembre de 2024
Este programa sirve para crear un documento con el promedio de una lista de alumnos
que se encuentra en otro archivo.
"""
#Establecer función
def alumnos_promedio(archivo_entrada, archivo_salida):
    "Calcular promedio"
    #Abre el archivo del que se obtendrá la información
    with open(archivo_entrada,"r", encoding="utf8") as entrada:
        #Crea el archivo en el que se escribirá la información
        with open(archivo_salida, "w", encoding="utf8") as salida:
            for linea in entrada:
                separar= linea.split(" ")
                nombre= separar[0]
                apellido= separar[1]
                calificaciones= (separar[2:])
                #Convierte cada elemento de la lista calificaciones en float
                calis=(float(x) for x in calificaciones) 
                promedio= sum(calis)/len(calificaciones)
                promedio_round= round(promedio, 1)
                salida.write(f"{apellido.upper()}, {nombre}: {promedio_round}\n")
#Rutas
archivo_entrada= "data/calificaciones.txt"
archivo_salida= "data/promedios.txt"
#Ejecutar función
alumnos_promedio(archivo_entrada, archivo_salida)