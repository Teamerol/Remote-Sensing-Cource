from matplotlib import colors
import rasterio
import matplotlib.pyplot as plt
from numpy import zeros
import numpy as np
import seaborn as sns

with rasterio.open("T33VXF_20210831T101031_B10.jp2", "r") as file:
    B10 = file.read(1)

with rasterio.open("T33VXF_20210831T101031_B11.jp2", "r") as file:
    B11 = file.read(1)


N10 = 1830
N11 = 5490
N10_new = N11
print(np.max(B10))

B10_new_grid = zeros((N10_new, N10_new))
print(B10_new_grid.shape)

i, j = np.nested_iters(B10, [[0],[1]], flags = ["c_index"])
for x in i:
    for y in j:
        B10_new_grid[3*(i.index) : 3*(i.index)+3, 3*(j.index) : 3*(j.index)+3] = B10[i.index, j.index]

"""
fig, ((ax1, ax2)) = plt.subplots(1,2)
B10_image = ax1.imshow(B10, cmap='gray', vmin = np.quantile(B10, 0.10), vmax = np.quantile(B10, 0.90))
B10_new_image = ax2.imshow(B10_new_grid, cmap='gray', vmin = np.quantile(B10_new_grid, 0.10), vmax = np.quantile(B10_new_grid, 0.90))
plt.colorbar(B10_image, ax = ax1, orientation = 'horizontal', shrink = 0.9)
plt.colorbar(B10_new_image, ax = ax2, orientation = 'horizontal', shrink = 0.9)

fig2 = plt.figure(2)
plt.hist(B10, bins = 20, density=True)

fig3 = plt.figure(3)
plt.hist(B10_new_grid, bins = 20, density=True)

plt.show()
"""