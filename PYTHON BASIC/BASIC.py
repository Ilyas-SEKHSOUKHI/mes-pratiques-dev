#BASIC 
print("Hello World") # Pour Afficher
# Les Variable
username = "ilyas" # var string
age = 85 # var int
wallet = 100.12 # var float
isHappy = True # var Bool
# Affichage des var 
print(username,age) 
print(wallet,isHappy)
# la fonction str pour que la var age se transforme de int to string
print("Salut "+username+" vous avez "+str(age)+" ans") 
# recolter des valeur de l'utilisateur
ProductName = input("Entrez le nom du produit") #pour que le user entre le nom du produit
Price = int(input("Entrez le prix du produit")) #pour que le user entre le prix 
#le int car la valeur entrez par user va etre string 
TVA = (20*Price)/100 # on a transformer Pric en int pour l'inclure dans cette operation 
Totale = Price-TVA
print("le Nom du Produit "+ProductName+" le prix "+str(Price)+" la tva 20% "+str(TVA)+" le totale apres la tva "+str(Totale))
#Les conditions
#Exemple 1
if age<=20 :
    print("Petit")
elif age>20 and age<60 :
    print("Adulte")
else:
    print("Vieux") 
#Exemple 2
wallet = 500
Prix_Produit = 20
if wallet < Prix_Produit:
    print("Euror")
else:
    print("Achat accepte")
    wallet = wallet - Prix_Produit
    print("la valeur de votre wallet = "+str(wallet))
    print("la valeur de votre wallet = {}".format(wallet))