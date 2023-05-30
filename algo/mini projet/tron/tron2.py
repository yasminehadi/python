"""
Programme du tron
hadi,yasmine,1G6
"""
import pygame
from random import *

#constantes de la fenaître d'affichage
LARGEUR=400       #hauteur de la fenaître
HAUTEUR=400      #largeur de la fenaître
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenaître
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractaires
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//4
motoY=LARGEUR//4
moto2X=LARGEUR//2
moto2y=LARGEUR//2
direction = 'haut'
tempsPartie=0

def dessineDecor():
    """
    dessine un decor,
    """
    rondALEA=randint(3,10)
    rectALEA=randint(3,10)
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],2)
    for i in range(0,rondALEA):
        pygame.draw.circle(fenetre, ROUGE, (randint(10,470), randint(10,470)), randint(10,25))
    for i in range(0,rectALEA):      #cercle plein aux coord x,y de rayon 10
        pygame.draw.rect(fenetre, BLEU, [randint(5,400), randint(5,400), randint(10,25), randint(10,25)],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifié
     si on touche un mur ou autre chose
    aucun obstacle correspond à une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
    elif direction=='droite':
        x=motoX+1
        y=motoY
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée

def deplacementmoto2():
    """
    deplace la moto
    """
    global motoX2,motoY2
    touche=False
    if direction=='haut':
        x=moto2X
        y=moto2Y-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=moto2X
        y=moto2Y+1
    elif direction=='droite':
        x=moto2X+1
        y=moto2Y
    elif direction=='gauche':
        x=moto2X-1
        y=moto2Y
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        moto2X=x2
        moto2Y=y2
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée



loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenaître (croix rouge)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_e]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_d]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_f]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_s]:  #est-ce la touche LEFT
        direction = 'gauche'

    #fenetre.fill((0,0,0))   #efface la fenaître, non utilisé ici

    if deplacementmoto()==True:
        loop=False
    frequence.tick(60)
    pygame.display.update() #mets à  jour la fenaître graphique
    tempsPartie+=1
pygame.quit()
print('perdu')
print('temps partie',tempsPartie)