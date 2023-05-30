"""
a=(1,2)
print (type(a))
print(a)

a=(1,"bonjour")
b=a*2
print(b)

tuple_1=(5,2,25,56)
tuple_2=("jack","tony")
tuple_3=tuple_1+tuple_2
print(tuple_3)

couleur=(255,128,64)
rouge=couleur[0]
vert=couleur[1]
bleu=couleur[2]
print(rouge,vert,bleu)

tuple=("a",1,5.6,45,"toto")
longueur=len(tuple)
print("longueur du tuple",longueur)
for i in range(0,longueur):
    print(tuple[i])

tuple=("a",1,5.6,45,"toto")
longueur=len(tuple)
print("longueur du tuple",longueur)
for valeur in tuple:
    print(valeur)
"""
"""
a=(1,2) # ou a=1,2
a[0]=0
"""
"""
a=(1,2)
b=(0,a[1])
print(a,b)

couleur=(255,128,64)
rouge=couleur[0]
vert=couleur[1]
bleu=couleur[2]
print(rouge,vert,bleu)

couleur=(255,128,64) #emballage
rouge,vert,bleu=couleur #déballage
print(rouge,vert,bleu)

def donne_moi_ton_nom():
    tuple=("Roger", "Federer")
    return tuple
print(donne_moi_ton_nom())

lst=[45,12,4,78]
print (type(lst))
print(lst)

lst=[45,12,4,78]
lst[1]=0
print(lst)

lst=[45,12,4,78]
longueur=len(lst)
print("longueur de la liste",longueur)
for i in range(0,longueur):
    print(lst[i])

lst=[45,12,4,78]
for valeur in lst:
    print(valeur)

lst=[0] *10
print(lst)
lst[2]=5
print(lst)

lst=[i for i in range(0,10)]
print(lst)

lst=[i*2 for i in range(0,10)]
print(lst)

#ajout d’un élément dans la liste
lst=[i for i in range(0,10)]
print(lst)
lst.append(50)
print(lst)

#affiche les derniers éléments en partant de l’indice 2
lst=[i for i in range(0,10)]
print(lst)
print(lst[2:])

#affiche les 3 premiers éléments
lst=[i for i in range(0,10)]
print(lst)
print(lst[:3])

#affiche le 2ème élément en partant de la fin
lst=[i for i in range(0,10)]
print(lst)
print(lst[-2])

#affiche les éléments entre l’indice 2 et l’indice 6 (exclu)
lst=[i for i in range(0,10)]
print(lst)
print(lst[2:6])

lst=[i for i in range(0,10)]
print(lst)
lst.remove(5)
print(lst)

lst=[i for i in range(0,10)]
print(lst)
lst.insert(7,12)
print(lst)

lst=[[1,2,3],
[4,5,6],
[7,8,9]]
print(lst)

#accès à un élément du tableau
lst=[[1,2,3],
[4,5,6],
[7,8,9]]
ligne=1
colonne=2
print(lst[ligne][colonne])

#affichage sous forme de tableau
lst=[[1,2,3],
[4,5,6],
[7,8,9]]
for ligne in range(0,3):
    for colonne in range(0,3):
        print(lst[ligne][colonne],end="")
    print()

#initialisation d’un tableau à 2 dimensions
ligne = 3
colonne = 4
lst = [[0] * ligne for i in range(colonne)]
lst[1][1]=2
print(lst)

def Tuple(tuple):
    prenom,nom,adresse,codePostal,ville=tuple
    print("prenom :",prenom)
    print("nom :",nom)
    print("adresse :",adresse)
    print("code postal :",codePostal)
    print("ville :",ville)
tuple=("bruce","wayne","3 impasse de la chauve souris",72000,"le mans")
Tuple(tuple)

def calcul(x,coefficients):
    a,b=coefficients
    y=a*x+b
    return y
coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))

from math import sqrt
def distance(ptA,ptB):
    xA,yA=ptA
    xB,yB=ptB
    AB=sqrt((xB-xA)**2+(yB-yA))**2
    return AB
ptA=(1,1)
ptB=(2,2)
print(distance(ptA,ptB))

def min(liste):
    min=liste[0]
    for i in range(len(liste)):
        if liste[0]<min:
            min=liste[20]
    return min
liste=[20,8,9,2,35,49]
print(min(liste))

def max(liste):
    max=liste[5]
    for i in range(len(liste)):
        if liste[0]>max:
            max=liste[49]
    return max
liste=[20,8,9,2,35,49]
print(max(liste))

def somme(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total
lst=[20,8,9,2,35,49]
print(somme(lst))

def moyenne1(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total/len(lst)
lst=[20,8,9,2,35,49]
print(moyenne1(lst))

def somme(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total
lst=[20,8,9,2,35,49]
print(somme(lst))

def moyenne2(lst):
    moyenne2=somme(lst)/len(lst)
    return moyenne2
lst=[20,8,9,2,35,49]
print(moyenne2(lst))
"""
def min(lst):
    min=lst[0]
    for i in range(len(lst)):
        if lst[0]<min:
            min=lst[i]
    return min

def max(lst):
    max=lst[3]
    for i in range(len(lst)):
        if lst[0]>max:
            max=lst[i]
    return max

def moyenne1(lst):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    return total/len(lst)

def rechercheMaxMinMoyenne(lst):
    print(min(lst))
    print(max(lst))
    print(moyenne1(lst))
print(min,max,moyenne1)

lst=[45,12,4,78]
rechercheMaxMinMoyenne(lst)


