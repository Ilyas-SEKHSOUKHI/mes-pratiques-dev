'''
------------------------------------------------------
Exercice 5 — Comparer avec sorted()
------------------------------------------------------
Teste ton algorithme et compare le résultat avec la fonction Python intégrée :

print(tri_selection(tab))
print(sorted(tab))

Les deux doivent donner le même résultat.
'''
def Tri_Par_Selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    return tab



liste = [5,8,9,4,6,7]
print(Tri_Par_Selection(liste))
print(sorted(liste))