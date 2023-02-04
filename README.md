# What is this?¿Qué Es Esto?
facturascraper is meant to fulfill a very local use-case, as such we will explain the gist in this intro but will not be discussing the workings in english any further. This function takes a folder path and a filename to scrape the folder for official Chilean commercial invoices as pdf files, it will take all invoices and extract issuer name, id number, client name, bill number, total cost, tax, total plus tax, date and invoice serial number and store it in the filename.csv file as a CSV.

facturascraper es una función diseñada para tomar todas las facturas (de emisión electronica y Chilena) en una carpeta por la siguiente información:
>NOMBRE EMISOR,RUT EMISOR,FOLIO,FECHA,NOMBRE RECEPTOR,RUT RECEPTOR,MONTO NETO,IVA,TOTAL

Esta será guardada en un archivo en formato CSV.

# ¿Cómo Usar?
La función facturaScraper toma dos argumentos:

>*carpetaOrigen* es la ruta de archivo a la carpeta donde se encuentran las facturas a utilizar. Por defecto se usa ./facturasPendientes

>*archivoDestino* es el nombre del archivo donde se guardará la información extraida, en formato csv. Por defecto se usa nuevasFacturasConvertidas.csv

# Futuro Del Proyecto
Este proyecto cumple las metas personales establecidas, por lo que se considera finalizado.