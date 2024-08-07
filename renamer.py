import os

for image in os.listdir("."):
    if image.startswith("ezgif-"):
        os.rename(image,image[6:])