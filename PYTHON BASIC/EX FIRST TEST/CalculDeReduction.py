## Exercice 6 : Calcul de réduction
'''
Créez un programme pour un magasin :
- Demande le prix original d'un produit
- Si le prix est > 100€, applique une réduction de 15%
- Si le prix est entre 50€ et 100€, applique 10%
- Si < 50€, pas de réduction
- Affiche le prix final
'''
print("-----------Calcul de reduction------------")
Prix_Original = float(input("Entrez le prix original : "))
Reduction = 0
if Prix_Original > 100:
    print("Reduction de 15%")
    Reduction = Prix_Original - (15*Prix_Original)/100
    print("Prix avec Reduction = "+str(Reduction))
elif Prix_Original >= 50 and Prix_Original<=100:
    print("Reduction de 10%")
    Reduction = Prix_Original - (10*Prix_Original)/100
    print("Prix avec Reduction = "+str(Reduction))
else:
    print("Pas de Reduction")