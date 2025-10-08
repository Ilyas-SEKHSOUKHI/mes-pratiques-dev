'''
6. Calcul de moyenne
Crée une fonction moyenne(note1, note2, note3) qui calcule et retourne la moyenne de trois notes.
Si la moyenne ≥ 10 → “Admis”, sinon → “Échoué”.
'''
def moyenne(note1,note2,note3):
    somme = note1+note2+note3
    m = somme/3
    return m
Note_1 = int(input("Entrez votre note : "))
Note_2 = int(input("Entrez votre note : "))
Note_3 = int(input("Entrez votre note : "))
print("Votre moyenne = "+str(moyenne(Note_1,Note_2,Note_3)))