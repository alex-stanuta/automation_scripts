#Converts and reshapes images from a folder using the PIL library

#changeImage.py
#!/usr/bin/env python3
import os
from PIL import Image

#os.chdir("/home/****/supplier-data/images")
for file in os.listdir("/supplier-data/images"):
  try:
    name, ext = os.path.splitext(file)
    im = Image.open(file)
    new_im = im.convert("RGB").resize((600,400))
    path = "/supplier-data/images/" + name + ".jpeg"
    new_im.save(path,"JPEG")
  except OSError:
    pass
