def alumnos_promedio(archivo_entrada, archivo_salida):
    "Calcular promedio"
    with open(archivo_entrada,"r", encoding="utf8") as entrada:
        with open(archivo_salida, "w", encoding="utf8") as salida:
            for linea in entrada:
                separar= linea.split(" ")
                nombre= separar[0]
                apellido= separar[1]
                calificaciones= (separar[2:])
                calis=(float(x) for x in calificaciones)
                promedio= sum(calis)/len(calificaciones)
                promedio_round= round(promedio, 1)
                salida.write(f"{apellido.upper()}, {nombre}: {promedio_round}\n")

archivo_entrada= "data/calificaciones.txt"
archivo_salida= "data/promedios.tx"

alumnos_promedio(archivo_entrada, archivo_salida)