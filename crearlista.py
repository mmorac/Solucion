import pandas as pd
import os


def crearlista(archivo_entrada):

    #Dirección para guardar el archivo de salida, que sería en la carpeta del perfil de usuario
    archivo_salida = os.environ['USERPROFILE'] + "\\Documents\\people.out"

    try:
        #Abrir, leer y cerrar el archivo de entrada
        f = open(archivo_entrada, "r", encoding="UTF-8")
        texto = f.read()
        f.close()
    except Exception:
        return "Error en el archivo de entrada"

    #Convertir el texto en un arreglo separado por líneas
    texto = texto.split("\n")

    arreglo = []

    #Convertir el archivo en un arreglo de arreglos, donde cada arreglo atómico es cada línea separada por pipes "|"
    for linea in texto:
        lst = linea.split("|")

        if(len(lst) > 1):
            try:
                lst[-1] = int(lst[-1])
            except ValueError:
                lst[-1] = 0

            try:
                lst[-2] = int(lst[-2])
            except ValueError:
                lst[-2] = 0

        arreglo.append(lst)

    #Crear DataFrame para manipular la información
    df = pd.DataFrame(arreglo, columns = ["PersonId", "Name", "LastName", "CurrentRole", "Country", "Industry", "NumberOfRecommendations", "NumberOfConnections"])

    #Ordenar por cantidad de recomendaciones
    ordenado = df.sort_values(by=["NumberOfRecommendations"], ascending=False)

    #Obtener las primeras 100 filas
    exportar = ordenado.head(100)

    #Exportar únicamente la columna PersonId sin index ni título
    encabezado = ["PersonId"]
    exportar.to_csv(archivo_salida, columns = encabezado, index=False, header = False)

    return "Archivo exitosamente procesado"
