'''
3. Fonction avec retour de valeur
Crée une fonction carre(nombre) qui retourne le carré du nombre passé en paramètre.
Exemple : carre(4) → 16
'''
def carre(nombre):
    Resultat = nombre*nombre
    return Resultat
Num = int(input("Entrez un Nombre : "))
print(" Carre de "+str(Num)+" = "+str(carre(Num)))