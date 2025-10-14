package EX4_Rectangle_Class;
/*
 * 4. Classe "Rectangle"
----------------------
Crée une classe `Rectangle` avec :
- longueur (double)
- largeur (double)

Ajoute :
- une méthode `calculerSurface()`
- une méthode `calculerPerimetre()`
- une méthode `afficherInfos()`
 */
public class Rectangle {
    double longueur;
    double largeur;
    public Rectangle(double longueur,double largeur){
        this.longueur = longueur;
        this.largeur = largeur; 
    }
    public double calculerSurface(){
        double surface = longueur*largeur;
        return surface;
    }
    public double calculerPerimetre(){
        double perimaitre = 2 * (longueur+largeur);
        return perimaitre;
    }
    public void afficherInfos(){
        System.out.println("Longueur : "+longueur);
        System.out.println("Largeur : "+largeur);
        System.out.println("Surface : "+calculerSurface());
        System.out.println("Perimetre : "+calculerPerimetre());
    }
}
