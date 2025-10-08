'''
9. Plus grand nombre
Crée une fonction max3(a, b, c) qui retourne le plus grand des trois nombres.
'''
def max3(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c<b:
        print(c)
    else:
        print("Euror")
Numbre_1 = int(input("Entrez un Nombre : "))
Numbre_2 = int(input("Entrez un Nombre : "))
Numbre_3 = int(input("Entrez un Nombre : "))
print(max3(Numbre_1,Numbre_2,Numbre_3))