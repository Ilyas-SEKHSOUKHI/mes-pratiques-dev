'''
3. Condition simple
- Demande à l’utilisateur d’entrer son âge.
- Si l’âge < 18 → affiche “Mineur”,
  sinon → affiche “Majeur”.
'''
age = int(input("Enrez votre age : "))
if age < 18:
    print("Mineur")
else:
    print("Majeur")