''' Extractor de registros 

Dado un path donde se encuentran archivos ofuscados (.csv en lo preferible)
Un path donde escribir todos los archivos filtrados
Y un diccionario de Transacciones a filtrar (ya tiene un default)

Nos escribe en el path seleccionado, todas las transacciones filtradas declaradas en dic_TransaccionesAFiltrar

ejemplo:

extraer_de_ofuscados("C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Ofuscados.csv", 
                     "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Filtrados")
                     

'''

TransaccionesDefault = {
        "0001":"Generar Sesión",
        "0002":"Identificacion del cliente",
        "0003":"Reset de Clave",
        "0005":"Fin de sesión bancaria.",	
        "0006":"Operaciones pendientes",
        "0008":"Consulta de Cta.Cte",
        "0008":"Consulta de saldos de Cuentas",
        "0009":"Consulta de saldos de Cuentas",
        "0009":"Consulta de caja de Ahorro",
        "0010":"Consulta de Movimientos",
        "0011":"Consulta de Tarjetas",
        "0012":"Consulta de pagos ingresados",
        "0013":"Consulta banelco débito",
        "0015":"Información de cotizaciones",
        "0016":"Hacer transferencias",
        "0017":"Efectuar una CompraVenta",
        "0018":"Pago de tarjeta de crédito",
        "0019":"Efectuar un Plazo Fijo",
        "0021":"Pedido de chequeras",
        "0040":"Pedido de Número de Sesión",
        "0048":"(401)Consulta de Saldos de Cuenta",
        "0049":"Cotitulares de Cuenta",
        "0054":"Consultar calificación FATCA",
        "0060":"Consulta de Tasas de Plazos Fijos",
        "0062":"Pedido de saldos de Fondos",
        "0063":"Pedido de valor de cuotaparte de Fondos",
        "0068":"Estado de Fondos",
        "0070":"Consulta de CBU",
        "0074":"Operaciones Permitidas",
        "0078":"Consulta de saldos disponibles",
        "0079":"Consulta de consumos ingresados",
        "0080":"Consulta de Préstamos",
        "0301":"Setear el N° de Nodo",
        "0302":"Consulta de Plazos Fijos",
        "0313":"Consulta de Préstamos",
        "0314":"Grabar el Préstamo",
        "0316":"Consulta de Débitos automáticos",
        "0317":"Pedidos de Stop Debit",
        "0318":"Consulta de cheques de una Cuenta",
        "0336":"Consulta de Habilitación Banelco/Oasis",
        "0337":"Confirmación de Habilitación Banelco/Oasis",
        "0339":"Grabación de datos Habilitación Banelco/Oasis",
        "0351":"Grabación de clave provisoria",
        "0352":"Consulta de Datos de Reset de Clave Provisoria",
        "0353":"Grabación de datos de la Clave Provisoria",
        "0354":"Obtener Código Individual Solution",
        "0355":"Grabar SAC",
        "0358":"HSBC Rewards Status Subscripción",
        "0360":"Consulta de Puntos HSBC Rewards",
        "0361":"Cuentas no vinculadas a Banelco",
        "0362":"Vincular cuenta a Banelco",
        "0363":"Setear cuenta principal",
        "0364":"Cotización y Disponible para el cliente",
        "0369":"Reset TD PIN",
        "0372":"Monto de la Primer Cuota"}
 
def traer_regs(numTX,LFofuscados):
    numTX =str(numTX)
    Listado = []
    for reg in LFofuscados:
        reg_fixed = ""
        spliteados = reg.split(";")
        if spliteados[2] == numTX: 
            spliteados[7] = "  " + spliteados[7]
            for split in spliteados:
                reg_fixed = reg_fixed + ";" + split
            reg_fixed = reg_fixed[1::]
            Listado.append(reg_fixed)
    return Listado

def traer_regs_nombre(TXName, LFofuscados):
    Listado = []
    for reg in LFofuscados:
        reg_fixed = ""
        spliteados = reg.split(";")
        if spliteados[4] == TXName:
            spliteados[7] == "  " + spliteados[7]
            for split in spliteados:
                reg_fixed = reg_fixed + ";" + split
            Listado.append(reg_fixed)
    return Listado

def traer_necesitados(ruta_ofuscados, ruta_escritura, dic_TransaccionesAFiltrar):
    Fofuscados  = open(ruta_ofuscados, 'r')
    LFofuscados = Fofuscados.readlines()
    
    for tx in dic_TransaccionesAFiltrar:
        numTx = int(tx)
        Listado = traer_regs(numTx,LFofuscados)

        ruta_a_escribir = ruta_escritura + "\\TX " + tx
        arc_w  = open(ruta_a_escribir, 'w')
        arc_w.writelines(Listado)
        arc_w.close()

def extraer_de_ofuscados(pathOfuscados, pathEscritura, dic_TransaccionesAFiltrar = TransaccionesDefault):
    ruta_ofuscados = pathOfuscados
    ## ruta_lectura = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Ofuscados.csv"

    ruta_escritura = pathEscritura
    ## ruta_escritura = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Filtrados"
    
    traer_necesitados(ruta_ofuscados, ruta_escritura, dic_TransaccionesAFiltrar)




