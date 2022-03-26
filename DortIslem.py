from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Python Dört İşlem")
pencere.geometry("650x200")


def sayisalMi(s1):
    s1 = str(s1)
    if s1.isdigit():
        return True
    else:
        return False


def hataBas():
    messagebox.showerror("HATA", "Değerler sayısal olmalıdır")


def topla():
    s1 = txt_sayi1.get()
    s2 = txt_sayi2.get()
    if sayisalMi(s1) and sayisalMi(s2):
        sonuc = int(s1) + int(s2)
        txt_sonuc.delete(0, END)
        txt_sonuc.insert(0, str(sonuc))
    else:
        hataBas()


def cikar():
    s1 = txt_sayi1.get()
    s2 = txt_sayi2.get()
    if sayisalMi(s1) and sayisalMi(s2):
        sonuc = int(s1) - int(s2)
        txt_sonuc.delete(0, END)
        txt_sonuc.insert(0, str(sonuc))
    else:
        hataBas()


def carp():
    s1 = txt_sayi1.get()
    s2 = txt_sayi2.get()
    if sayisalMi(s1) and sayisalMi(s2):
        sonuc = int(s1) * int(s2)
        txt_sonuc.delete(0, END)
        txt_sonuc.insert(0, str(sonuc))
    else:
        hataBas()


def bol():
    s1 = txt_sayi1.get()
    s2 = txt_sayi2.get()

    if sayisalMi(s1) and sayisalMi(s2):
        if int(s2) == 0:
            var = messagebox.showerror("HATA!", "Hiç bir sayı sıfıra bölünemez!")
        else:
            sonuc = int(s1) / int(s2)
            txt_sonuc.delete(0, END)
            txt_sonuc.insert(0, str(sonuc))
    else:
        hataBas()


lbl_sayi_1 = Label(pencere, text="1.Sayı: ", font=("Consolas", 16))
lbl_sayi_2 = Label(pencere, text="2.Sayı: ", font=("Consolas", 16))

lbl_sayi_1.place(x=20, y=25)
lbl_sayi_2.place(x=20, y=65)

txt_sayi1 = Entry(pencere, text="", font=("Consolas", 16))
txt_sayi2 = Entry(pencere, text="", font=("Consolas", 16))

txt_sayi1.place(x=120, y=25)
txt_sayi2.place(x=120, y=65)

btn_topla = Button(pencere, text="+", width=5, height=2, font=(20), command=topla)
btn_topla.place(x=120, y=100)

btn_cikar = Button(pencere, text="-", width=5, height=2, font=(20), command=cikar)
btn_cikar.place(x=180, y=100)

btn_carp = Button(pencere, text="X", width=5, height=2, font=(20), command=carp)
btn_carp.place(x=240, y=100)

btn_bol = Button(pencere, text="/", width=5, height=2, font=(20), command=bol)
btn_bol.place(x=300, y=100)

lbl_sonuc = Label(pencere, text="Sonuç: ", font=("Consolas", 16))
lbl_sonuc.place(x=370, y=23)

txt_sonuc = Entry(pencere, text="", font=("Consolas", 16), bd=3)
txt_sonuc.place(x=370, y=63)

pencere.mainloop()
