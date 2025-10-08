'''
4. Somme de deux nombres
Crée une fonction addition(a, b) qui retourne la somme de a et b.
Appelle la fonction et affiche le résultat.
'''
def addition(a,b):
    somme = a+b
    return somme
Num_1 = int(input("Entrez un Nombre : "))
Num_2 = int(input("Entrez un Nombre : "))
print("Resultat = "+str(addition(Num_1,Num_2)))