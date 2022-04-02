from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from Veritabani import Veritabani
from Grafik import Grafik
import threading
from Kur import Kur


class Doviz:
    pencere = Tk()
    tab_control = Notebook(pencere)
    tab_altin = Frame(tab_control)
    tab_dolar = Frame(tab_control)
    tab_euro = Frame(tab_control)

    tab_control.add(tab_altin, text="Altın")
    tab_control.add(tab_dolar, text="Dolar")
    tab_control.add(tab_euro, text="Euro")

    tab_control.grid(row=0, column=0, ipadx=10, ipady=10)

    @classmethod
    def zamanFormat(cls, zamanStr):
        zamankisa = []

        for z in zamanStr:
            zmn = datetime.strptime(z, '%d.%m.%Y %H:%M:%S')
            zmn = zmn.strftime("%d.%m %H:%M")
            zamankisa.append(zmn)
        return zamankisa

    @classmethod
    def tekrar(cls):
        komut = "SELECT zaman,kur FROM tb_altin ORDER BY(zaman) DESC"
        altinKur = Veritabani.kurGetir(komut)
        x = [row[0] for row in altinKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in altinKur]
        Grafik.Ciz(cls.tab_altin, xf, y, 'Altın Kuru')

        komut = "SELECT zaman,kur FROM tb_dolar ORDER BY(zaman) DESC"
        dolarKur = Veritabani.kurGetir(komut)
        x = [row[0] for row in dolarKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in dolarKur]
        Grafik.Ciz(cls.tab_dolar, xf, y, 'Dolar Kuru')

        komut = "SELECT zaman,kur FROM tb_euro ORDER BY(zaman) DESC"
        euroKur = Veritabani.kurGetir(komut)
        x = [row[0] for row in euroKur]
        xf = cls.zamanFormat(x)
        y = [row[1] for row in euroKur]
        Grafik.Ciz(cls.tab_euro, xf, y, 'Euro Kuru')

        altin = threading.Thread(target=Kur.getir, args=["altin"])
        dolar = threading.Thread(target=Kur.getir, args=["dolar"])
        euro = threading.Thread(target=Kur.getir, args=["euro"])

        altin.start()
        dolar.start()
        euro.start()

        cls.pencere.after(10000, cls.tekrar)


altin = threading.Thread(target=Kur.getir, args=["altin"])
dolar = threading.Thread(target=Kur.getir, args=["dolar"])
euro = threading.Thread(target=Kur.getir, args=["euro"])

altin.start()
dolar.start()
euro.start()

Doviz.tekrar()
Doviz.pencere.mainloop()
