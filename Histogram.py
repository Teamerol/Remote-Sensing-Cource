import matplotlib.pyplot as plt
import rasterio
import numpy as np


with rasterio.open("T33VXF_20210831T101031_B05.jp2", "r") as file:
    B5 = file.read(1)

with rasterio.open("T33VXF_20210831T101031_B06.jp2", "r") as file:
    B6 = file.read(1)

print(B5.shape)
print(B6.shape)

hist, xedges, yedges = np.histogram2d(B5.flatten(), B6.flatten(), bins = np.array([10, 10]))
print(hist)
xx, yy = np.meshgrid(np.arange(hist.shape[1]), np.arange(hist.shape[0]))

xx = np.ravel(xx)
yy = np.ravel(yy)
zz = np.zeros_like(xx)

dx = dy = 0.5 * np.ones_like(zz)
dz = np.log(hist.ravel())

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
bars = ax.bar3d(xx, yy, zz, dx, dy, dz, color = 'green')
ax.set_title("B5 - B6")
ax.set_xlabel("B5")
ax.set_ylabel("B6")
ax.set_zlabel("log scale pixels")
plt.show()