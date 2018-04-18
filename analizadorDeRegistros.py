''' Analizador de registros vía archivo

Dado un path de un archivo con multiples registros, los analiza y devuelve un string con:
el tamaño de sus requests y responses con su codigo de ResponseEnd y la cantidad de registros

ejemplo:

STRING = analisis_de_registros("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\TXs\\regs")


'''

def tamanio_payload_request(Paquete):
    spliteado = Paquete.split(";")
    ultimo = len(spliteado) - 2
    if len(spliteado[ultimo]) == 55: print(Paquete)
    return len(spliteado[ultimo])

def tamanio_payload_response(Paquete):
    spliteado = Paquete.split(";")
    ultimo = len(spliteado) - 1
    tipoResp = spliteado[3]
    return (tipoResp,len(spliteado[ultimo]))

def nombres_operaciones(Paquete):
    spliteado = Paquete.split(";")
    return (spliteado[4],spliteado[2])

def comparador(uno,otro):
    if uno > otro: return 1
    if uno < otro: return -1
    if uno == otro: return 0

def analisis_de_registros(Ruta):
    ## ruta = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\TXs\\regs"
    ruta = Ruta

    registros  = open(ruta, 'r')
    Lregistros = registros.readlines()

    ReqValores = []
    ResValores = []
    for reg in Lregistros:
        ReqValores.append(tamanio_payload_request(reg))
        ResValores.append(tamanio_payload_response(reg))

    ReqValores = set(ReqValores)
    ResValores = set(ResValores)
    # Lvalores = sorted(Lvalores,key=lambda x: int(x[1]))

    resultado = ""

    resultado = resultado + "Cantidad de registros: " + str(len(Lregistros)) + "\n"
    resultado = resultado + "Tamanio Payloads Requests: " + str(ReqValores) + "\n"
    resultado = resultado + "Tamanio Payloads Responses: " + str(ResValores)

    registros.close()

    return resultado
