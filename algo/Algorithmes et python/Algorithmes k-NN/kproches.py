def distance(x1,x2):
    return abs(x1-x2)

def Kvoisins(L,k,x):
    listeDistanceIndice=[]
    for i in range(len(L)):
        d= distance(x,L[i])
        listeDistanceIndice.append([d,i])
    listeDistanceIndice.sort()
    voisins=[]
    for i in range(k):
       voisins.append(listeDistanceIndice[i][1])
    return voisins

def predireClasse(L,classes,k,x):
    voisins=Kvoisins(L,k,x)
    classespossibles = ['C','T']
    decompte=[0,0]
    for v in voisins:
        if classes[v]=='C':
            decompte[0] +=1
        else:
            decompte[1] +=1
    if decompte[1]>decompte[0]:
        classeChoisie=classespossibles[1]
    else:
        classeChoisie=classespossibles[0]
    if decompte[2]>decompte
    return  classeChoisie

