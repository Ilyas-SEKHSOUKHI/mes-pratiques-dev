'''
------------------------------------------------------
Exercice 3 — Tri décroissant
------------------------------------------------------
Adapte ton code pour que le tri se fasse en ordre décroissant (du plus grand au plus petit).

Exemple :
Entrée : [4, 1, 7, 3]
Sortie attendue : [7, 4, 3, 1]
'''
def Tri_Selection_Decroissant(tab):
    for i in range(len(tab)):
        max = i
        for j in range(i+1,len(tab)):
            if tab[j]>tab[max]:
                max = j
        temp = tab[i]
        tab[i]=tab[max]
        tab[max]=temp
    return tab

Liste = [0]
for i in range(4):
    Entrer = int(input("Entrez un Nombre : "))
    Liste.append(Entrer)

print(Liste)
print(Tri_Selection_Decroissant(Liste))