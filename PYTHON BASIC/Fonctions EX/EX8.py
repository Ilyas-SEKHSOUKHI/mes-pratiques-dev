'''
8. Fonction avec liste
Crée une fonction afficher_liste(liste) qui affiche chaque élément de la liste sur une ligne différente.
'''
def afficher_liste(liste):
    for i in range(len(liste)):
        print(liste[i])

notes = []
for i in range(5):
    A = int(input("Entrez une note : "))
    notes.append(A)
print(notes) 
print(afficher_liste(notes))