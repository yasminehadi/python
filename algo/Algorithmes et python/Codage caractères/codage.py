"""
car='a'
print(car)

car = 'b'
print(ord(car))
print(ord(car)+2)

valeur=66
print(chr(valeur))

car = 'a'
valeur=ord(car)+2
print(valeur)
print(chr(valeur))

valeur=346
print(chr(valeur))
valeur=0x1f3
print(chr(valeur))

import os
fichier=open("texte.txt","w")
fichier.write("bonjour\n")
fichier.write("salut")
fichier.close()

import os
fichier=open("texte.txt","a")
fichier.write("hasta luego")
fichier.close()

import os
fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()
"""

new_message =""     # initialise new_message avec un message vide
message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")
print("Vous avez saisi ",message)  # Affiche le message saisi

for n in message:               # pour chaque caractère n dumessage saisi (de la chaine message)
    code_initial = ord(n)       # la variable code_initial prend le code (Unicode)
                              # du caractère courant (n)
    code_minuscule = code_initial+32   # calcul le codecorrespondant au caractère minuscule

    car_minuscule = chr(code_minuscule) # car_minuscule prend le caractère/symbole correspondant
                                        #à la variable code_minuscule
    print(car_minuscule)      # Affiche le caractère obtenu
    new_message = new_message + car_minuscule  # ajoute le caractère obtenu à new_message

else

print (new_message)    # Affiche le nouveau message








