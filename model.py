import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# 簡易モデル
df["deltaT"] = df["battery_temp"] - df["ambient_temp"]

print(df.groupby("cooling")["deltaT"].mean())

# 可視化
df.boxplot(column="deltaT", by="cooling")
plt.show()
