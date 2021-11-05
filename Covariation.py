import numpy as np
import rasterio


with rasterio.open("T33VXF_20210831T101031_B05.jp2", "r") as file:
    B5 = file.read(1)

with rasterio.open("T33VXF_20210831T101031_B06.jp2", "r") as file:
    B6 = file.read(1)

B5_vector = B5.flatten()
B6_vector = B6.flatten()

cov_matrix = np.cov(B5_vector, B6_vector, ddof=1)

print(cov_matrix)