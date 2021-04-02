from PIL import Image
#from IPython.display import display
import urllib.request

# ouvrir une image hébergée sur internet
##im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))
im=Image.open('projetnsimars2021.jpg')
im.show()

# créer une nouvelle image vide
# le deuxième argument représente la taille de l'image et le troisième argument (optionnel) la couleur de remplissage au format RVB
im_new = Image.new("RGB", (500, 500), (60, 0, 80))

# informations sur l'image
print(im.format, im.size, im.mode)

# taille de l'image
width, height = im.size

endroit = input ("Où souhaitez-vous avoir la barre?")
endroit=int(endroit)






# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
for x in range(100):
    for y in range(500):
        pixel = im.getpixel((x+endroit, y))

# valeurs des couleurs rouge, vert, bleu
        p_rouge = pixel[0]
        p_vert =  pixel[1]
        p_bleu =  pixel[2]

# modification du pixel de coordonnées x, y
        im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))






# valeurs du pixel de coordonnées x, y (l'origine (0, 0) est en haut à gauche)
for x in range(50):
    for y in range(450):
        pixel = im.getpixel((x+endroit, y))

# valeurs des couleurs rouge, vert, bleu
        p_rouge = pixel[0]
        p_vert =  pixel[1]
        p_bleu =  pixel[2]

# modification du pixel de coordonnées x, y
        im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))






# affichage de l'image
im_new.save('sortie.png')
im_new.show()
