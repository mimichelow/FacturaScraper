from pdfminer.high_level import extract_text
from pathlib import Path
import pandas as pd


def facturascraper(carpetaOrigen="./facturasPendientes", archivoDestino="nuevasFacturasConvertidas.csv"):
    def extraerInfo(direccionArchivo):
        respuesta = {}
        texto = extract_text(direccionArchivo)
        texto = texto.split("\n")
        for linea in texto:
            linea.strip()

        texto = [linea for linea in texto if linea != ""]

        print(texto)

        for n in range(len(texto)):

            if "Giro:" in texto[n] and "NOMBRE EMISOR" not in respuesta:
                respuesta["NOMBRE EMISOR"] = texto[0]
                if n > 0:
                    for lineasExtra in range(1, n):
                        respuesta["NOMBRE EMISOR"] = respuesta["NOMBRE EMISOR"] + f" {texto[lineasExtra]}"
                        respuesta["NOMBRE EMISOR"] = respuesta["NOMBRE EMISOR"].strip()

            if texto[n] == "GIRO:":
                respuesta["RUT RECEPTOR"] = texto[n + 1]

            if "SEÑOR" in texto[n]:
                marcador = texto[n].index(":")
                respuesta["NOMBRE RECEPTOR"] = texto[n][marcador + 1:]
                for lineasExtra in range(1, 4):
                    if ":" in texto[n + lineasExtra]:
                        break
                    else:
                        respuesta["NOMBRE RECEPTOR"] = respuesta["NOMBRE RECEPTOR"] + f" {texto[n + lineasExtra]}"
                respuesta["NOMBRE RECEPTOR"] = respuesta["NOMBRE RECEPTOR"].strip()

            if "R.U.T.:" in texto[n] and len(texto[n]) > 8:
                marcador = texto[n].index(":")
                respuesta["RUT EMISOR"] = texto[n][marcador + 1:]

            if "MONTO NETO $" in texto[n]:
                respuesta["MONTO NETO"] = texto[n + 1]
                respuesta["MONTO NETO"] = int(respuesta["MONTO NETO"].replace(".",""))


            if "I.V.A. 19%" in texto[n]:
                respuesta["IVA"] = texto[n + 1]
                respuesta["IVA"] = int(respuesta["IVA"].replace(".",""))

            if "Timbre Electr" in texto[n]:
                respuesta["TOTAL"] = texto[n - 1]
                respuesta["TOTAL"]=int(respuesta["TOTAL"].replace(".",""))

            if "FACTURA ELECTRONICA" in texto[n]:
                marcador = texto[n + 1].index("º")
                respuesta["FOLIO"] = texto[n + 1][marcador + 1:]

            if "Fecha Emision" in texto[n]:
                marcador = texto[n].index(":")
                respuesta["FECHA"] = texto[n][marcador + 2:]
        return respuesta

    diccionarioRespuesta = []

    for child in Path(carpetaOrigen).iterdir():
        if child.is_file():
            diccionarioRespuesta.append(extraerInfo(carpetaOrigen + "/" + child.name))

    df = pd.DataFrame.from_dict(diccionarioRespuesta)
    df.to_csv(rf"{archivoDestino}", index=False, header=True)
