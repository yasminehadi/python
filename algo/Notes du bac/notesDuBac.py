#import pygal   #question 8
coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]

def calculMoyenne(coefficients,notes):
    somme=0
    for i in range(0,len(notes)):
        somme=somme+notes[i]*coefficients[i]
    return somme/100
#print(calculMoyenne(coefficients,notes))

def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<8:
        print("vous devez allez au rattrapage")
    elif 12>moyenne>=10:
        print("vous avez votre bac")
    elif 14>moyenne>=12:
        print("vous avez votre bac avec mention assez bien")
    elif 16>moyenne>=14:
        print("vous avez votre bac avec mention bien")
    else:
        print("vous avez votre bac avec mention très bien")

def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(1,len(notes)):
        if notes[i]<min:
            min=notes[i]
    return min
print(rechercheNoteMin(notes))

def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(1,len(notes)):
        if notes[i]>max:
            max=notes[i]
    return max
print(rechercheNoteMax(notes))

def rechercheNote(notes,matieres,laNote):
    compteur=0
    for i in range(0,len(notes)):
        if notes[i]==laNote:
            compteur=compteur+1
            print("matieres",matieres[i])
    print("vous avez obtenu",compteur)

def changeNote(notes):
    for i in range(0,len(notes)):
        note=-1
        while(note<0 or note>20):
            print("quel est votre note en",matieres[i])
            note=float(input())
        notes[i]=note

def tableauBac(coefficients,notes,matieres):
    print("(0:40)(1:8)(2:8)(3:8)".format("Enseignement scientifique","Histoire/géographie","Langue vivante A ","Langue vivante B ","EPS","Enseignement spécialité 1ere","Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2")
    pass

#changeNote(notes)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,12)
tableauBac(coefficients,notes,matieres)

"""
#line_chart = pygal.HorizontalBar()
#line_chart.title = 'Notes du Bac (/20)'
#a completer question 8

#line_chart.render_to_file('notes.svg')
"""
