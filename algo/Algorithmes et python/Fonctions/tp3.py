"""
a=3
b=5
c=a*b
print("Résultat: ",c)

def multiplie (a,b):
 return a * b
c=multiplie(2,5)
print("Résultat: ",c)
d=multiplie(4,5)
print("Résultat: ",d)

def affiche(valeur):
    print(valeur,end='')

def compte(max):
    for n in range(0,max+1):
        print(n)

compte(5)
print()
compte(8)

def calcul(x):
    return 2*x+3

for x in range(0,11):
    print("x=", x , "y=",calcul(x))

def test():
    b=5
    print(a,b)

a=2
b=7
test()
print(a,b)

def texte():
    print("bonjour")
texte()

def texte(prenom):
    print("bonjour",prenom)
texte("yasmine")

def somme(a,b):
    s=a+b
    return s
print(somme(3,5))

def calculsurface(longueur,largeur):
    surface=longueur*largeur
    return surface
print(calculsurface(10.5,2))

def calculformule (x):
    y=2*x**2-4+3
    return y
print(calculformule(3.2))

def triangle(hauteur):
    for h in range(1,hauteur+2):
        for i in range(1,h):
            print("*",end="")
        print()

triangle(6)
"""
from math import pi
def volume(rayon):
    v=4*pi*rayon**3/3
    return v
print(volume(10))