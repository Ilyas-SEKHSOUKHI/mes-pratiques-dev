'''
8. Mini-calculatrice
- Demande à l’utilisateur de choisir une opération (+, -, *, /).
- Demande deux nombres et affiche le résultat.
'''
Numbre1 = int(input("Entrez un Nombre : "))
operation = input("Entrez operation : ")
Numbre2 = int(input("Entrez un nombre : "))
if operation == "+":
    somme = Numbre1+Numbre2
    print("Resultat : "+str(somme))
elif operation == "-":
    soustraction = Numbre1-Numbre2
    print("soustraction : "+str(soustraction))
elif operation == "*":
    mlt = Numbre1*Numbre2
    print("multiplication : "+str(mlt))
elif operation == "/":
    div = Numbre1/Numbre2
    print("division : "+str(div))
else:
    print("Euror")