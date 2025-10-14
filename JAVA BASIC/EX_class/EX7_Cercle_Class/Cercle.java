package EX7_Cercle_Class;
/*
 * 7. Classe "Cercle"
------------------
Crée une classe `Cercle` avec :
- rayon (double)

Ajoute :
- une méthode `calculerAire()`
- une méthode `calculerPerimetre()`
- une méthode `afficherInfos()`
 */
public class Cercle {
    double rayon;
    public Cercle(double rayon){
        this.rayon = rayon;
    }
    public double calculerAire(){
        double Aire = 3.14 * (rayon*rayon);
        return Aire;
    }
    public double calculerPerimetre(){
        double Perimetre = 2 * 3.14 * rayon;
        return Perimetre;
    }
    public void afficherInfos(){
        System.out.println("Rayon : "+rayon);
        System.out.println("Aire : "+calculerAire());
        System.out.println("Perimetre : "+calculerPerimetre());
    }
}
