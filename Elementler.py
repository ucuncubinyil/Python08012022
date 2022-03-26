from tkinter import *

window = Tk()
window.geometry("700x700")

yazi = Label(window, text="Merhaba Grafik", fg="Purple", font=("Consolas", 24))
yazi.place(x=5, y=10)

button = Button(window, text="Beni Değiştir", font=("Consolas", 24))
button.place(x=300,y=10)

girilenMetin =  Entry(window, text="", bd=3, font=("Consolas", 24))
girilenMetin.place(x=5,y=100)

window.mainloop()
