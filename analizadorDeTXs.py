''' Analizador de registros vía archivo

Dado un directorio con multiples archivos con multiples registros, 
los analiza y nos escribe en el directorio destino:
la cantidad de registros
el tamaño de sus requests 
el tamaño de sus responses con su codigo de ResponseEnd

ejemplo:
analizador_de_txs("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Analisis de Filtrados\\",
                  "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Filtrados\\")


'''

from analizadorDeRegistros import analisis_de_registros

from os import listdir
from os.path import isfile, join

def analizador_de_txs(pathWrite,pathRead):

    ## ruta_escritura = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Analisis de Filtrados\\"
    
    ## ruta_lectura = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Filtrados\\"

    TXs = [f for f in listdir(pathRead) if isfile(join(pathRead, f))]

    for tx in TXs:
        ruta_a_escribir = pathWrite + tx
        arc_w  = open(ruta_a_escribir, 'w')

        analisis = analisis_de_registros(pathRead + tx)

        arc_w.write(analisis)

        arc_w.close()
        
