# Sesli kontrol sistemi
# pip install pipwin
# pipwin install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Bişeyler söyle")
    audio = r.listen(source)

try:
    print("Söylediğiniz cümle :  " + r.recognize_google(audio, language="tr"))
except sr.UnknownValueError:
    print("Google speech  sesi anlayamadı")
except sr.RequestError as e:
    print("Ses isteği hatası : {0}".format(e))
