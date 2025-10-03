## Exercice 3 : Système de notes
'''
Créez un programme qui :
- Demande à l'utilisateur d'entrer 3 notes (sur 20)
- Calcule la moyenne
- Affiche la moyenne et la mention :
  - < 10 : "Échec"
  - 10-14 : "Passable"
  - 14-16 : "Bien"
  - 16-18 : "Très bien"
  - > 18 : "Excellent"
'''
print("--------Systeme de notes-----------")
print("Entrez 3 Notes sur 20")
Premiere_Note = float(input("Entrez la premiere note"))
Deuxieme_Note = float(input("Entrez la deuxieme note"))
Troisieme_Note = float(input("Entrez la troisieme note"))
Moyenne = (Premiere_Note+Deuxieme_Note+Troisieme_Note)/3
if Moyenne<10:
    print("Echec")
elif Moyenne>=10 and Moyenne<14:
    print("Passable")
elif Moyenne>=14 and Moyenne<16:
    print("Bien")
elif Moyenne>=16 and Moyenne<18:
    print("Tres Bien")
else:
    print("Excellent")