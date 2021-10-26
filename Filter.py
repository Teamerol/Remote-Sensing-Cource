import matplotlib.pyplot as plt
import rasterio
import numpy as np
from scipy.signal import convolve2d


with rasterio.open("T33VXF_20210831T101031_B05.jp2", "r") as file:
    B5 = file.read(1)

with rasterio.open("T33VXF_20210831T101031_B06.jp2", "r") as file:
    B6 = file.read(1)

#Kernel for high pass filter
W_HP_3 =np.matrix("-1 -1 -1; -1 8 -1; -1 -1 -1")
W_HP_3 = W_HP_3 / 9
print(W_HP_3)

#Kernel for low pass filter
W_LP_3 =np.matrix("1 1 1; 1 1 1; 1 1 1")
W_LP_3 = W_LP_3 / 9
print(W_LP_3)

#Convolution (русск. "свёртка")
result_LP = convolve2d(B5, W_LP_3, mode = 'valid')
result_HP = convolve2d(B5, W_HP_3, mode = 'valid')

#Creating images
fig, ((ax1, ax2, ax3)) = plt.subplots(1,3)
B5_img = ax1.imshow(B5, cmap = 'Greys_r', vmin = np.quantile(result_LP, 0.10), vmax = np.quantile(result_LP, 0.90),)
LP_filter = ax2.imshow(result_LP, cmap = 'Greys_r', vmin = np.quantile(result_LP, 0.10), vmax = np.quantile(result_LP, 0.90))
HP_filter = ax3.imshow(result_HP, cmap = 'Greys_r', vmin = np.quantile(result_HP, 0.10), vmax = np.quantile(result_HP, 0.90))
plt.colorbar(B5_img, ax = ax1, orientation = 'horizontal', shrink = 0.9)
plt.colorbar(LP_filter, ax = ax2, orientation = 'horizontal', shrink = 0.9)
plt.colorbar(HP_filter, ax = ax3, orientation = 'horizontal', shrink = 0.9)
ax1.set_title("B5")
ax2.set_title("Low pass")
ax3.set_title("High pass")
plt.show()