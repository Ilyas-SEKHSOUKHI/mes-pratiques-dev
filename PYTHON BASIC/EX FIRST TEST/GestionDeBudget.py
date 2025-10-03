## Exercice 2 : Gestion de budget
'''
Créez un programme de gestion de budget :
- L'utilisateur entre son budget initial
- Puis entre le prix de 3 produits qu'il souhaite acheter
- Le programme calcule le total des achats
- Affiche si le budget est suffisant ou non
- Si suffisant, affiche le budget restant
'''

print("------------Gestion de budget------------")
Budget = float(input("Entrez votre Budget"))
Premier_Produit = float(input("Enrtez le prix du premier produit"))
Deuxieme_Produit = float(input("Entrez la valeur du deuxieme produit"))
Troisieme_Produit = float(input("Entrez la valeur du Troisieme Produit"))
Total = Premier_Produit+Deuxieme_Produit+Troisieme_Produit
if Budget == Total or Budget > Total:
    print("Budget Suffisant")
    Budget = Budget-Total
    print("Budget Restant : "+str(Budget))
else:
    print("Budget Non Suffisant")