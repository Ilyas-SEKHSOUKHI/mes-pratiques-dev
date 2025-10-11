'''
------------------------------------------------------
Exercice 2 — Affichage étape par étape
------------------------------------------------------
Modifie ta fonction pour afficher la liste après chaque insertion afin d’observer les étapes du tri.

Exemple :
Étape 1 : [2, 5, 4, 6, 1, 3]
Étape 2 : [2, 4, 5, 6, 1, 3]
...
'''
def Tri_Par_Insertion(tab):
    for i in range(1,len(tab)):
        element = tab[i]
        
        j = i-1
        while j>=0 and tab[j]>element:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=element
    return tab

liste = [2,5,4,6,1,3]
print(liste)
print(Tri_Par_Insertion(liste))
