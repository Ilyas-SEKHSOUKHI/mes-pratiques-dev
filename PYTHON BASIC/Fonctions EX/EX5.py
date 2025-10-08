'''
5. Vérification pair ou impair
Crée une fonction pair_ou_impair(n) qui affiche si le nombre est pair ou impair.
'''
def pair_ou_impaire(n):
    if n%2==0:
        return "pair"
    else:
        return "impair"
Numbre = int(input("Entrez un Nombre : "))
print(pair_ou_impaire(Numbre))