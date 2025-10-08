'''
7. Boucle while
- Demande à l’utilisateur un mot de passe jusqu’à ce qu’il entre "admin123".
- Une fois correct, affiche "Accès autorisé".
'''
mot_de_passe = input("Entrez votre mot de passe : ")
while mot_de_passe != "admin123":
    mot_de_passe = input("Entrez votre mot de passe : ")
print("True")    
