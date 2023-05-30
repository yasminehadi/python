"""
codeMorseLettres=['.-','-...','-.-.','-..','.','..-.','--.','....','..',
           '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
           '...','-','..-','...-','.--','-..-','-.--','--..']
codeMorseChiffres =['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']

texte=str(input("votre texte ?"))
def LettresMorse(Lettre,cle):
    Lettre=Lettre.upper()
    MorseLettres=""
    for c in Lettre:
        if c>="A" and c<="Z":
            ascii=ord(c)
            lettre=ascii-65
            lettre=(lettre+cle)%26
            ascii=lettre+65
            caractere=chr(ascii)
            MorseLettres=MorseLettres+caractere
        else:
            MorseLettres=MorseLettres+c
    return MorseLettres
cle=3
menu=''
while menu!='q':
    print("-----")
    print("1: Codage d'une phrase")
    print("2: Décodage d'une phrase")
    print("3: changement de la cle")
    print("q: quitter")
    print("-----")
    menu=input("votre choix?")
    if menu=='1':
        phrase=input("votre code en clair?")
        print('la phrase codée est',LettresMorse(lettre,cle))
    if menu=='2':
        phrase=input("votre phrase codée?")
        print('la phrase décodée est',LettresMorse(lettre,-cle))
    if menu=='3':
        cle=int(input("votre nouvelle cle"))
"""


def double(mot):
    for n in range(0,len(mot)):
        mot=mot*2
print(double("bon"))






