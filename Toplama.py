from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Toplama")
pencere.geometry("500x100")

def toplamaIslemi(sayi1, sayi2):
    return sayi1 + sayi2


lblSayi1 = Label(pencere, text="Sayı 1", font=("Consolas", 12))
lblSayi1.place(x=0, y=0)

sayi1 = Entry(pencere, text="")
sayi1.place(x=150, y=0)

lblSayi2 = Label(pencere, text="Sayı 1", font=("Consolas", 12))
lblSayi2.place(x=0, y=50)

sayi2 = Entry(pencere, text="")
sayi2.place(x=150, y=50)

def hesapla():
    sonuc =  str(toplamaIslemi(int(sayi1.get()),int(sayi2.get())))
    var = messagebox.showinfo("Uyarı", "Merhaba sonuç : "+ sonuc)

hesaplaButton = Button(pencere, text="Hesapla", font=("Consolas", 12), command=hesapla)
hesaplaButton.place(x=300, y= 30)

pencere.mainloop()
