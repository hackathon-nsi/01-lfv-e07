from PIL import Image
#from IPython.display import display
from meniar3 import *
import urllib.request

# ouvrir une image hébergée sur internet
##im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))
im=Image.open('photohackathon.jpg')
im.show()

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (500, 500), (60, 0, 80))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size




def iris():
    endroit = input ("Où souhaitez-vous avoir la barre? (0-100)")
    endroit=int(endroit)
    n=input("Combien souhaitez-vous de barres? (1 ou 2)")
    n=int(n)
    if n == 1:
            for x in range(120):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    if n == 2:
            for x in range(120):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
            for x in range(200,300):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
    im_new.save('sortie.png')
    im_new.show()



menu=input("Bandes(b) ou filtre(f)")
if menu=="b":
    iris()
if menu=="f":
    meniar()

