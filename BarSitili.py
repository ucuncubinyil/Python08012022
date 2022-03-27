from matplotlib import pyplot as plt


#Bar tipinde grafik çizme

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

lang = ["C", "C++", "Java", "Python", "Php"]

students = [23,17,35,90,12]

ax.bar(lang,students)

plt.show()
