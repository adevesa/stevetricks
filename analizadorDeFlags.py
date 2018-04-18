''' Analizador de Flags

Dado un pathIN donde estan los flags de requests
un flagOUT donde estan los flags de responses

los dos directorios deben tener la misma cantidad de archivos

Analiza uno por uno y crea un archivo en el directorio pathAnalize
con su correspondiente analisis.

ej:
analizar_flags("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\FlagsIN",
"C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\FlagsOUT",
"C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\AnalisisFlags")


'''

from FlagToLength import flag_to_length
from os import listdir
from os.path import isfile, join

def analizar_flags(pathIN, pathOUT, pathAnalize):

    TXs = [f for f in listdir(pathIN) if isfile(join(pathIN, f))] ## Nombres de los TXs


    for tx in TXs:
        
        ruta_IN = pathIN + "\\" + tx
        ruta_OUT = pathOUT + "\\" + tx

        resultado = "---Analísis de Flags de entrada--- \n"
        resultado = resultado + flag_to_length(ruta_IN)

        resultado += "---Analísis de Flags de salida--- \n"
        resultado = resultado + flag_to_length(ruta_OUT)

        ruta_a_escribir = pathAnalize + "\\" + tx
        arc_w  = open(ruta_a_escribir, 'w')
        arc_w.write(resultado)
        arc_w.close()
    
analizar_flags("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\FlagsIN",
"C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\FlagsOUT",
"C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Transacciones\\AnalisisFlags")
        


