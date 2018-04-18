''' Convertir FLAGS crudos en Lista de FLAGS

Dado un archivo donde esten los flags como estan descritos al seleccionar la columna flags del archivo word
Nos devuelve una lista de strings con sus nombres flags listos para ser mapeados.

Por default el archivo se encuentra ubicado en:
"C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\TXs\\flags"

ej archivo:
A(LFLAG)
N(LHORA)
N(LMONTO)

ej return:
['LFLAG','LHORA','LMONTO]

ej uso:
LISTA = crudo_to_flag("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\TXs\\flags")

Hay problemas con Flags con Ñ, tener cuidado.

'''
import re

ruta_def = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\TXs\\flags"

def crudo_to_flag(ruta = ruta_def):
   
    flags  = open(ruta, 'r')
    Lflags = flags.readlines()

    stringazo = ""
    Listado = []
    for flag in Lflags:
        patronA_N = r"A\(|N\(|H\(|C\("
        stringazo = re.sub(patronA_N,'', flag)

        patronComma_Space = r", "
        if re.search(patronComma_Space,stringazo):
            stringazo = re.split(patronComma_Space,stringazo)
            Listado.append(stringazo[0])
            # for item in stringazo:
            #     patronCierre_N = r"\)\n"
            #     item = re.sub(patronCierre_N, '',item)
            #     Listado.append(item)
            stringazo = ""

        else:
            patronCierre_N = r"\)\n"
            stringazo = re.sub(patronCierre_N, '',stringazo)
                            
            Listado.append(stringazo)
            stringazo = ""
        
    return Listado


