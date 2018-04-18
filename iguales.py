''' Detector de igualdad '''

ruta = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Ofuscados.csv"
ruta2 =  "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Info\\Ofuscados.txt"

Fcsv  = open(ruta, 'r')
LFcsv = Fcsv.readlines()

Ftxt  = open(ruta2, 'r')
LFtxt = Ftxt.readlines()

n = 0

while True:
    if LFcsv[n] == LFtxt[n]: print("Iguales")
    else: pass
    n += 1

