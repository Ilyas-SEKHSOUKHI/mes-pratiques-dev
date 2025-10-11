'''
------------------------------------------------------
Exercice 2 — Affichage des étapes
------------------------------------------------------
Modifie ton code pour afficher la liste après chaque échange afin de voir comment le tri évolue.

Exemple :
Étape 1 : [1, 5, 8, 2, 3]
Étape 2 : [1, 2, 8, 5, 3]
...
'''
def Tri_Selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min =j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
        print(tab)
    return tab

Liste = [1,5,8,2,3]
print(Tri_Selection(Liste))