''' FlagToLength

Dado un archivo que contenga los Flags como se ven en la documentación word
Los pone en limpio para analizar y
Nos muestra:
una lista de Flag (strings declarados en dic_trad)
la misma lista mapeada con sus valores correspondiente
y su suma

'''
dic_trad={"LCANTEFECTPRODUCTOS":2,
            "LCANTTARJ":2,
            "LCLAVE":4,
            "LCODOP":4,
            "LCODPOST":5,
            "LCODRET":3,
            "LCOMPROBANTE":8,
            "LCONCEPTO":2,
            "LDESCSERV":-1,
            "LDIASDESC":3,
            "LDOC":15,
            "LDOM":50,
            "LESTADOOP":3,
            "LESTADO":2,
            "LFECHA":8,
            "LFLAG":1,
            "LHORA":6,
            "LLOC":25,
            "LMESSBIENVENIDA":80,
            "LCODIGOERROR":2,
            "LMESSFROMBRIS":80,
            "LMONEDA":2,
            "LMONTO":14,
            "LNACIONALIDAD":3,
            "LNOMBRESUC":50,
            "LNUMCAJ":5,
            "LNUMREF":8,
            "LOBSERVACIONES":254,
            "LOPERADORA":3,
            "LPARTEDEC":2,
            "LPARTEDEC4":4,
            "LPARTEDEC6":6,
            "LPLAZO":3,
            "LPRODUCTO":20,
            "LPROV":25,
            "LRAZONSOCIAL":50,
            "LRECLAMO":2,
            "LSESSIONID":8,
            "LSUCURSAL":3,
            "LTASA":5,
            "LTEL":16,
            "LTIPODOC":3,
            "LTIPOOP":2,
            "LTIPOPAGO":2,
            "LTIPOPRODUCTO":1,
            "LTIPOSERV":2,
            "LCBU":23,
            "LESEMPLEADO":2,
            "LEMPLEADO":2,
            "LCODIGOFONDO":2,
            "LTIPOFONDO":2,
            "LVALORCUOTAPARTE":12,
            "LPARTEDECIMALCUOTAPARTE":6,
            "PARTEDECIMALCP":6, ##
            "LCANTIDADCUOTASPARTE":16,
            "LDESCRIPCIONFONDO":30,
            "LRENDIMIENTO":12,
            "LMONEDAFCI":20,
            "LCODMONEDAFCI":2,
            "LCODIGOMONEDAFCI":2, ##
            "LFECHAFCI":10,
            "LCODPOSTDE8":8,
            "LCATEGORIAUSUARIO":1,
            "LPRODUCTORESUMIDO":10,
            "LNROINVERSOR":13,
            "LDESCRIPCION":20,
            "LCODOPERACION":2,
            "LTITULO":50,
            "LINFORMACION":5000,
            "LBANCO":30,
            "LNODO":4,
            "LRAZSOCIAL":50,
            "LMOTIVO":30,
            "LTELEFONO":30,
            "LOBS":80,
            "LCATEGORIACIS":10,
            "LNROINVERSOR":13,
            "LBLANCOS":10,
            "LCODIGOMONEDA":1,
            "LNCUOTAS":4,
            "LNCUOTA":4, ##
            "LDIAS":3,
            "LTIPOPRESTAMO":3,
            "LTASAPRESTAMO":7,
            "LDESCPRESTAMO":30,
            "LREFER":22,
            "LENTE":5,
            "LSUBENTE":3,
            "LMESAÑO":6,
            "LMESANO":6, ##
            "LCODIS":4,
            "LCOCAN":3,
            "LCOSIT":15,
            "LCOSITADI":10,
            "LOBSCRM":256,
            "LNOMBRE":35,
            "LSEGMENTO":50,
            "LOFICIAL":64,
            "LOFICIAL1":6,
            "LIR":5,
            "LCODCOM":4,
            "LDESCOM":30,
            "LCANTIDAD":3,
            "LCANT":3,
            "LCATDES":32,
            "LPRODES":30,
            "LDESEST":32,
            "LDESESTABR":8,
            "LDESIS":50,
            "LDESISABR":25,
            "LDESCRI":255,
            "LDESBEN":512,
            "LFECHASTR":10,
            "LIDCLIENTE":12,
            "LIDBANELCO":19,
            "LCTACTECR":10,
            "LCATEIVA":3,
            "LTIPOTTASA":1,
            "LPLAZOEXLO":4,
            "LCODCOMPANIA":3,
            "LMONEDAEXLO":1,
            "LTIO":3,
            "LAUX":3,
            "LIDULTMO":2,
            "LIP":15,
            "LARCHIVO":20,
            "LULTIMPRE":5,
            "LAGENT":5,
            "LPOSICION":4,
            "LSPLIT":4,
            "LTELEFFAX":13,
            "LCANTAVISOS":4,
            "LCODBCO":5,
            "LCUIT":11,
            "LPRODUCTOMAILTARJETA":20,
            "LMESSAGEFROMONLINE":80,
            "LMESSFROMONLINE":80,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "\n":0}

import crudoToList as CtL

def transformar_flag(FLAG):
    if type(FLAG) == type(4): return FLAG
    try:
        return dic_trad[FLAG]
    except:
        return int(FLAG)

def transformar_lista(Lista):
    Lista_mapeada = list(map(transformar_flag, Lista))
    return Lista_mapeada

def flag_to_length(ruta):
    flags = CtL.crudo_to_flag(ruta)

    resultado = ""

    resultado = resultado + "Flags a mapear = " + str(flags) + "\n"
    resultado = resultado + "Flags mapeados = " + str(transformar_lista(flags)) + "\n"
    resultado = resultado + "Tamaño paquete = " + str(sum(transformar_lista(flags))) + "\n"

    return resultado


