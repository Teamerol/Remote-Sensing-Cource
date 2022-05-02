import rasterio
import matplotlib.pyplot as plt
import numpy as np


with rasterio.open("T33VXF_20210831T101031_B08.jp2", "r") as file:
    B8 = file.read(1)

#Regions for labeling
sea = B8[9000:9100, 6400:6500]
urban = B8[1750:1850, 7350:7450]
forest = B8[3450:3550, 1350:1450]

#Apriori probabilities
sea_apriori = 0.45
urban_apriori = 0.2
forest_apriori = 0.35

#Historgams
sea_hist, sea_bins = np.histogram(sea.ravel(), density=True)
urban_hist, urban_bins = np.histogram(urban.ravel(), density=True)
forest_hist, forest_bins = np.histogram(forest.ravel(), density=True)

#Aposteriori probablities
sea_aposteriori =  sea_hist * sea_apriori
urban_aposteriori = urban_hist * urban_apriori
forest_aposteriori = forest_hist * forest_apriori

#Borders of classes
#Constants are taken manually  from results of lines plot.
max_sea = max(sea_bins)
min_forest = 1214
max_forest = 2427

#Class map array
class_map = np.zeros(len(B8.ravel()))

#Image references
def plot_images():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    sea_reference = ax1.imshow(sea)
    ax1.set_title("Sea")
    fig.colorbar(sea_reference, ax = ax1, shrink = 0.5)
    urban_reference = ax2.imshow(urban)
    ax2.set_title("Urban area")
    fig.colorbar(urban_reference, ax = ax2, shrink = 0.5)
    forest_reference = ax3.imshow(forest)
    ax3.set_title("Forest")
    fig.colorbar(forest_reference, ax = ax3, shrink = 0.5)
    plt.show()

#See histogram
def plot_hist():
    plt.hist(sea.ravel(), bins=10, density=True, color="blue", histtype='step')
    plt.hist(urban.ravel(), bins=10, density=True, color="pink", histtype='step')
    plt.hist(forest.ravel(), bins=10, density=True, color="green", histtype='step')
    plt.title("Three classes")
    plt.show()

def plot_lines():
    plt.plot(sea_bins[:-1], sea_aposteriori, color = "blue")
    plt.plot(urban_bins[:-1], urban_aposteriori, color = "pink")
    plt.plot(forest_bins[:-1], forest_aposteriori, color = "green")
    plt.title("Aposteriority probabilities")
    plt.show()

def classification():
    i = 0
    for val in B8.ravel():
        if val < max_sea:
            class_map[i] = 1
        elif val > min_forest and val < max_forest:
            class_map[i] = 2
        else:
            class_map[i] = 3
        
        i = i + 1
    
    class_map_reshaped = class_map.reshape(10980, 10980)
    plt.imshow(class_map_reshaped)
    plt.savefig("figure.png")
    plt.imsave("class_map.png", class_map_reshaped)
    plt.show()

classification()