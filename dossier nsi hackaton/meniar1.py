
from PIL import Image

import urllib.request
img= Image.open("images/photohackathon.jpg").convert("RGB")

#print(img.size)
width,height = img.size
pixels= img.load()
#print(pixels[1,2])

for py in range(height):
    for px in range(width):
        r,g,b = img.getpixel((px,py))
        newr = r
        newg = 0
        newb = 0
        pixels[px,py] = (newr,newg,newb)
img.show()

