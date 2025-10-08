'''
10. Fonction principale (main)
Crée une fonction main() qui demande à l’utilisateur d’entrer deux nombres,
puis affiche la somme, la différence, le produit et le quotient,
en appelant des fonctions séparées pour chaque opération.

'''
def main():
    global Nombre_1
    global Nombre_2
    Nombre_1 = int(input("Entrez un Nombre : "))
    Nombre_2 = int(input("Entrez un Nombre : "))
    return Nombre_1,Nombre_2
print("les valeur entrer : "+str(main()))

def somme(a,b):
    S = a+b
    return S
print("La somme = "+str(somme(Nombre_1,Nombre_2)))

def soustraction(a,b):
    M = a-b
    return M
print("La soustraction = "+str(soustraction(Nombre_1,Nombre_2)))

def multiplication(a,b):
    N = a*b
    return N
print("La multiplication = "+str(multiplication(Nombre_1,Nombre_2)))

def division(a,b):
    D = a/b
    return D
print("La division = "+str(division(Nombre_1,Nombre_2)))