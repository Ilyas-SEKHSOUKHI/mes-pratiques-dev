'''
9. Moyenne des notes
- Demande à l’utilisateur d’entrer 3 notes (dans une liste).
- Calcule et affiche la moyenne.
- Si moyenne ≥ 10 → “Admis”, sinon “Échoué”.

'''
somme = 0
Notes = [10,15,20]
for i in range(len(Notes)):
    somme = somme + Notes[i]
moyenne = somme/len(Notes)
print("la moyenne : "+str(moyenne))