from PIL import Image
import glob, os

size = 128, 128
src_file = '/home/metal-machine/Desktop/ad.png'
im = Image.open(src_file)
im.thumbnail(size)
m = im.save(src_file + ".thumbnail", "JPEG")

print m


im = Image.open(src_file)
    im.thumbnail(size)
    im.save(src_file + ".thumbnail", "JPEG")
    
