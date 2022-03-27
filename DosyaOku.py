from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\1\Desktop\arabalar.csv")
data.head()

df = pd.DataFrame(data)
name = df["name"].head(12)
price = df["price"].head(12)

fig, ax = plt.subplots(figsize=(16, 9))

ax.barh(name,price)



plt.show()



