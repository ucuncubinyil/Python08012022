from tkinter import *
from tkinter import  messagebox

window = Tk()

window.title("Python Kursu")
window.geometry("500x600")

uygulama = Frame(window)
uygulama.grid()

def dialog():
    var = messagebox.showinfo("Uyarı", "Merhaba ben sadece bilgilendirme amaçlı oluşturuldum")


def dialog2():
    var = messagebox.askyesno("Uyarı", "Merhaba ben sadece bilgilendirme amaçlı oluşturuldum")


button1 = Button(uygulama, text=" uyarı  ", width=50, height=30, command=dialog)
button1.grid(padx=110, pady=80)

button2 = Button(uygulama, text=" hata ", width=50, height=30, command=dialog2)
button2.grid(padx=10, pady=60)

window.mainloop()

