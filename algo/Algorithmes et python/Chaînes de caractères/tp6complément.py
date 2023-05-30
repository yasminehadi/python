"""
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebraille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>='' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebraille(texte))

def insertionTexte (texte):
    nouveauTexte=''
    for indice in range (len(texte)-1):
        nouveauTexte+=texte[indice]+'*'
    nouveauTexte+=texte[-1]
    return nouveauTexte
texte=str(input("votre texte?"))
print(insertionTexte(texte))
"""
