from osgeo import gdal
import os

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

new_dicrectory = "transformed"
if not os.path.isdir(new_dicrectory):
    os.mkdir(new_dicrectory)

for file in os.listdir(path):
    if file.endswith(".jp2"):
        print(file)
        try:
            image = gdal.Open(path + "/" + file)
        except:
            print("Error while opening")

        driver = gdal.GetDriverByName("HFA")
        driver.CreateCopy(new_dicrectory + "/" + file[:-4] + ".img", image, strict=0)