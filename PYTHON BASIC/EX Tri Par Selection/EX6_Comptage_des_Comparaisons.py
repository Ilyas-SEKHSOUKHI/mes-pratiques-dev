'''
------------------------------------------------------
Exercice 6 — Comptage des comparaisons
------------------------------------------------------
Modifie ton algorithme pour compter le nombre de comparaisons effectuées pendant le tri.
À la fin, affiche le nombre total.
'''
def Tri_de_Selection(tab):
    A = 0 
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            A += 1
            if tab[j]<tab[min]:
                min = j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    print(A)
    return tab

liste = [8,3,6,2,9]
print(liste)
print(Tri_de_Selection(liste))