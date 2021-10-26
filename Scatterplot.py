import rasterio
import numpy as np
import matplotlib.pyplot as plt


with rasterio.open("T33VXF_20210831T101031_B05.jp2", "r") as file:
    B5 = file.read(1)

with rasterio.open("T33VXF_20210831T101031_B06.jp2", "r") as file:
    B6 = file.read(1)

plt.scatter(B5, B6, s = 0.5, c="k", marker="*")
plt.xlabel("B5")
plt.ylabel("B6")
plt.title("Scatterplot B5 - B6")
plt.show()