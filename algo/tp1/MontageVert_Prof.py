a=4
b=3.2
c="hello"
print(a,b,c,"->",end=",") #pas de retour à la ligne
print(a+5) #affichage de variable avec retour à la ligne
print("bonjour") #affichage de texte avec retour à la ligne

a=1
if a>10:
    print("ok")
    print("supérieur")
else:
    print("inférieur")
    print("hello")

a=34
b=6
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a%b
i=b**2
print(c,d,e,f,g,h,i)

a=10
b=12
if a==3 or b==6:
    print("egalité")
else:
    print("pas égale")

a=4
carre=a**2
print("la valeur de a=",a,"au carre est de",carre)