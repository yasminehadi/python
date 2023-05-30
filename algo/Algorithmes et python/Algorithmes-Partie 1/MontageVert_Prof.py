a=4
carre=a**2
print("la valeur de a=",a,"au carre est de",carre)

kilometre=100
miles=kilometre/1.609
print("la distance de",kilometre,"kilometre est de",miles,"miles")

a=2
b=3
print("avant échange a=",a,"et b=",b)
temp=a
a=b
b=temp
print ("après échange a=",a,"et b=",b)

valeur_tva=20
prix_ht=40
tva=prix_ht*valeur_tva/100
prix_ttc=prix_ht+tva
print("prix ht du produit:",prix_ht,"€")
print("indice de la tva en 2015:",valeur_tva,"%")
print("valeur de la tva:",tva,"€")
print("prix ttc:",prix_ttc,"€")

a=3
b=-15
r=a*0
if r<0:
    print("néfatif")
else:
    print("positif")

nb_valeur=10
result=0
for n in range(1,nbvaleur+1):
    print("somme des",nb_valeur,"premier nombres entiers est:",result)

