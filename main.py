# python -m pip install -U matplotlib
# Eğer kütüphane yoksa yükle

from matplotlib import pyplot as plt

x_ekseni = [1, 2, 3, 4, 5]
y_ekseni_ayse = [50, 80, 90, 100, 110]
y_ekseni_ali = [40, 60, 100, 105, 130]
y_ekseni_arzu = [55, 70, 110, 115, 150]



plt.plot(x_ekseni, y_ekseni_ayse, color='r', linestyle="dotted", marker="v", label="Ayşe")
plt.plot(x_ekseni,y_ekseni_ali,'k-o', label="Ali")
plt.plot(x_ekseni,y_ekseni_arzu, label="Arzu", color="#3366ff", marker="8", linestyle="dashdot")

#  are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'


# plt.plot(x_ekseni, y_ekseni_ayse, label="Ayşe")
# plt.plot(x_ekseni,y_ekseni_ali, label="Ali")
# plt.plot(x_ekseni,y_ekseni_arzu, label="Arzu")

plt.legend()
plt.tight_layout()

plt.savefig("cizim.png")
plt.grid(True)

plt.xkcd()
plt.style.use('grayscale')

plt.title("Yaş-Boy Tablosu")
plt.xlabel("Yaşlar")
plt.ylabel("Boy Uzunlukları(cm)")
plt.show()


print(plt.style.available)