'''
------------------------------------------------------
Exercice 3 — Tri décroissant
------------------------------------------------------
Adapte ton code pour que la liste soit triée du plus grand au plus petit.

Exemple :
Entrée : [5, 2, 4, 6, 1, 3]
Sortie attendue : [6, 5, 4, 3, 2, 1]
'''
def Tri_Insertion_decroissant(tab):
    for i in range(1,len(tab)):
        element = tab[i]
        j = i-1
        while j>=0 and tab[j]<element:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=element
    return tab
Liste = [5,2,4,6,1,3]
print(Liste)
print(Tri_Insertion_decroissant(Liste))