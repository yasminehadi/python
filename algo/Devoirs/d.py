def moyenne(tab):
    if tab==[]:
        print("erreur")
        return none
    else:
        somme=0
        for i in range(len(tab)):
            somme+=tab[i]
        moyenne=somme(len(tab))
        return moyenne

print(moyenne([5,3,8])) #5.3333
print(moyenne([1,2,3,4,5,6,7,8,9,10])) #5.5
print(moyenne([])) #erreur

def multiplication(n1,n2):
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    resultat=0
    for i in range(n2):
        resultat+=n1
    return resultat

def dicotomie(tab,x):
    debut=0
    fin=len(tab)-1
    while debut <= fin:
        m=(debut+fin)//2
        if x==tab[m]:
            debut=m+1
        else:
            fin=m-1
        return false
