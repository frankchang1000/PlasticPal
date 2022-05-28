from PIL import Image
import os
directory = "data/001/plasticBag"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        prefix = filename.split(".png")[0]
        im = Image.open(filename)
        im.save(prefix+'.jpg')
    elif filename.endswith(".jpeg"):
        prefix = filename.split(".jpeg")[0]
        im = Image.open(filename)
        im.save(prefix+'.jpg')
    else:
        continue

    