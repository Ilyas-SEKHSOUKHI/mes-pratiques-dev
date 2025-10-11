'''
------------------------------------------------------
Exercice 1 — Tri simple
------------------------------------------------------
Écris une fonction tri_selection(tab) qui trie une liste de nombres entiers en ordre croissant sans utiliser sort().

Exemple :
Entrée : [5, 2, 8, 1, 3]
Sortie attendue : [1, 2, 3, 5, 8]
'''
#Tri de selection
def Tri_Selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    return tab

Liste = [5,2,8,1,3]
print(Tri_Selection(Liste))