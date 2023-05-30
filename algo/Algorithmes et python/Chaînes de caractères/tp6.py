# Créé par yasmine.HADI, le 01/12/2022 en Python 3.7
"""
phrase = "bonjour"
print (phrase[1:4])

chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)

w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))

chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')

chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')

s = "Welcome"
print(s[-1])
print(s[-2])

s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])

s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))

chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)

ch = 'A'
print(ord(ch))

valeur=66
print(chr(valeur))

chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)

def compteLettre(lettre,chaine):
    chaine.count("e")
    return chaine.count("e")
print(compteLettre('e','je vais au cine ce soir'))

def compteLettre(lettre,chaine):
    somme=0
    for i in range(len(chaine)):
        if chaine[i]==lettre:
            somme=somme+1
    return somme
print(compteLettre('e','je vais au cine ce soir'))

def premierMot(chaine):
    chaine[1]
    for i in range(len(chaine)):

    return chaine
print(fonctionpremierMot("enfin il arrête de pleuvoir "))

print("un peu,beaucoup,passionément")

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
longueur=len(semaine)
for i in range(0,longueur):
    print(semaine[i])
"""
def comptelettre(lettre,chaine):
    compteur=0
    for n in range(0,len(chaine)):
        if chaine[n]==lettre:
            compteur+=1
    return compteur
print(comptelettre('e','je vais au cine ce soir'))

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jourdepart=6
for n in range(1,32):
    print("{0:10}{1:2} décembre".format(semaine[jourdepart],n))
    jourdepart=(jourdepart+1)%7

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jourdepart=6
for n in range(1,32):
    print("{0:10}{1:2}décembre".format(semaine[jourdepart],n))
    jourdepart=(jourdepart+1)%7

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
jourdepart=6
for n in range(1,32):
    print("{0:10}{1;2}décembre".format(semaine[jourdepart,n]))
    jourdepart=(jourdepart+1)%7






























