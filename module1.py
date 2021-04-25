from PIL import Image
#from IPython.display import display
#from meniar5 import *
import urllib.request


im=Image.open('photohackathon.jpg')
#im.show()


im_new = Image.new("RGB", (500, 500), (60, 0, 80))


#print(im.format, im.size, im.mode)


width, height = im.size




#def iris():
#endroit = input ("Où souhaitez-vous avoir la barre? (0-100)")
endroit=int(5)
#n=input("Combien souhaitez-vous de barres? (1 ou 2)")
#n=int(n)
#if n == 1:
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
#if n == 2:
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(20,30):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(40,50):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(60,70):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(80,90):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(100,110):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(120,130):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(140,150):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(160,170):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(180,190):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(200,210):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(220,230):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(240,250):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(260,270):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(280,290):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(300,310):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(320,330):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(340,350):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(360,370):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))


for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(380,390):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(400,410):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(420,430):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(440,450):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(460,470):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))

for x in range(10):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))
for x in range(480,490):
                for y in range(500):
                    pixel = im.getpixel((x+endroit, y))
                    p_rouge = pixel[0]
                    p_vert =  pixel[1]
                    p_bleu =  pixel[2]
                    im_new.putpixel((x+endroit,y),(p_rouge,p_vert,p_bleu))



im_new.save('sortie.png')
im_new.show()





#menu=input("Bandes(b) ou filtre(f)")
#if menu=="b":
#    iris()
#if menu=="f":
 #  meniar()