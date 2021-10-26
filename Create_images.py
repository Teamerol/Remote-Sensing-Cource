import os
import rasterio
import matplotlib.pyplot as plt
from numpy import quantile

images = []
names_of_images =[]

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

with os.scandir("./") as entries:
    for entry in entries:
        print(entry.name)
        if entry.name.endswith(".img"):
            images.append(entry.name)
            names_of_images.append(entry.name[:-4])

try:
    os.mkdir("pictures")
    print("Folder is created")
except:
    print("Folder already exists")

for image, name in zip(images, names_of_images):
    with rasterio.open(image, "r") as file:
        band = file.read(1)
    
    print(image, name)
    plt.imshow(band, cmap='viridis', vmin = quantile(band, 0.10), vmax = quantile(band, 0.90))
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Sentinel-2 " + name)
    plt.colorbar()
    plt.savefig("./pictures/" + name + ".png")
    plt.close()