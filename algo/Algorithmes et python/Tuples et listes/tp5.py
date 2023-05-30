"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new("RGB",(256,256),(0,0,0))

largeur,hauteur=img.size
draw=ImageDraw.Draw(img)
draw.line((0,0,largeur,hauteur),fill=(0,255,0))

draw.line((10,20,100,200),fill=(255,0,0))
img.show()

from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for x in range(0,nbDroites):
        draw.line((x*ecart,0,x*ecart,hauteur),fill=(0,255,0))

traceDroite(10,20)


img.show()
"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():



tracecible()
img.show()











