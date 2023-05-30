def remplirCamion(meubles,volumeMax):
    v=0
    n=len(meubles)
    meublesChoisis=[]
    for i in range(0,n):
        if v+meubles[i] [i] <=volumeMax:
            meublesChoisis.append(meubles[i][0])
            v=v+meubles[i] [i]
    print ('volumax embarqué',v)
    return meublesChoisis


#liste des objets
meubles=[['armoire',3],['fauteuil',1.1],['lave vaisselle',1.0],['lit',0.9],['ordinateur',0.2]]
print(meubles)
volumeMax=5
print('Les meubles choisis sont')
meublesChoisis=remplirCamion(meubles,volumeMax)
print(meublesChoisis)
