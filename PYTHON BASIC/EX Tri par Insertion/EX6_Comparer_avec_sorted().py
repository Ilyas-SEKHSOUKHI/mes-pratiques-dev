'''
------------------------------------------------------
Exercice 6 — Comparer avec sorted()
------------------------------------------------------
Teste ton tri et compare le résultat avec la fonction Python intégrée sorted().

print(tri_insertion(tab))
print(sorted(tab))
'''
def Tri_Insertion(tab):
    for i in range(1,len(tab)):
        element = tab[i]
        j = i-1
        while j>=0 and tab[j]>element:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=element
    return tab

Liste = [5,2,4,6,1,3]
print(Liste)
print(Tri_Insertion(Liste))
print(sorted(Liste))