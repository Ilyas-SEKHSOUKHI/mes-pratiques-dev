#EX7
'''
7. FILTRAGE DE LISTE
   • Crée une liste de prix : [120, 80, 45, 300, 150]
   • Crée une nouvelle liste avec seulement les prix ≥ 100
   • Affiche la liste filtrée
'''
Prix = [120,80,45,300,150]
Prixx = []
for i in range(len(Prix)):
    if Prix[i]>=100:
        Prixx.append(Prix[i])
print(Prixx)

#EX8
'''
8. FUSION DE LISTES
   • Crée : A = [1, 2, 3] et B = [4, 5, 6]
   • Fusionne A et B avec l'opérateur + (crée une nouvelle liste)
   • Fusionne A et B avec extend() (modifie A)
   • Affiche les résultats
'''
A = [1,2,3]
B = [4,5,6]
C = []
C = A + B
print(C)
A.extend(B)
print(A)

#EX9
'''
9. SUPPRIMER LES DOUBLONS
   • Crée : nombres = [1, 2, 2, 3, 4, 4, 5]
   • Supprime tous les doublons
   • Affiche la liste sans répétitions
'''
nombres = [1,2,2,3,4,4,5]
# Convertir la liste en set
nombres_set = set(nombres) # set sup tout les double 
print(nombres)
print(nombres_set)  # Exemple de sortie : {1, 2, 3, 4, 5}
# A Reviser

#EX10
'''
10. LISTE MIXTE
    • Crée une liste avec différents types :
      [42, "hello", 3.14, True, "python"]
    • Parcours la liste avec une boucle for
    • Pour chaque élément, affiche sa valeur et son type
'''
objects = [42,"hello",3.14,True,"python"]
for object in objects:
   print(f"{object}  {type(object)}")

# for i in range(len(Liste)):
#     print(Liste[i])
#     print(type(Liste[i]))
