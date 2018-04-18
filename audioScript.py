path = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Para subir a HSBC\\Para subir a HSBC\\tablaAudios.csv"

lista = []

import csv
with open(path, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            lista.append([row[0], row[2], row[3], row[4]])

lista2 = []

for elem in lista:
    if elem[2] != '': lista2.append(elem)

pathAudios = "C:\\Users\\adevesa\\Documents\\Certius Info\\HSBC\\Para subir a HSBC\\Para subir a HSBC\\"

from shutil import copyfile

for elem in lista2:
    copyfile(pathAudios+elem[0],pathAudios+'prueba\\'+elem[1]+'.wav')
    copyfile(pathAudios+elem[0],pathAudios+'prueba\\'+elem[2]+'.wav')
    copyfile(pathAudios+elem[0],pathAudios+'prueba\\'+elem[3]+'.wav')