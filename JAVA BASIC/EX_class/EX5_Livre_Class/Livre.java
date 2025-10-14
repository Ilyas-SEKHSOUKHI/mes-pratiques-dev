package EX5_Livre_Class;
/*
 * 5. Classe "Livre"
-----------------
Crée une classe `Livre` avec :
- titre (String)
- auteur (String)
- nombreDePages (int)

Ajoute :
- un constructeur
- une méthode `afficherDetails()`
 */
public class Livre { // Class
    String titre;
    String auteur;
    int nombreDePages;
    public Livre(String titre,String auteur,int nombreDePages){ // Constructeur
        this.titre = titre;
        this.auteur = auteur;
        this.nombreDePages = nombreDePages;
    }
    public void afficherDetails(){
        System.out.println("Titre : "+titre);
        System.out.println("Auteur : "+auteur);
        System.out.println("Pages Num : "+nombreDePages);
    }
}
