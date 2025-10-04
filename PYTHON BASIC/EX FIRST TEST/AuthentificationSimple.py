## Exercice 7 : Authentification simple
'''
Créez un système d'authentification :
- Définissez un nom d'utilisateur et mot de passe fixes
- Demandez à l'utilisateur de s'identifier
- Vérifiez si les informations correspondent
- Affichez un message de bienvenue ou d'erreur
'''
print("---------Authentification Simple----------")
Nom = "Ilyas sekhsoukhi"
Code = "Admin123@"  
Nom_Entrer = input("Entrez votre nom : ")
Code_Entrer = input("Entrez votre code : ")
if Nom_Entrer == Nom and Code_Entrer == Code:
    print("Bienvenue")
else:
    print("Euror")