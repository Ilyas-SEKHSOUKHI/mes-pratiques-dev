'''
10. Liste dynamique
- Crée une liste vide.
- Demande à l’utilisateur d’ajouter 5 noms (avec append()).
- Affiche la liste finale.
'''
Liste =[]
for i in range(5):
    Names = input("Entrez le nom n"+str(i))
    Liste.append(Names)
print(Liste)