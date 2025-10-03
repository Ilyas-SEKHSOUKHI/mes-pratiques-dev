## Exercice 4 : Convertisseur d'âge
'''
Créez un programme qui :
- Demande l'âge de l'utilisateur
- Convertit cet âge en :
  - Mois
  - Jours (approximatif : âge × 365)
  - Heures (approximatif : jours × 24)
- Affiche tous ces résultats
'''
print("---------Convertisseur d'age-----------")
age = int(input("Entrez votre age : "))
mois = age * 12
jours = age * 365
heures = jours * 24
print("Votre age = "+str(age)+" en jours "+str(jours)+" en heures "+str(heures)+" en mois "+str(mois))