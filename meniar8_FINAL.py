from PIL import Image
#from IPython.display import display
#from meniar5 import *
import urllib.request
im=Image.open('photohackathon.jpg').convert("RGB")

im.show()

f_ou_b = input (" voulez vous un filtre (f) ou des bandes (b) ou les deux (fb)? ")


if f_ou_b == "f":
    couleur = input (" choisissez la couleur de la photo: rouge, jaune, violet, vert, cyan, blanc ou bleu ")
    width,height = im.size
    pixels= im.load()
    for py in range(height):
        for px in range(width):
            r,g,b = im.getpixel((px,py))

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
            im.putpixel((px,py),(newr,newg,newb))
    im.show()


if f_ou_b == "b":
    im_new = Image.new("RGB", (437, 805), (60, 0, 80))
    width, height = im.size
    endroit=int(5)
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(20,30):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(40,50):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(60,70):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(80,90):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(100,110):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(120,130):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(140,150):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))


    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(160,170):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(180,190):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(200,210):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(220,230):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(240,250):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(260,270):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(280,290):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(300,310):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(320,330):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(340,350):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(360,370):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))


    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(380,390):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(400,410):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(420,430):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    im_new.show()




if f_ou_b == "fb":
    couleur = input (" choisissez la couleur de la photo: rouge, jaune, violet, vert, cyan, blanc ou bleu ")
    width,height = im.size
    pixels= im.load()
    for py in range(height):
        for px in range(width):
            r,g,b = im.getpixel((px,py))

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
            im.putpixel((px,py),(newr,newg,newb))

    im_new = Image.new("RGB", (437, 805), (60, 0, 80))
    width, height = im.size
    endroit=int(5)
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(20,30):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(40,50):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(60,70):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(80,90):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(100,110):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(120,130):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(140,150):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))


    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(160,170):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(180,190):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(200,210):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(220,230):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(240,250):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(260,270):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(280,290):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(300,310):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(320,330):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(340,350):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(360,370):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))


    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(380,390):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(400,410):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

    for x in range(10):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    for x in range(420,430):
                for y in range(805):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]





    #im.show()











    #im_new.save('sortie.png')
    im_new.show()

