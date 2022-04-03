buyukAlfabe = "ABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefghıijklmnoöprsştuüvyz"

def lower(text: str):
    newText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            newText += kucukAlfabe[index]
        else:
            newText += i
    return newText


import speech_recognition as sr
from os import system as komut

r = sr.Recognizer()
with sr.Microphone() as source:
    komut("cls")
    print("Bişeyler söyle")
    audio = r.listen(source)

flag = False

try:
    text = r.recognize_google(audio, language="tr")
    print("Algılanan: " + text)
    text = lower(text)
except sr.UnknownValueError:
    print("Google sesi anlayamadı")
except sr.RequestError as e:
    print("İstek yapılırken hata oluştu : {0}".format(e))

if flag:
    if text == "hesap makinesi":
        komut("calc")
    elif text == "haberleri aç":
        komut("start chrome www.haberler.com")
