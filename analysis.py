import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_log.csv")

df["deltaT"] = df["battery_temp"] - df["ambient_temp"]

print(df.groupby("cooling")["deltaT"].mean())

df.boxplot(column="deltaT", by="cooling")
plt.title("Cooling effect on Pixel 6a battery temperature")
plt.show()
