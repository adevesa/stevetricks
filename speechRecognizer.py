#### SpeechRecognizerFiles.py
##
## Debemos poner el path a la hora de ejecutar el script
## La carpeta SOLO debe contener los audios en formato .FLAC
## Utiliza el CloudRecognizer de Google por lo tanto, si no anda es posible que haya vencido el plazo gratuito
##
## Tambien necesita pip install SpeechRecognizer
## pip install google-cloud speech
## pip install pyaudio
## pip3 install google-api-python-client
## 
##
###



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