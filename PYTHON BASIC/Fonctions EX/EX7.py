'''
7. Factorielle
Crée une fonction factorielle(n) qui calcule la factorielle d’un nombre à l’aide d’une boucle.
'''

def factorielle(n):
    Resultat = 1
    for i in range(n+1):
        if i != 0:
            Resultat = Resultat * i
    return Resultat
Numbre = int(input("Entrez un Nombre : "))
print(factorielle(Numbre))