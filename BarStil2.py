from matplotlib import pyplot as plt
import numpy as np

N = 5

menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

ind = np.arange(N)

width = 0.35

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.bar(ind, menMeans, width, color='r')
ax.bar(ind, womenMeans, width, color='b')

ax.set_ylabel("Skorlar")
ax.set_xlabel("Tahminler")
ax.set_title("Ekerler ve Kadınlar Skor Tablosu")

ax.set_xticks(ind,('G1','G2','G3','G4','G5'))

ax.set_yticks(np.arange(0,81,10))
ax.legend(labels=["Erkekler", "Kadınlar"])

plt.show()

