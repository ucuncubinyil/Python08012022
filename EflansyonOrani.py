from matplotlib import pyplot as plt


yilllar = [2010,2011,2012,2013,2014,2015,2016]
ikibin_on = [10000,15010,30000,65454,65645,65688,22547]
ikibin_onbir = [10100,15010,30200,35454,65645,65688,22547]
ikibin_oniki = [13000,15010,30000,25454,65645,65688,22547]
ikibin_onuc = [10000,15010,30100,35454,65645,65688,22547]
ikibin_ondort = [20300,15010,33000,65454,65645,6518,22547]
ikibin_onbes = [10000,15010,30004,65454,65645,65688,22547]
ikibin_onalti = [10000,15010,30000,65454,65645,62688,22547]


plt.plot(yilllar, ikibin_on, label="2010")
plt.plot(yilllar, ikibin_onbir, label="2011")
plt.plot(yilllar, ikibin_oniki, label="2012")
plt.plot(yilllar, ikibin_onuc, label="2013")
plt.plot(yilllar, ikibin_ondort, label="2014")
plt.plot(yilllar, ikibin_onbes, label="2015")
plt.plot(yilllar, ikibin_onalti, label="2016")




plt.show()