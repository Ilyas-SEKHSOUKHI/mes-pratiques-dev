'''
------------------------------------------------------
Exercice 4 — Comptage des déplacements
------------------------------------------------------
Ajoute un compteur pour compter combien de déplacements d’éléments ont été faits pendant le tri,
et affiche le résultat à la fin.

Exemple attendu :
Nombre total de déplacements : 8

'''
def Tri_Insertion(tab):
    A = 0
    for i in range(1,len(tab)):
        element = tab[i]
        j = i-1
        while j>=0 and tab[j]>element:
            tab[j+1]=tab[j]
            j-=1
            A+=1
        tab[j+1]=element
    print(A)
    return tab

Liste = [5,2,4,6,1,3]
print(Liste)
print(Tri_Insertion(Liste))