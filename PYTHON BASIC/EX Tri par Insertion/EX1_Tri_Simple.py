'''
------------------------------------------------------
Exercice 1 — Tri simple
------------------------------------------------------
Écris une fonction tri_insertion(tab) qui trie une liste d’entiers en ordre croissant sans utiliser sort().

Exemple :
Entrée : [5, 2, 4, 6, 1, 3]
Sortie attendue : [1, 2, 3, 4, 5, 6]
'''
def Tri_Par_Insertion(tab):
    for i in range(1,len(tab)):
        element = tab[i]
        j = i-1
        while j>=0 and tab[j]>element:
            tab[j+1]=tab[j]
            j -= 1
        tab[j+1]=element
    return tab

Liste = [5,2,4,6,1,3]
print(Liste)
print(Tri_Par_Insertion(Liste))