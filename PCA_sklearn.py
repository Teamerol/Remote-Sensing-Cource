import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


with rasterio.open("T33VXF_20210831T101031_B05.jp2", "r") as file:
    B5 = file.read(1).flatten()

with rasterio.open("T33VXF_20210831T101031_B06.jp2", "r") as file:
    B6 = file.read(1).flatten()

with rasterio.open("T33VXF_20210831T101031_B07.jp2", "r") as file:
    B7 = file.read(1).flatten()

with rasterio.open("T33VXF_20210831T101031_B8A.jp2", "r") as file:
    B8A = file.read(1).flatten()

with rasterio.open("T33VXF_20210831T101031_B11.jp2", "r") as file:
    B11 = file.read(1).flatten()

with rasterio.open("T33VXF_20210831T101031_B12.jp2", "r") as file:
    B12 = file.read(1).flatten()

#PCA analysis
pca = PCA(n_components = 3)

X = np.array([B5, B6, B7, B8A, B11, B12])
pca.fit(X)

def principal_components_images(pca_components, shape: int):

    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    pc1 = ax1.imshow(pca_components[0].reshape((shape,shape)))
    ax1.set_title("Principal component 1")
    pc2 = ax2.imshow(pca_components[1].reshape((shape,shape)))
    ax2.set_title("Principal component 2")
    pc3 = ax3.imshow(pca_components[2].reshape((shape,shape)))
    ax3.set_title("Principal component 3")

    plt.colorbar(pc1, ax = ax1, orientation = 'horizontal', shrink = 0.9)
    plt.colorbar(pc2, ax = ax2, orientation = 'horizontal', shrink = 0.9)
    plt.colorbar(pc3, ax = ax3, orientation = 'horizontal', shrink = 0.9)

    plt.show()

def principal_components_scatterplots(pca_components):
    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    ax1.scatter(pca_components[0], pca_components[1], s = 0.5, c="k", marker="*")
    ax1.set_title("Principal components 1 and 2")
    ax2.scatter(pca_components[1], pca_components[2], s = 0.5, c="k", marker="*")
    ax2.set_title("Principal components 2 and 3")
    ax3.scatter(pca_components[0], pca_components[3], s = 0.5, c="k", marker="*")
    ax3.set_title("Principal components 1 and 3")

    plt.show()

principal_components_images(pca_components=pca.components_, shape=5490)