
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
        print('la phrase codée est',codage(phrase,cle))
    if menu=='2':
        phrase=input("votre phrase codée?")
        print('la phrase décodée est',codage(phrase-cle))
    if menu=='3':
        cle=int(input("votre nouvelle cle"))

"""
def LettresChiffres(Chiffres,cle):
    Chiffres=Chiffres.upper()
    MorseChiffres=""
    for c in Chiffres:
        if c>="A" and c<="Z":
            ascii=ord(c)
            lettre=ascii-65
            lettre=(lettre+cle)%26
            ascii=lettre+65
            caractere=chr(ascii)
            MorseChiffres=MorseChiffres+caractere
        else:
            MorseChiffres=MorseChiffres+c
    return MorseLettres
cle=3
"""
"""
def ChiffresMorse(chiffres):
    chiffres=chiffres.upper()
    MorseChifrres=""
    for c in range(0,len(chiffres)):
        if chiffres[c]>="" and chiffres[c]<="10":
            MorseChifrres+=codeMorseChiffres[ord(chiffres[c])-32]
    return MorseChifrres

print(ChiffresMorse(chiffres))
"""
"""
def double(mot):
    for n in range(0,len(mot)):

print(double("bon"))
"""






