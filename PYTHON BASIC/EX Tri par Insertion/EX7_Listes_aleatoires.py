'''
------------------------------------------------------
Exercice 7 — Listes aléatoires
------------------------------------------------------
Génère une liste aléatoire avec random.randint() et applique ton tri.

Exemple :
import random
tab = [random.randint(0, 100) for i in range(10)]
print(tri_insertion(tab))
'''
import random

def Tri_Insertion(tab):
    for i in range(1,len(tab)):
        element = tab[i]
        j = i-1
        while j >=0 and tab[j]>element:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=element
    return tab


tab = [random.randint(0,100)for i in range(10)]
print(tab)
print(Tri_Insertion(tab))