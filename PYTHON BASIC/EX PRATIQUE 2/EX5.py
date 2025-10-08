'''
5. Liste d’étudiants
- Crée une liste avec 4 prénoms.
- Affiche le premier et le dernier prénom.
- Ajoute un nouveau prénom à la fin et affiche la nouvelle liste.
'''
etudiants = ["ilyas","saad","amira","aziz"]
print(etudiants)
print("Premier etudiant dans la liste : "+etudiants[0])
print("le dernier etudiant dans la liste : "+etudiants[len(etudiants)-1])
etudiants.append("oussama")
print(etudiants)