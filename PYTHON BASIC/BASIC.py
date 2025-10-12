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
#Les Listes
Les_Etudiant = ["Ilyas","Aziz","Oussama"] # Cree une liste
print(Les_Etudiant) # Afficher la liste
print(Les_Etudiant[0]) # Afficher le premier element
print(len(Les_Etudiant)) # Nombre d'element dans la liste
print(Les_Etudiant[len(Les_Etudiant)-1]) # Afficher le dernier element
#modification de element
Les_Etudiant[0] = "Sekhsoukhi" # Modifier le premier element
print(Les_Etudiant[0]) # Afficher l'element modifier
#injecter une valeur
Les_Etudiant.insert(2,"Saad") # injecter Saad avant oussama
print(Les_Etudiant)
# injecter une valeur a la fin de la liste 
Les_Etudiant.append("Zakaria")
print(Les_Etudiant)
Les_Etudiant.extend(["Amira","Ranya"]) # ajouter + d'element au liste
print(Les_Etudiant)
# Delete un element 
del Les_Etudiant[3] #sup oussama
Les_Etudiant.pop(1) #sup aziz
Les_Etudiant.remove("Amira")#sup Amira
print(Les_Etudiant)
# Sup Tout
Les_Etudiant.clear()
print(Les_Etudiant)
#Les Boucles
# boucle for
for Num_Client in range(1,6):
    print("Client N "+str(Num_Client))
# boucle for each : 
Emails = ["ilyas@gameil.com","Sekhsoukhi@gmai.com","Aziz@gamil.com"]
for email in Emails:
    print("Publier a : ",email)
# boucle while
Num = 0
while Num !=5: #condition Vrai donc il continue
    print("test")
    Num = Num + 1 

#Les Fonctions
def welcome_message(): # la fonction
    print("welcome")
    print("Test")

welcome_message() # appelation de la fonction
#-----------exemple 2---------------
def somme(a,b):
    print(a+b)
c = 1
d = 5
somme(c,d)
#Class / Constractor / Methode
class Player: #class
    def __init__(self,pseudo,health,attack): # Constractor
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(pseudo,health,attack) # Affichage des info de Player 1/2
    def get__pseudo(self): # Methode
        return self.pseudo
    def get__health(self): # Methode
        return self.health
    def get__attack(self): # Methode
        return self.attack

Player1 = Player("ilyas",20,5)
Player2 = Player("amira",20,2)
print(Player1) # Ne marche pas
print(Player2) # Ne marche pas
print(Player1.get__pseudo()) # Affiche le pseudo du player1
print(Player1.get__health()) # Affiche le health du player1
print(Player1.get__attack()) # Affiche le attack du player1