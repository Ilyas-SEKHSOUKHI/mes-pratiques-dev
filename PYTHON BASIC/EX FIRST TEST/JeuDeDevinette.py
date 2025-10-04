## Exercice 5 : Jeu de devinette
'''
Créez un jeu où :
- Le programme génère un nombre aléatoire entre 1 et 10
- L'utilisateur doit deviner le nombre
- Le programme donne des indices ("Plus" ou "Moins")
- Affiche un message de félicitations quand c'est trouvé

ASTUCE : Utilisez import random et random.randint(1, 10)
'''
import random
print("--------Jeu De Devinette -----------")
Numbre = int(input("Entrez un nombre"))  
Aleatoire_Nombre = random.randint(1,10) # Donne un nombre aléatoire de type int
print(Aleatoire_Nombre)
Resultat = False
while Numbre != Aleatoire_Nombre:
    if(Numbre>Aleatoire_Nombre):
        print("Mois")
        Numbre = int(input("Entrez un nombre"))
    else:
        print("Plus")
        Numbre = int(input("Entrez un nombre"))

print("Bon Resultat")

