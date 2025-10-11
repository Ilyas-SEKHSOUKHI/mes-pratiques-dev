'''
------------------------------------------------------
Exercice 4 — Trouver le minimum
------------------------------------------------------
Écris une petite fonction indice_minimum(tab, debut) qui retourne l’indice du plus petit élément à partir de la position debut.

Exemple :
tab = [8, 3, 6, 2, 9]
indice_minimum(tab, 1)  # Résultat attendu : 3 (car tab[3] = 2)
'''
def indice_minimum(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    print(tab)
    
    for i in range(len(tab)):
        if liste_1[i]==tab[0]:
            Resultat = i
    print(Resultat)




liste = [8,3,6,2,9]
liste_1 = [8,3,6,2,9]
print(liste)
print(indice_minimum(liste))