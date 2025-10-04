#EX4
'''
4. CALCULS SUR LES NOMBRES
   • Crée une liste de 5 nombres
   • Calcule et affiche :
     - La somme totale
     - La moyenne
     - Le plus grand nombre
     - Le plus petit nombre
'''
Numbers = [2,5,3,6,7]
somme=0
for i in range(len(Numbers)):
    somme = somme + Numbers[i]
print("La Somme : "+str(somme))
moyenne = somme / len(Numbers)
print("La moyenne : "+str(moyenne))

for i in range(len(Numbers)):
    max = Numbers[0]
    if max<Numbers[i]:
        max = Numbers[i]
print("Le plus grand nombre : "+str(max))

for i in range(len(Numbers)):
    min = Numbers[0]
    if min> Numbers[i]:
        min = Numbers[i]
print("Le plus petit nombre : "+str(min))

#EX5
'''
5. RECHERCHE D'ÉLÉMENT
   • Crée une liste d'étudiants : ["Alice", "Bob", "Charlie"]
   • Demande à l'utilisateur d'entrer un nom
   • Affiche "Présent" si le nom est dans la liste, sinon "Absent"
'''
Etudiant = ["Alice","Bob","Charlie"]
Nom = input("Entrez un Nom")
for i in range(len(Etudiant)):
    if Etudiant[i]==Nom:
        Pr = True
    else:
        Pr = False
    if Pr == True:
        break
if Pr == True:
    print("Present")
else:
    print("Absent")

#EX6
'''
6. TRI ET ORDRE
   • Crée une liste de prénoms dans le désordre
   • Trie-la par ordre alphabétique
   • Inverse l'ordre de la liste
   • Affiche les deux versions
'''
Prenoms = ["Ilyas","Amine","Saad","Oussama"]
print(Prenoms)
# Trie la liste par ordre alphabétique (modifie la liste originale)
Prenoms.sort()
print(Prenoms)
# Inverse l'ordre de la liste
Prenoms.reverse()
print(Prenoms)
#EX6 A Reviser