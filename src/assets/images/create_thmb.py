#!/usr/local/bin/python3

import glob
from PIL import Image

files = glob.glob('gallery/*')

for file in files:
   im=Image.open(file)
   im.thumbnail((240,240))
   im.save(file.replace("gallery", "gallery_thmb"))
