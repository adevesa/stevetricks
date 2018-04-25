#### SpeechRecognizerFiles.py
##
## Primero que nada se necesita Python. Con la versión 3.6.5 32 bits esta funcionando, con las otras versiones se desconoce.
##
## Debemos poner el path a la hora de ejecutar el script. Se cambia desde un editor cualquiera.
## La carpeta SOLO debe contener los audios en formato .FLAC (estos se pueden modificar desde batch processing de GoldWave)
## Utiliza el CloudRecognizer de Google por lo tanto, si no anda es posible que haya vencido el plazo gratuito
##
## Tambien necesita 
## pip install SpeechRecognizer
## pip install google-cloud speech
## pip install pyaudio
## pip3 install google-api-python-client
## 
## se ejecuta de la siguiente forma
## python speechRecognizer.py
## >> Muestra en consola todos los resultados.
## python speechRecognizer.py >> resultados.txt
## >> Guarda en un archivo los resultados para luego visualizarlos.
##
##
## Certius Tech 2018. adevesa.
###


# Acá se setea el path.
path = "C:\\Users\\adevesa\\Documents\\PRUEBAX\\"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

import speech_recognition as sr

r = sr.Recognizer()

for file in onlyfiles:
    with sr.WavFile(path+file) as source:
        audio = r.record(source)
    try:
        print(file + ": " + r.recognize_google(audio,language="es-LA"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
