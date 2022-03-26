from tkinter import *
from tkinter import messagebox

# Canvas tasarım
pencere = Tk()
pencere.title("Python GUI")  # Penceremize bir başlık verdik
pencere.geometry("600x500")  # Penceremizi boyutlandırdık


def temizle():
    txt.delete(0, END)


def degistir():
    metin = txt.get()
    yazi["text"] = metin
    temizle()


yazi = Label(pencere, text="Merhaba", fg="Orange",
             font=("Arial", 18))
# Label(elemanın ekleneceği canvas,metni,
# yazı rengi(foreground(önplan)),font(yazıtipi,fontsize))
yazi.place(x=5, y=10)  # place=x,y koordinatlarında pixel ile tanımlanır.

button = Button(pencere, text="Değiştir", font=("Arial", 18), width=20, command=degistir)
button.place(x=300, y=50)

txt = Entry(pencere, text="", bd=3, font=("Arial", 18))
txt.place(x=5, y=45)

button = Button(pencere, text="Temizle", font=("Arial", 18), width=20, command=temizle)
button.place(x=300, y=100)

pencere.mainloop()
