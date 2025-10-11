'''
------------------------------------------------------
Exercice 7 — Listes aléatoires
------------------------------------------------------
Génère une liste aléatoire avec random.randint() et applique ton tri.

Exemple :
import random
tab = [random.randint(0, 100) for i in range(10)]
'''
import random
def Tri_de_Selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    return tab

tab = [random.randint(0, 100) for i in range(10)]
print(tab)
print(Tri_de_Selection(tab))
