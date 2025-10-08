'''
4. Gestion de stock
- Demande le nom d’un produit et sa quantité.
- Si la quantité = 0 → affiche “Rupture de stock”,
  sinon → affiche “Produit disponible”.
'''
product_name = input("Entrez le nom de votre produit : ")
quantite = int(input("Entrez la quantite : "))
if quantite == 0:
    print("Rupture de stock")
else:
    print("Produit disponible")