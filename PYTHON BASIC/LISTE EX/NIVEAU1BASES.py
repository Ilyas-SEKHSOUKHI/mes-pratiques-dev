#EX1
'''1. CRÉER ET ACCÉDER
   • Crée une liste : fruits = ["pomme", "banane", "orange"]
   • Affiche :
     - Le premier fruit
     - Le dernier fruit
     - Le nombre total de fruits'''
fruits = ["pomme","banane","orange"]
#Affichage
print("le premier fruit : "+fruits[0])
print("le dernier fruit :  "+fruits[len(fruits)-1])
print("le nombre total de fruits : "+str(len(fruits)))

#EX2
'''
2. MODIFICATIONS DE BASE
   • À partir de la liste de fruits :
     - Ajoute "fraise" à la fin
     - Ajoute "kiwi" au début
     - Supprime "banane"
     - Affiche la liste finale'''

fruits.insert(0,"fraise")
fruits.append("kiwi")
del fruits[2] #sup banane
print(fruits) #afficher la liste

#EX3
'''
3. MODIFIER UN ÉLÉMENT
   • Crée une liste de 3 pays
   • Remplace le deuxième pays par "Maroc"
   • Affiche la liste modifiée
'''
pays = ["France","china","Germany"]
pays[1]="Maroc"
print(pays)