## Exercice 1 : Calculatrice d'IMC
'''
Créez un programme qui calcule l'Indice de Masse Corporelle (IMC).
- Demandez à l'utilisateur son poids (en kg) et sa taille (en m)
- Calculez l'IMC avec la formule : IMC = poids / (taille²)
- Affichez l'IMC et un message selon ces catégories :
  - < 18.5 : "Maigreur"
  - 18.5-25 : "Normal"
  - 25-30 : "Surpoids"
  - > 30 : "Obésité"
'''
print("-----------Calculatrice d'imc--------------")
Poids = float(input("Entrez votre poids"))
Taille = float(input("Entrez votre Taille"))
IMC = Poids/(Taille*Taille) # Calculer l'IMC
print(IMC)
#Les Categories
if IMC < 18.5:
    print("Maigreur")
elif IMC > 18.5 and IMC < 25:
    print("Normal")
elif IMC > 25 and IMC < 30:
    print("Surpoids")
else:
    print("obesite")
