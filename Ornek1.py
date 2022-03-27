from matplotlib import pyplot as plt
import numpy as np

barWidth = 0.25

fig = plt.subplots(figsize =(12, 8))

IT = [12, 30, 1, 8, 22]
MH = [28, 6, 16, 5, 10]
YN = [29, 3, 24, 25, 17]

br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

#Plot değlerini girme
plt.bar(br1, IT, color='r', width=barWidth, edgecolor= "grey", label='Bilgi İşlem')
plt.bar(br2, MH, color='g', width=barWidth, edgecolor="grey", label='Muhasebe')
plt.bar(br3, YN, color='b', width=barWidth, edgecolor='grey', label='Yönetim')

#xtickleri girme
plt.xlabel("Birimler", fontweight="bold", fontsize=15)
plt.ylabel("Geçen Birimler", fontweight="bold", fontsize=15)

plt.xticks([r+ barWidth for r in range(len(IT))],
           ['2015','2016','2017', '2018', '2019'])

plt.legend()
plt.show()