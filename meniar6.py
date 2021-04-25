from PIL import Image

import urllib.request
img= Image.open("photohackathon.jpg").convert("RGB")

couleur = input (" choisissez la couleur de la photo: rouge, jaune, violet, vert, cyan, blanc ou bleu ")


# print(img.size)
width,height = img.size
pixels= img.load()
#print(pixels[1,2])


#def meniar():
for py in range(height):
        for px in range(width):
            r,g,b = img.getpixel((px,py))

            if couleur == "rouge":
                newr = r
                newg = 0
                newb = 0
            if couleur =="bleu":
                newr = 0
                newg = 0
                newb = b
            if couleur =="vert":
                newr = 0
                newg = g
                newb = 0
            if couleur == "jaune":
                newr = r
                newg = g
                newb = 0
            if couleur == "violet":
                newr = r
                newg = 0
                newb = b
            if couleur == "cyan":
                newr = 0
                newg = g
                newb = b
            if couleur == "blanc":
                newr = r
                newg = g
                newb = b
            img.putpixel((px,py),(newr,newg,newb))
img.show()


